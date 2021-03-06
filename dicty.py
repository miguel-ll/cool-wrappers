from bs4 import BeautifulSoup #and pip install lxml
import requests
import re

def desc(wd):
    wd = re.sub(" ", "-", wd)
    u = f"https://www.dictionary.com/browse/{wd}"
    url = requests.get(u)
    soup = BeautifulSoup(url.text, features='lxml')
    try:
        result = soup.body.find('span', attrs={'class' :'one-click-content'}).text
    except:
        return
    return result.capitalize()

def ptdesc(wd):
    wd = re.sub(" ", "-", wd)
    u = f"https://www.lexico.pt/{wd}"
    url = requests.get(u)
    soup = BeautifulSoup(url.text, features='lxml')
    try:
        result = soup.body.find('p', attrs={'id' : 'significado'}).text
    except:
        return
    return result

def ptdesc2(wd):
    wd = re.sub(" ", "-", wd)
    u = f"https://www.dicio.com.br/{wd}"
    url = requests.get(u)
    soup = BeautifulSoup(url.text, features='lxml')
    try:
        result = soup.body.find('p', attrs={'class' : 'significado'}).text
    except:
        return
    result2 = soup.body.find('p', attrs={'class' : 'adicional'})
    li = []
    for res in result2.find_all('a'):
        li.append(res.get_text())
    # essa funcao retorna result (o significado), e li (uma lista, sendo o primeiro elemento o plural da palavra e o segundo a versao feminina, caso exista.)
    return result,li
