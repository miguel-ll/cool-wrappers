import requests
import json
import re

def obj_info(obj_value):
    url = f"https://proxyapp.correios.com.br/v1/sro-rastro/{obj_value}"
    resp = requests.get(url)
    data = resp.json()
    cod_obj = data['objetos'][0]['codObjeto']
    previsao = data['objetos'][0]['dtPrevista']
    previsao = re.sub('T', ' ', previsao)
    status = data['objetos'][0]['eventos'][0]['descricao']
    criado = data['objetos'][0]['eventos'][0]['dtHrCriado']
    criado = re.sub('T', ' ', criado)
    endereco1 = data['objetos'][0]['eventos'][0]['unidade']['endereco']['cidade']
    endereco2 = data['objetos'][0]['eventos'][0]['unidade']['endereco']['uf']
    destino1 = data['objetos'][0]['eventos'][0]['unidadeDestino']['endereco']['cidade']
    destino2 = data['objetos'][0]['eventos'][0]['unidadeDestino']['endereco']['uf']
    destinatario = data['objetos'][0]['eventos'][1]['destinatario']
    endereco_atual = f"{endereco1}, {endereco2}"
    destino_atual = f"{destino1}, {destino2}"
    return cod_obj, previsao, status, criado, endereco_atual, destino_atual, destinatario

def obj_infov2(obj_value):
    url = f"https://proxyapp.correios.com.br/v1/sro-rastro/{obj_value}"
    resp = requests.get(url)
    data = resp.json()
    cod_obj = data['objetos'][0]['codObjeto']
    previsao = data['objetos'][0]['dtPrevista']
    previsao = re.sub('T', ' ', previsao)
    status = data['objetos'][0]['eventos'][0]['descricao']
    criado = data['objetos'][0]['eventos'][0]['dtHrCriado']
    criado = re.sub('T', ' ', criado)
    endereco1 = data['objetos'][0]['eventos'][0]['unidade']['endereco']['cidade']
    endereco2 = data['objetos'][0]['eventos'][0]['unidade']['endereco']['uf']
    destino1 = data['objetos'][0]['eventos'][0]['unidadeDestino']['endereco']['cidade']
    destino2 = data['objetos'][0]['eventos'][0]['unidadeDestino']['endereco']['uf']
    destinatario = data['objetos'][0]['eventos'][1]['destinatario']
    endereco_atual = f"{endereco1}, {endereco2}"
    destino_atual = f"{destino1}, {destino2}"
    print(f"CODIGO: {cod_obj} \nPREVISAO DE ENTREGA: {previsao} \nSTATUS: {status} \nVIAGEM INICIADA EM: {criado} \nENDERECO ATUAL: {endereco1}, {endereco2} \nDESTINO ATUAL: {destino1}, {destino2} \nDESTINATARIO: {destinatario}")
