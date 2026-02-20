import requests
import json
import os

def ListUser(url, auth, json_data, ofile):
    path = f'{url}/ISAPI/AccessControl/UserInfo/Search?format=json'
    try:
        with open(ofile, 'w', encoding='utf-8') as archivo_salida:
            response = requests.post(path, auth=auth, json=json_data)
            response.raise_for_status()
            json_response = response.json()
            total_informado = json_response["UserInfoSearch"]["totalMatches"]
            print(f'Total de Registro Informado {total_informado}')
            
            with open(os.path.join('c:', 'tmp', 'listuser.json'), 'w') as archivo:
                archivo.write(json.dumps(json_response, indent=4))
            
            pos = 0
            while True:
                for info in json_response["UserInfoSearch"]["UserInfo"]:
                    linea_proc = f"{info['employeeNo']}\t{info['name']}\t{info['userType']}\t{info['Valid']['beginTime']}\t{info['Valid']['endTime']}"
                    print(linea_proc)
                    archivo_salida.write(linea_proc + '\n')
                
                if json_response["UserInfoSearch"]["responseStatusStrg"] == 'OK':
                    break
                
                pos += 30
                json_data["UserInfoSearchCond"]["searchResultPosition"] = pos
                response = requests.post(path, auth=auth, json=json_data)
                response.raise_for_status()
                json_response = response.json()
    except requests.exceptions.RequestException as e:
        print(f'Error en la solicitud: {e}')
    except json.JSONDecodeError as e:
        print(f'Error al procesar JSON: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')
