import json

import requests

from .project_paths import OUTPUT_DIR

def ListUser(url, auth, json_data):
    path = f'{url}/ISAPI/AccessControl/UserInfo/Search?format=json'
    log_file = OUTPUT_DIR / 'list_user.txt'
    json_output = OUTPUT_DIR / 'sa_li_entrada.json'
    log_file.parent.mkdir(parents=True, exist_ok=True)

    archivo_salida = log_file.open('w', encoding='utf-8')
    response = requests.post(path, auth=auth, json=json_data)    
    if response.status_code == 200:
        json_response = response.json()
        total_informado = json_response["UserInfoSearch"]["totalMatches"]
        print (f'Total de Registro Informado {total_informado}')        
        with json_output.open('w', encoding='utf-8') as archivo:
            archivo.write(json.dumps(json_response, indent=4))
        pos = 0
        while True:
            for info in json_response["UserInfoSearch"]["UserInfo"]:
                linea_proc = f"{info['employeeNo']}\t{info['name']}\t{info['userType']}\t{info['Valid']['beginTime']}\t{info['Valid']['endTime']}"
                print(linea_proc)
                archivo_salida.write( linea_proc + '\n')
            if json_response["UserInfoSearch"]["responseStatusStrg"] == 'OK':
                break
            pos = pos + 30
            json_data["UserInfoSearchCond"]["searchResultPosition"] = pos
            response = requests.post(path, auth=auth, json=json_data)    
            json_response = response.json()
    else:
        print('Error:', response.status_code)
    archivo_salida.close()
