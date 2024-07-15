from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.linkedin.com/mynetwork/grow/")
bs = BeautifulSoup(html.read(),"html.parser")
print(bs)