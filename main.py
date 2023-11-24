import pandas as pd
import json

from api.api_services import obter_token
from api.api_services import listar_apontamentos
from data.dataframe import importa_dados

def main():
    
    print("\nBem-vindo(a) a API da Kartado! Digite suas credenciais de acesso:\n")
    
    username = input("Username de acesso: ")
    password = input("Senha de acesso: ")

    #Intervalo de Km a ser consultado
    intervalo_km = float(input("\nIntervalo de quilômetros a ser consultado: "))

    #Filtro de Status:
    filtro = input("\nDeseja aplicar filtro de status? Digite S ou N \n")

    while filtro != "S" and filtro != "N":
        print("Inspira uma resposta válida!")
        filtro = input("Deseja aplicar filtro de status? Digite S ou N")
    
    print("\nAguarde...\n")
    
    #Credenciais de teste, para deixar como padrão, apenas descomentar as duas linhas abaixo:
    # username = "jhonathanmachado"
    # password = "LXGhBHP9q7"

    token = obter_token(username, password)
    apontamento_dados_service = listar_apontamentos(token)
    
    with open("./data/dados.json",'w') as arquivo:
        json.dump(apontamento_dados_service, arquivo)

    dados_tabela = importa_dados()

    #Aplicando filtro de status
    if filtro == 'S':
        status = dados_tabela['status'].drop_duplicates()
        status = list(status)
        
        print("\nForam encontrados os seguintes status: ")
        print(status)
 
        status_desejado = input("\nDigite o status a ser filtrado: ")

        while status_desejado not in status:
            print("Inspira um status válido.")
            status_desejado = input("Digite o status a ser filtrado: ")
        
        dados_tabela = dados_tabela[dados_tabela['status']==status_desejado]

    #Aplicando filtro de intervalo de km
    dados_tabela = dados_tabela[dados_tabela['km']<=intervalo_km]

    #Informações sobre o dataFrame
    num_linhas, num_colunas = dados_tabela.shape
    print(f'O DataFrame tem {num_linhas} linhas e {num_colunas} colunas.')

    dados_tabela.to_excel('./data/tabela_dados_kartado.xlsx', index=False)
    print("Os dados do Dataframe já estão prontos e podem ser acessados em: consulta_api_kartado/dados/tabela_dados_kartado.xlsx \n")

if __name__ == "__main__":
    main()
