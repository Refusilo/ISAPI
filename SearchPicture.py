import requests
import json
from datetime import datetime
import pytz
from requests.auth import HTTPDigestAuth

def SearchPicture(url, user, passwd, ifile):
    def json_entrada_leer(pos=0):
        return {
            "searchResultPosition": pos,
            "maxResults": 30,
            "faceLibType": "blackFD",
            "FDID": "1"
        }

    path = f'{url}/ISAPI/Intelligent/FDLib/FDSearch?format=json'
    pos = 0
    total_registros = None

    try:
        with open(ifile, 'w', encoding='utf-8') as archivos:
            while True:
                json_entrada = json_entrada_leer(pos)
                response = requests.post(path, auth=HTTPDigestAuth(user, passwd), json=json_entrada)
                response.raise_for_status()

                json_data = response.json()
                if total_registros is None:
                    total_registros = json_data["totalMatches"]
                
                print(f'Num of Matched: {json_data["numOfMatches"]} - {json_data["totalMatches"]} - {json_data["responseStatusStrg"]}')
                if int(json_data["numOfMatches"]) > 0:
                    for info in json_data["MatchList"]:
                        linea_proc = f"Id={info['FPID']}\tfaceURL={info['faceURL']}"
                        print(linea_proc)
                        archivos.write(linea_proc + '\n')
                    pos += json_data["numOfMatches"]
                else:
                    break

                if total_registros <= pos:
                    break
    except requests.exceptions.RequestException as e:
        print(f'Error en la solicitud: {e}')
    except json.JSONDecodeError as e:
        print(f'Error al procesar JSON: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')
    finally:
        print(f'Cantidad de Registros Visualizado: {total_registros}')
