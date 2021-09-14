from bs4 import BeautifulSoup

import requests

site = requests.get("https://www.climatempo.com.br/").content
#objeto site recebendo o conteúdo da requisição http do site
soup = BeautifulSoup(site, "html.parser")
#objeto soup baixando html do site
print(soup.prettify())
#transforma html em string e exibe

#temperature = soup.find("span", class_="_block _margin-b-5 -gray")
#print(temperature.string)
#print(soup.title.string)
#print(soup.find("admin"))