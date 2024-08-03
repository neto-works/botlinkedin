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

<button aria-label="Pendente, clique para retirar o convite enviado a Rusdrael Antony de Araújo Freire" id="ember518" class="artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--full artdeco-button--secondary ember-view full-width" type="button">        
<svg role="none" aria-hidden="true" class="artdeco-button__icon " xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="clock-small">
<!---->    <use href="#clock-small" width="16" height="16"></use>
</svg>


<span class="artdeco-button__text">
    Pendente
</span></button>