import requests
from pprint import pprint

#{'key': '5006ea243c377b71496c0f8f1e1c98f3af22f827'}
def client():

    token = 'Token 5006ea243c377b71496c0f8f1e1c98f3af22f827'

    headers = {
        'Authorization': token,
    }
    response = requests.get(
        url='http://127.0.0.1:8000/api/UserProfiles/',
        headers = headers
    )

    print('Status Code: ',response.status_code)

    response_data=response.json()
    pprint(response_data)


if __name__ == '__main__':
    client()