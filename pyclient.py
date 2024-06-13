import requests 

response = requests.post("http://127.0.0.1:8000/log-in", json={"username":"helllll", "password":"hellisthis"})
print(response.json())