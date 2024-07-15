import os
import time
import platform
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = ""

def identificar_sistema():
    sistema = platform.system()
    if sistema == "Windows":
        return os.path.abspath(os.getcwd()) + "/chromedriver_win32"
    elif sistema == "Linux":
        return os.path.abspath(os.getcwd()) + "/chromedriver_linux64"
    else:
        print("Sistema operacional não reconhecido:", sistema)

chrome_driver_path = identificar_sistema()
html = urlopen("https://www.linkedin.com/mynetwork/grow/")
bs = BeautifulSoup(html.read(),"html.parser")
#print(bs)
print(chrome_driver_path)