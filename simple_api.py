import requests

# URL da API do Pokémon
api_url = 'https://pokeapi.co/api/v2/pokemon'

# Realizando a requisição GET à API
response = requests.get(api_url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Convertendo a resposta para JSON
    data = response.json()
    # Exibindo os primeiros resultados
    for pokemon in data['results'][:5]:
        print(f"Nome: {pokemon['name'].capitalize()}")
        print(f"URL: {pokemon['url']}\n")
else:
    print(f"Falha ao acessar a API. Status code: {response.status_code}")
