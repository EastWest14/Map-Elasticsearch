import requests

def numberR():
	return 5

r = requests.get('http://localhost:9200/')
print(r.status_code)
