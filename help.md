 - Pra usar webdrive compativeltu tem que baixar uma versão do chrome de acordo com a ultima versao do web drive 
 - E tem que fazer ele não atualizar - ou seja modificar google updates arquivos

usar bs4 para obte rhtml das paginas e percorrer
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.linkedin.com/login/")
bs = BeautifulSoup(html.read(), "html.parser")  #mudar o parser se quizer trazer html maisformatado

print(bs)

- pip3 install lxml
- pip3 install html5lib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml

html = urlopen("http://pythonscraping.com/pages/page1.html")
bs = BeautifulSoup(html.read(), "lxml")
print(bs.contents)