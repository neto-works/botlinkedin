import os
import platform
import subprocess
from decouple import config
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TEMPO_ESPERADO_ACESSSAR = 30
SECRET_E = config('SECRET_EMAIL')
SECRET_P = config('SECRET_PASSWORD')

def identificar_sistema() -> str:
    sistema = platform.system()
    if sistema == "Windows":
        return os.path.abspath(os.getcwd()) + "\\windows\\chromedriver.exe"
    elif sistema == "Linux":
        return os.path.abspath(os.getcwd()) + "/linux/chromedriver"
    else:
        raise Exception("Sistema operacional não reconhecido: " + sistema)

chrome_driver_path = identificar_sistema()

if platform.system() == "Linux":
    comando_chmod = ['chmod', '+x', chrome_driver_path]
    subprocess.run(comando_chmod)

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://www.linkedin.com/login/")

    username = WebDriverWait(driver, TEMPO_ESPERADO_ACESSSAR).until(EC.visibility_of_element_located((By.ID, 'username')))
    username.send_keys(SECRET_E)

    password = WebDriverWait(driver, TEMPO_ESPERADO_ACESSSAR).until(EC.visibility_of_element_located((By.ID, 'password')))
    password.send_keys(SECRET_P)

    login_button = WebDriverWait(driver, TEMPO_ESPERADO_ACESSSAR).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn__primary--large')))
    login_button.click()

    WebDriverWait(driver, TEMPO_ESPERADO_ACESSSAR).until(EC.url_changes("https://www.linkedin.com/login/"))

    driver.get("https://www.linkedin.com/mynetwork/grow/")

    while True:
        try:
            # Localizar todos os botões que contêm "Conectar"
            buttons = WebDriverWait(driver, TEMPO_ESPERADO_ACESSSAR).until(EC.presence_of_all_elements_located((By.XPATH, '//button[contains(@aria-label, "Convidar") and .//span[text()="Conectar"]]')))

            for button in buttons:
                try:
                    if button.is_displayed():
                        button.click()
                        print("Botão 'Conectar' clicado.")
                        time.sleep(2)  # Esperar 2 segundos antes de procurar o próximo botão
                except Exception as e:
                    print(f"Erro ao tentar clicar no botão: {e}")

            # Esperar antes de tentar encontrar novos elementos
            time.sleep(10)

            # Recarregar a página para procurar novos botões, se necessário
            driver.refresh()

        except Exception as e:
            print(f"Erro encontrado: {e}")
            time.sleep(40)

finally:
    print("Feche o navegador para terminar a execução.")
    while True:
        try:
            time.sleep(60)
        except KeyboardInterrupt:
            break

print("Fim da execução")
