import requests
from requests.auth import HTTPDigestAuth

from .project_paths import OUTPUT_DIR

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
    output_file = OUTPUT_DIR / 'search_picture.txt'
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open('w', encoding='utf-8') as archivos:    
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
    print(f'Cantidad de Registros Visualizado: {total_registros}')
