import pandas as pd
import json

#Abrindo arquivo json e retorna um dataframe
def abre_arquivo_json():
    with open('./data/dados.json', 'r') as arquivo:
    
        dados_json = json.load(arquivo)
        df_json = pd.DataFrame(dados_json['response']['data'])
    
    return df_json


#Função auxiliar para verificar valor nulo
def verifica_nulo(dic, key):
  if dic['data'] != None:
    return dic['data'][key]
  return None


#Função para inserir item no DataFrame
def insere_item(attributes, relationships, stepBuilding):
  #uuid
  df['uuid'].append(attributes['uuid'])

  #numero
  df['numero'].append(attributes['number'])

  #rodovia
  df['rodovia'].append(attributes['roadName'])

  #km
  df['km'].append(attributes['km'])

  #kmFinal
  df['kmFinal'].append(attributes['endKm'])

  #latitude
  df['latitude'].append(attributes['point']['coordinates'][0])

  #longitude
  df['longitude'].append(attributes['point']['coordinates'][1])

  #faixa
  df['faixa'].append(attributes['lane'])

  #track
  df['track'].append(attributes['track'])

  #branch
  df['branch'].append(attributes['branch'])

  #kmReference
  df['kmReference'].append(attributes['kmReference'])

  #sentido
  df['sentido'].append(attributes['direction'])

  #status
  df['status'].append(relationships['status']['data']['type'])

  #criadoPor
  df['criadoPor'].append(relationships['createdBy']['data']['id'])

  #empresa
  df['empresa'].append(relationships['company']['data']['id'])

  #job
  job = verifica_nulo(relationships['job'], 'id')
  df['job'].append(job)

  #criadoEm
  df['criadoEm'].append(attributes['createdAt'])

  #encontradoEm
  df['encontradoEm'].append(attributes['foundAt'])

  #atualizadoEm
  df['atualizadoEm'].append(attributes['updatedAt'])

  #executadoEm
  df['executadoEm'].append(attributes['executedAt'])

  #preco
  df['preco'].append(attributes['price'])

  #comprimento
  df['comprimento'].append(stepBuilding['comprimento'])

  #largura
  df['largura'].append(stepBuilding['largura'])

  #height/altura
  df['altura'].append(stepBuilding['altura'])

  #volume
  df['volume'].append(stepBuilding['volume'])

  return df

#Percorre o json para inserir os registros
def percorre_json():

    for i, j in df_json.iterrows():

        item_attributes = df_json['attributes'][i]
        item_relationships = df_json['relationships'][i]

        #Verifica quais registros possuem StepBuilding 
        if item_attributes['formData'].get('stepBuilding', False):
            
            #Para cada item da lista em stepBuilding
            for k in item_attributes['formData']['stepBuilding']:

                #comprimento/width
                comprimento = k['width']

                #altura/height
                altura = k['height']

                #largura/lenght
                largura = k['length']

                #volume
                volume = k['volume']

                item_stepBuilding = { 'comprimento': comprimento, 'altura': altura, 'largura': largura ,'volume': volume}
                insere_item(item_attributes, item_relationships, item_stepBuilding)
        
        else:
            item_stepBuilding = { 'comprimento': None, 'altura': None, 'largura': None ,'volume': None}
            insere_item(item_attributes, item_relationships, item_stepBuilding)


#Inicia a importação de dados
def importa_dados():
    global df_json, df

    #Define estrutura da tabela de saída
    df = {
        "uuid": [],
        "numero": [],
        "rodovia": [],
        "km": [],
        "kmFinal": [],
        "latitude": [],
        "longitude": [],
        "comprimento": [],
        "largura": [],
        "altura": [],
        "faixa": [],
        "track": [],
        "branch": [],
        "kmReference": [],
        "sentido": [],
        "status": [],
        "criadoPor": [],
        "empresa": [],
        "job": [],
        "criadoEm": [],
        "encontradoEm": [],
        "atualizadoEm": [],
        "executadoEm": [],
        "preco": [],
        "volume": []
        }
    
    df_json = abre_arquivo_json()
    percorre_json()
    dados_tabela = pd.DataFrame(df)

    return dados_tabela
