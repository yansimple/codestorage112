import requests
import json

response = requests.get('https://blockchain.info/rawaddr/3QJdB9gcQMnoADtosaABLP7jXHkXokLJqf')
#print(response.read())
print(type(response))

chain = json.loads(str(response))

print(chain)
print()