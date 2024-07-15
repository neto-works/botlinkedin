import os
import time
import platform
import subprocess
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_driver_path = ""

def identificar_sistema() -> str:
    sistema = platform.system()
    if sistema == "Windows":
        return os.path.abspath(os.getcwd()) + "/windows/chromedriver.exe"
    elif sistema == "Linux":
        return os.path.abspath(os.getcwd()) + "/linux/chromedriver"
    else:
        print("Sistema operacional não reconhecido:", sistema)


chrome_driver_path = identificar_sistema()

# Dar permissão de execução apenas no Linux
if platform.system() == "Linux":
    comando_chmod = ['chmod', '+x', chrome_driver_path]
    subprocess.run(comando_chmod)

# Configurar opções do Chrome (se necessário)
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Rodar em modo headless (sem interface gráfica)

# Inicializar o serviço do ChromeDriver
service = Service(chrome_driver_path)

# Inicializar o WebDriver passando o serviço do ChromeDriver e opções do Chrome
driver = webdriver.Chrome(service=service, options=chrome_options)

# Abrir um site
driver.get("https://www.linkedin.com")
#driver.get("https://www.linkedin.com/mynetwork/grow/")

# Esperar um pouco para a página carregar
time.sleep(5)

# Exemplo de interação com um elemento na página (aqui usando Selenium)
element = driver.find_element_by_name("q")
element.send_keys("Hello, Selenium!")
element.send_keys(Keys.RETURN)

# Esperar um pouco para ver os resultados
time.sleep(5)

# Fechar a janela do navegador
driver.quit()

# Exemplo de uso de BeautifulSoup para parsing HTML (não está sendo usado no seu código atualmente)
# html = urlopen("https://www.linkedin.com/mynetwork/grow/")
# bs = BeautifulSoup(html.read(),"html.parser")
# print(bs)

print("Caminho para o ChromeDriver:", chrome_driver_path)