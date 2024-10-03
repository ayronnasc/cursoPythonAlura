from fastapi import FastAPI, Query
import requests

app = FastAPI()

#criação de rotas () 
@app.get('/api/hello')  #Decorator, quando isso for requisitado [api/hello] dentro da aplicação, será executada a função hello_world()
def hello_world():
    '''
    Endpoint que exibe uma mensagem legal do mundo da programação! 
    '''
    return {'Hello':'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios dos restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url) # get -> verbo http , para solicitar um recurso
    print(response) # quando se tem um response [200] -> significa que a solicitação foi atendida com sucesso

    if response.status_code == 200: 
        dados_json = response.json()
        if restaurante is None: # nenhuma informação de restaurante foi passada
            return {'Dados':dados_json}
 
        dados_restaurante = []
        for item in dados_json: 
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description'] 
                })
        return {'Restaurante':restaurante, 'Cardápio':dados_restaurante}

    else: 
        return {'Erro':f'{response.status_code} - {response.text}'}