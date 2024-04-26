import requests
import json

def DeleteUser(url, auth, ifile):
    path = f'{url}/ISAPI/AccessControl/UserInfo/Delete?format=json'
    
    with open(ifile, 'r') as archivo:
        json_data = json.load(archivo)
    response = requests.put(path, auth=auth, json=json_data)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener los datos JSON de la respuesta
        json_data = response.json()
        # Procesar los datos JSON según sea necesario
        print(json_data)
        # for info in json_data["UserInfoSearch"]["UserInfo"]:
            
        #     print(f"{info['employeeNo']}\t{info['name']}\t{info['userType']}\t{info['Valid']['beginTime']}\t{info['Valid']['endTime']}")
        # print("cantidad de empleados:",len(json_data["UserInfoSearch"]["UserInfo"]))
    else:
        # Si la solicitud no fue exitosa, imprimir el código de estado
        print('Error:', response.status_code)