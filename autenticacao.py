import requests

# Configurações
client_id = '522ccf28819650679413c9b53f753cca616966bf'
client_secret = '27c666004df6b63d17c70df771695994d20a551a96a217c0a128734d6314'
refresh_token = '9480f7e4b081bb0450c8ea755e5fae91e8e4d3fe'

# Endpoint para obter novo access token
url = 'https://api.bling.com.br/Api/v3/token'

# Dados para a requisição
data = {
    'grant_type': 'refresh_token',
    'client_id': client_id,
    'client_secret': client_secret,
    'refresh_token': refresh_token
}

# Realiza a requisição
response = requests.post(url, data=data)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    tokens = response.json()
    new_access_token = tokens['access_token']
    new_refresh_token = tokens.get('refresh_token')  # Pode ou não ser retornado
    print('Novo Access Token:', new_access_token)
    print('Novo Refresh Token:', new_refresh_token)
else:
    print('Erro ao obter novo access token:', response.json())