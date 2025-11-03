import requests

def fetch_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data['value'])
    else:
        print("failed fetching")
    
fetch_joke()