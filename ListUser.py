
import requests
import json
from types import SimpleNamespace
from readData_Ora import readData

def ListUser(url, auth, json_data):
    #ora = readData('192.168.0.218', 'balcanes','brobol1957','1521','orcl',r'\\192.168.0.218\d\sistemas\excel\ora')
    ora = readData('localhost', 'balcanes','pen','1521','orcl',r'F:\Python\ISAPI_ReadEvents\ora')
    path = f'{url}/ISAPI/AccessControl/UserInfo/Search?format=json'
    archivo_salida = open (r'c:\tmp\salida.txt', 'w', encoding='utf-8')
    response = requests.post(path, auth=auth, json=json_data)    
    if response.status_code == 200:
        json_response = response.json()
        total_informado = json_response["UserInfoSearch"]["totalMatches"]
        print (f'Total de Registro Informado {total_informado}')        
        with open('sa_li_entrada.json', 'w') as archivo:
            archivo.write(str(json.dumps(json_response, indent=4)))
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