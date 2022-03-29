import requests
import json

def cnpj_info(cnpj_value):
	url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj_value}"
	resp = requests.get(url)
	data = resp.json()
	funcs = []
	cnpjsocio = []
	qualificacao = []
	idade = []
	entrada = []
	desc = data['identificador_matriz_filial']
	if desc == 1:
	   descricao = 'Matriz'
	if desc == 2:
	   descricao = 'Filial'
	razao_social = data['razao_social']
	nome = data['nome_fantasia']
	desc_situacao = data['descricao_situacao_cadastral']
	data_situacao = data['data_situacao_cadastral']
	inicio_atividade = data['data_inicio_atividade']
	cnae_fiscal = data['cnae_fiscal']
	cnae_fiscal_descricao = data['cnae_fiscal_descricao']
	uf = data['uf']
	municipio = data['municipio']
	cep = data['cep']
	bairro = data['bairro']
	logradouro = data['logradouro']
	numero = data['numero']
	complemento = data['complemento']
	telefone1 = data['ddd_telefone_1']
	telefone2 = data['ddd_telefone_2']
	porte = data['porte']
	natureza = data['natureza_juridica']
	fax = data['ddd_fax']
	print(f"RAZAO SOCIAL: {razao_social} \nDESCRICAO: {descricao}\nNOME FANTASIA: {nome} \nSITUACAO CADASTRAL: {desc_situacao} \nDATA CADASTRO: {data_situacao} \nINICIO DA ATIVIDADE: {inicio_atividade} \nCNAE FISCAL: {cnae_fiscal} \nCNAE DESCRICAO: {cnae_fiscal_descricao} \nESTADO: {uf} \nMUNICIPIO: {municipio} \nCEP: {cep} \nBAIRRO: {bairro} \nLOGRADOURO: {logradouro},{complemento} \nNUMERO: {numero} \nTELEFONE 1: {telefone1} \nTELEFONE 2: {telefone2} \nPORTE: {porte} \nNATUREZA JURIDICA: {natureza} \nFAX: {fax} \n")
	
	print(f"QUANTIDADE DE FUNCIONARIOS: {len(data['qsa'])}\n")
	for i in range(0, len(data['qsa'])):
		funcs.append(data['qsa'][i]['nome_socio'])
		cnpjsocio.append(data['qsa'][i]['cnpj_cpf_do_socio'])
		qualificacao.append(data['qsa'][i]['qualificacao_socio'])
		idade.append(data['qsa'][i]['faixa_etaria'])
		entrada.append(data['qsa'][i]['data_entrada_sociedade'])
		print(f"NOME DO FUNCIONARIO: {funcs[i]}")
		print(f"CNPJ/CPF DO FUNCIONARIO: {cnpjsocio[i]}")
		print(f"QUALIFICACAO: {qualificacao[i]}")
		print(f"IDADE: {idade[i]}")
		print(f"DATA DE ENTRADA: {entrada[i]}\n------------------------------------------------")
