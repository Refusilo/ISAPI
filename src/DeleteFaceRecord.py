import requests
from types import SimpleNamespace
import json

def DeleteFaceRecord(url, auth, json_data):
    #faceLibType, FDID, FPIDList):
    path = f'{url}/ISAPI/Intelligent/FDLib/FDSetUp?format=json'
    '''fpidlist = []
    for fpid in FPIDList:
        fpidlist.append({
            'value': fpid
        })
    body = {
        'FPID': fpidlist
        }
    '''        
    response = requests.put(path, auth=auth, data=json.dumps(json_data))
    json_data = response.json()
    print ( json_data )
    
    with open(r'c:\tmp\salida.txt', 'w') as archivo:
        if response.status_code == 200:
            archivo.write('OK')
        else:
            json_data = response.json()
            print(f'DATA: {json_data}')
            archivo.write(f'{json_data["subStatusCode"]}')