
import urllib.request
import json
import requests

print('++++++++++++++++++++++++++')
print('######Consultando o  CEP ######')
print('++++++++++++++++++++++++++')
print()

cep_input = input('Digite o CEP para a consulta: ')

if len(cep_input) != 8:
    print('Quantidade de digitos inválido')
    exit()

request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

addres_data = request.json()

if 'erro' not in addres_data:
    print('++++ SEGUE AS INFORMAÇÕES ENCONTRADAS: ++++')
    print('logradouro: {}'.format(addres_data['cep']))
    print('complemento: {}'.format(addres_data['complemento']))
    print('Bairro: {}'.format(addres_data['bairro']))
    print('Cidade: {}'.format(addres_data['localidade']))
    print('Estado: {}'.format(addres_data['uf']))
    
else:
    print('{}: CEP inválido.'.format(cep_input))

