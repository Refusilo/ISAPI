import requests

from .project_paths import OUTPUT_DIR

def CreateUser(url, auth, json_data):
    path = f'{url}/ISAPI/AccessControl/UserInfo/Record?format=json'

    response = requests.post(path, auth=auth, json=json_data)

    output_file = OUTPUT_DIR / 'create_user.txt'
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open('w', encoding='utf-8') as archivo:
        if response.status_code == 200:
            archivo.write('OK')
        else:
            json_data = response.json()
            print(f'DATA: {json_data}')
            archivo.write(f'{json_data["subStatusCode"]}')
            
