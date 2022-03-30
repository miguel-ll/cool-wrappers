from bs4 import BeautifulSoup
import requests

# Amount can be a float or an int, From and To must be strings (the currency code in three letters, e.g USD, EUR)

def converter(Amount, From, To):
    u = f"https://www.xe.com/currencyconverter/convert/?Amount={Amount}&From={From.upper()}&To={To.upper()}"   
    url = requests.get(u)
    soup = BeautifulSoup(url.text, features='lxml')
    result = soup.body.find('p', attrs={'class' : 'result__BigRate-sc-1bsijpp-1'}).text
    return result
