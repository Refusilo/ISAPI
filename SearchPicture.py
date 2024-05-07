import requests
import json
from datetime import datetime
import pytz
from requests.auth import HTTPDigestAuth

def SearchPicture(url, user, passwd, json_data):
    def json_entrada_leer(pos=0):
        json_data = {
            "searchResultPosition":pos,
            "maxResults":30,
            "faceLibType":"blackFD",
            "FDID":"1"
        }
        return json_data    
    path = f'{url}/ISAPI/Intelligent/FDLib/FDSearch?format=json'
    pos = 0
    total_registros = None    
    with open(r'salida.txt', 'w', encoding='utf-8') as archivos:    
        while True:
            json_entrada = json_entrada_leer(pos)            
            response = requests.post(path, auth=HTTPDigestAuth(user, passwd), json=json_entrada)
            if response.status_code == 200:
                json_data = response.json()
                #print (json_data)
                if total_registros == None:
                    total_registros = json_data["totalMatches"]
                print (f'Num of Matched: {json_data["numOfMatches"]} - {json_data["totalMatches"]} - {json_data["responseStatusStrg"]}')
                if int(json_data["numOfMatches"]) > 0:
                    try:
                        for info in json_data["MatchList"]:
                            linea_proc = f"Id={info['FPID']}\tfaceURL={info['faceURL']}"                            
                            archivos.write (linea_proc + '\n')
                        pos = pos + json_data["numOfMatches"]
                    except Exception as e:
                        print(f'Error General!!: {e}')
                        break
                else:
                    break
                if total_registros <= pos:
                    break
            else:
                # Si la solicitud no fue exitosa, imprimir el códigitgo de estado
                print(f'Error: {response.status_code}')
                print ( response.json() )
                break
    archivos.close()
    print(f'Cantidad de Registros Visualizado: {total_registros}')
