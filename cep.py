import requests
import json

def cep_info(cepnum):
    url = f'https://brasilapi.com.br/api/cep/v2/{cepnum}'
    resp = requests.get(url)
    data = resp.json()
    cep = data['cep']
    estado = data['state']
    cidade = data['city']
    bairro = data['neighborhood']
    rua = data['street']
    longitude = data['location']['coordinates']['longitude']
    latitude = data['location']['coordinates']['latitude']
    opm_link = f"https://www.openstreetmap.org/search?query={latitude}%2C{longitude}"
    lonlat = f"{longitude},{latitude}"
    return cep, estado, cidade, bairro, rua, lonlat, opm_link

def cep_infov2(cepnum):
    url = f'https://brasilapi.com.br/api/cep/v2/{cepnum}'
    resp = requests.get(url)
    data = resp.json()
    cep = data['cep']
    estado = data['state']
    cidade = data['city']
    bairro = data['neighborhood']
    rua = data['street']
    longitude = data['location']['coordinates']['longitude']
    latitude = data['location']['coordinates']['latitude']
    opm_link = f"https://www.openstreetmap.org/search?query={latitude}%2C{longitude}"
    print(f"CEP: {cep} \nESTADO: {estado} \nCIDADE: {cidade} \nBAIRRO: {bairro} \nRUA: {rua} \nLONGITUDE, LATITUDE: {longitude},{latitude} \nOPMaps link: {opm_link}")
