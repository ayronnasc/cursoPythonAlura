import requests


url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url) # get -> verbo http , para solicitar um recurso
print(response) # quando se tem um response [200] -> significa que a solicitação foi atendida com sucesso

if response.status_code == 200: 
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json: 
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante: 
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description'] 
        })

else: 
    print(f'o erro foi {response.status_code}')

print(dados_restaurante['McDonalds'])