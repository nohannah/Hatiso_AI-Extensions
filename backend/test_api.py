import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "text": "You are stupid."
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())