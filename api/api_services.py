import requests
import json


BASE_URL = "https://api.kartado.com.br"
COMPANY = "7c7b39ac-7711-420a-9402-0859df283634"
REPORTINGS = "146979ce-8145-488f-97e6-41f84fe7de08"

# Este método é responsável por realizar uma request ao serviço de Autenticação/Autorização da Katardo API.
# Este método retorna um token JWT para concessão de acesso aos demais serviços da Katardo API.
def obter_token(usuario, senha):
        try:
            auth_url = f"{BASE_URL}/token/login/"
            payload = json.dumps({
                "data": {
                    "type": "ObtainJSONWebToken",
                    "attributes": {
                        "username": f"{usuario}",
                        "password": f"{senha}"
                    }
                }
            })
            headers = {
                'Content-Type': 'application/vnd.api+json'
            }

            response = requests.post(auth_url, headers=headers, data=payload) 
            if response.status_code == 200:
                return response.json()['data']['token']
            else:
                response.raise_for_status()
                
        except requests.exceptions.RequestException as e:
                print(response.status_code, response)
                print(e)

# Este método é responsável por realizar uma request ao serviço de "listagem de apontamentos" da Katardo API.
# Este método retorna um dict contendo a response da request e a quantidade de páginas do json de retorno.
def listar_apontamentos(token):
        try:
            token = "JWT " + token
            url = f"{BASE_URL}/Reporting/?company={COMPANY}"
            
            headers = {
                'Authorization': token
            }
            response = requests.get(url, headers=headers) 
            
            if response.status_code == 200:
                total_paginas = lista_qtde_paginas(response.json())
                return {'response': response.json(), 'total_paginas': total_paginas}
            elif response.status_code == 403:
                 print(f"Código {response.status_code}: este usuário não tem permissão para executar essa ação.")
            else:
                response.raise_for_status()
            
        except requests.exceptions.RequestException as e:
                print(f"Erro na request: {e}")

# Este método é responsável por realizar uma request ao serviço de "listagem de classes" da Katardo API.
# Este método retorna um dict contendo a response da request e a quantidade de páginas do json de retorno.
def listar_classes(token):
        try:
            token = "JWT " + token
            url = f"{BASE_URL}/Reporting/?company={COMPANY}"
            
            headers = {
                'Authorization': token
            }
            response = requests.get(url, headers=headers) 
            
            if response.status_code == 200:
                total_paginas = lista_qtde_paginas(response.json())
                return {'response': response.json(), 'total_paginas': total_paginas}
            elif response.status_code == 403:
                 print(f"Código {response.status_code}: este usuário não tem permissão para executar essa ação.")
            else:
                response.raise_for_status()
            
        except requests.exceptions.RequestException as e:
                print(f"Erro na request: {e}")

# Este método é responsável por realizar uma request ao serviço de "listagem de equipamentos rdo" da Katardo API.
# Este método retorna um dict contendo a response da request e a quantidade de páginas do json de retorno.
def listar_equipamentos_rdo(token):
        try:
            token = "JWT " + token
            url = f"{BASE_URL}/Reporting/?company={COMPANY}&reportings={REPORTINGS}"
            
            headers = {
                'Authorization': token
            }
            response = requests.get(url, headers=headers) 
            
            if response.status_code == 200:
                total_paginas = lista_qtde_paginas(response.json())
                return {'response': response.json(), 'total_paginas': total_paginas}
            elif response.status_code == 403:
                 print(f"Código {response.status_code}: este usuário não tem permissão para executar essa ação.")
            else:
                response.raise_for_status()
            
        except requests.exceptions.RequestException as e:
                print(f"Erro na request: {e}")

# Este método é responsável por realizar uma request ao serviço de "listagem de rdo's" da Katardo API.
# Este método retorna um dict contendo a response da request e a quantidade de páginas do json de retorno.
def listar_funcionarios_rdo(token):
        try:
            token = "JWT " + token
            url = f"{BASE_URL}/DailyReportWorker/?company={COMPANY}&reportings={REPORTINGS}"
            
            headers = {
                'Authorization': token
            }
            response = requests.get(url, headers=headers) 
            
            if response.status_code == 200:
                total_paginas = lista_qtde_paginas(response.json())
                return {'response': response.json(), 'total_paginas': total_paginas}
            elif response.status_code == 403:
                 print(f"Código {response.status_code}: este usuário não tem permissão para executar essa ação.")
            else:
                response.raise_for_status()
                
        except requests.exceptions.RequestException as e:
                print(f"Erro na request: {e}")

# Este método é responsável por realizar uma request ao serviço de "listagem de programacoes" da Katardo API.
# Este método retorna um dict contendo a response da request e a quantidade de páginas do json de retorno.
def listar_programacoes(token):
        try:
            token = "JWT " + token
            url = f"{BASE_URL}/Reporting/?company={COMPANY}"
            
            headers = {
                'Authorization': token
            }
            response = requests.get(url, headers=headers) 
            
            if response.status_code == 200:
                total_paginas = lista_qtde_paginas(response.json())
                return {'response': response.json(), 'total_paginas': total_paginas}
            elif response.status_code == 403:
                 print(f"Código {response.status_code}: este usuário não tem permissão para executar essa ação.")
            else:
                response.raise_for_status()
            
        except requests.exceptions.RequestException as e:
                print(f"Erro na request: {e}")

# Este método é responsável por realizar uma request ao serviço de "listagem de rdo's" da Katardo API.
# Este método retorna um dict contendo a response da request e a quantidade de páginas do json de retorno.
def listar_rdo(token):
        try:
            token = "JWT " + token
            url = f"{BASE_URL}/MultipleDailyReport/?company={COMPANY}&reportings={REPORTINGS}"
            
            headers = {
                'Authorization': token
            }
            response = requests.get(url, headers=headers) 
            
            if response.status_code == 200:
                total_paginas = lista_qtde_paginas(response.json())
                return {'response': response.json(), 'total_paginas': total_paginas}
            elif response.status_code == 403:
                 print(f"Código {response.status_code}: este usuário não tem permissão para executar essa ação.")
            else:
                response.raise_for_status()
            
        except requests.exceptions.RequestException as e:
                print(f"Erro na request: {e}")

# Este método é responsável por realizar uma request ao serviço de "listagem de unidades" da Katardo API.
# Este método retorna um dict contendo a response da request e a quantidade de páginas do json de retorno.
def listar_unidades(token):
        try:
            token = "JWT " + token
            url = f"{BASE_URL}/OccurrenceType/?company={COMPANY}"
            
            headers = {
                'Authorization': token
            }
            response = requests.get(url, headers=headers) 

            if response.status_code == 200:
                total_paginas = lista_qtde_paginas(response.json())
                return {'response': response.json(), 'total_paginas': total_paginas}
            elif response.status_code == 403:
                 print(f"Código {response.status_code}: este usuário não tem permissão para executar essa ação.")
            else:
                response.raise_for_status()
            
        except requests.exceptions.RequestException as e:
                print(f"Erro na request: {e}")

# Este método é responsável por realizar uma request ao serviço de "listagem de veículos rdo" da Katardo API.
# Este método retorna um dict contendo a response da request e a quantidade de páginas do json de retorno.
def listar_veiculos_rdo(COMPANY, REPORTINGS, token):
        try:
            token = "JWT " + token
            url = f"{BASE_URL}/DailyReportVehicle/?company={COMPANY}&reportings={REPORTINGS}"
            
            headers = {
                'Authorization': token
            }
            response = requests.get(url, headers=headers) 
            
            if response.status_code == 200:
                total_paginas = lista_qtde_paginas(response.json())
                return {'response': response.json(), 'total_paginas': total_paginas}
            elif response.status_code == 403:
                 print(f"Código {response.status_code}: este usuário não tem permissão para executar essa ação.")
            else:
                response.raise_for_status()
            
        except requests.exceptions.RequestException as e:
                print(f"Erro na request: {e}")

# Este método retorna a quantidade de páginas de acordo com a response informada.
def lista_qtde_paginas(response):
    paginas = response['meta']['pagination']['pages']
    return paginas
    

    
