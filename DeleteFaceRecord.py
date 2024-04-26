import requests
from types import SimpleNamespace
import json

def DeleteFaceRecord(url, auth, faceLibType, FDID, FPIDList):
    path = f'{url}/ISAPI/Intelligent/FDLib/FDSearch/Delete?format=json&FDID={FDID}&faceLibType={faceLibType}'
    fpidlist = []
    for fpid in FPIDList:
        fpidlist.append({
            'value': fpid
        })
    body = {
        'FPID': fpidlist
        }
            
    response = requests.put(path, auth=auth, data=json.dumps(body))

    return response.status_code