import os
import platform
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TEMPO_ESPERADO_ACESSSAR = 30

def identificar_sistema() -> str:
    sistema = platform.system()
    if sistema == "Windows":
        return os.path.abspath(os.getcwd()) + "\\windows\\chromedriver.exe"
    elif sistema == "Linux":
        return os.path.abspath(os.getcwd()) + "/linux/chromedriver"
    else:
        raise Exception("Sistema operacional não reconhecido: " + sistema)

chrome_driver_path = identificar_sistema()

# Dar permissão de execução apenas no Linux
if platform.system() == "Linux":
    comando_chmod = ['chmod', '+x', chrome_driver_path]
    subprocess.run(comando_chmod)

# Configurar opções do Chrome (se necessário)
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Rodar em modo headless (sem interface gráfica)

# Inicializar o serviço do ChromeDriver
service = Service(chrome_driver_path)

# Inicializar o WebDriver passando o serviço do ChromeDriver e opções do Chrome
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Acessar a página de login do LinkedIn
    driver.get("https://www.linkedin.com/login/")

    # Esperar até que o campo de nome de usuário esteja presente e visível  (componente react montar)
    username = WebDriverWait(driver, TEMPO_ESPERADO_ACESSSAR).until(EC.visibility_of_element_located((By.ID, 'username')))
    username.send_keys('jhonasGuthierres@gmail.com')

    # Esperar até que o campo de senha esteja presente e visível (componente react montar)
    password = WebDriverWait(driver, TEMPO_ESPERADO_ACESSSAR).until(EC.visibility_of_element_located((By.ID, 'password')))
    password.send_keys('JonasGutherres123')

    # Esperar até que o botão de login esteja presente e visível e clicar nele
    login_button = WebDriverWait(driver, TEMPO_ESPERADO_ACESSSAR).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn__primary--large')))
    login_button.click()

    # Esperar um pouco para a página carregar
    WebDriverWait(driver, TEMPO_ESPERADO_ACESSSAR).until(EC.url_changes("https://www.linkedin.com/login/"))

    # Abrir a aba de newtwork
    driver.get("https://www.linkedin.com/mynetwork/grow/")

    # Esperar um pouco para a página carregar
    WebDriverWait(driver, TEMPO_ESPERADO_ACESSSAR).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'artdeco-button__icon')))

    # Exemplo de interação com um elemento na página (corrija o seletor CSS conforme necessário)
    button = driver.find_element(By.CSS_SELECTOR, 'artdeco-button__icon')
    button.click()

finally:
    driver.quit()
    
    # Fechar a janela do navegador, 
    # pra fazer booot colocar em loop ficar seguindo ou adicionando pessoas
    # outra abordagem que vc pode querer fazer é mapear o meet para entrar reunião e depois de um horario exato finalizar o loop e sair
print("Fim da execução ")
