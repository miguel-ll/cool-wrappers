import requests
import json

def ddd_info(dddvalue):
    url = f"https://brasilapi.com.br/api/ddd/v1/{dddvalue}"
    resp = requests.get(url)
    data = resp.json()
    estado = data['state']
    cidades = []
    for i in range(0, len(data['cities'])):
        cidades.append(data['cities'][i])
    cidades = ", ".join(cidades)
    return estado, cidades

def ddd_infov2(dddvalue):
    url = f"https://brasilapi.com.br/api/ddd/v1/{dddvalue}"
    resp = requests.get(url)
    data = resp.json()
    estado = data['state']
    cidades = []
    for i in range(0, len(data['cities'])):
        cidades.append(data['cities'][i])
    cidades = ", ".join(cidades)
    print(f"ESTADO: {estado} \nCIDADES: {cidades}")
