import requests

def CreateUser(url, auth, json_data):
    path = f'{url}/ISAPI/AccessControl/UserInfo/Record?format=json'

    response = requests.post(path, auth=auth, json=json_data)

    with open(r'c:\tmp\salida.txt', 'w') as archivo:
        if response.status_code == 200:
            archivo.write('OK')
        else:
            json_data = response.json()
            print(f'DATA: {json_data}')
            archivo.write(f'{json_data["subStatusCode"]}')
            
