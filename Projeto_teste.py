
# Bibliotecas
import json
import requests #para solicitações http

#Função 
def CEPConsulta():
    print('+++++++++++++++++++++')
    print('######Consultando o  CEP ######')
    print('+++++++++++++++++++++')
    print()

    cep_input = input('Digite o CEP para a consulta: ')
#Inserindo uma opção caso passe quantidades do número do cep
    if len(cep_input) != 8:
        print('Quantidade de digitos inválido')
        exit()

#API com alteração no cep e colocando um dicionário
    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    addres_data = request.json()

    if 'erro' not in addres_data:
        print('>>>>>>>>>>>> SEGUE AS INFORMAÇÕES ENCONTRADAS: <<<<<<<<<<<<')
        print('logradouro: {}'.format(addres_data['cep']))
        print('complemento: {}'.format(addres_data['complemento']))
        print('Bairro: {}'.format(addres_data['bairro']))
        print('Cidade: {}'.format(addres_data['localidade']))
        print('Estado: {}'.format(addres_data['uf']))

# caso de erro de Cep:
    else:
        print('{}: CEP inválido.'.format(cep_input))

#opção para colocar dar continuidade

    opcao = int(input('Deseja realizar uma nova consulta ?\n1. Sim \n2. Sair\n'))
    if opcao == 1:
        CEPConsulta()
    else:
        print('Consulta finalizada')

CEPConsulta()

