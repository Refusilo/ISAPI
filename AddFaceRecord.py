import requests
import json
import os

def addFaceRecord(host, auth, img, json_data):
    url = f'{host}/ISAPI/Intelligent/FDLib/FaceDataRecord?format=json'
    print (img)
    with open(img, 'rb') as image_file:
        image_data = image_file.read()

    nombre_img = os.path.basename(img)
    files = {
        'FaceDataRecord': (None, json.dumps(json_data), 'application/json'),
        'FaceImage': (nombre_img, image_data, 'image/png')
    }

    response = requests.post(url, auth=auth, files=files)

    with open(r'c:\tmp\salida.txt') as archivos:
        if response.status_code == 200:
            archivos.write('OK')
        else:
            archivos.write(
                f'{response.status_code} {response.subStatusCode} - Error al Procesar')
