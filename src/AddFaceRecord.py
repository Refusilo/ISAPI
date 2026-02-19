import os
import json

import requests

from .project_paths import OUTPUT_DIR

def addFaceRecord(host, auth, img, json_data):
    url = f'{host}/ISAPI/Intelligent/FDLib/FaceDataRecord?format=json'
    with open(img, 'rb') as image_file:
        image_data = image_file.read()

    nombre_img = os.path.basename(img)
    files = {
        'FaceDataRecord': (None, json.dumps(json_data), 'application/json'),
        'FaceImage': (nombre_img, image_data, 'image/png')
    }

    response = requests.post(url, auth=auth, files=files)

    output_file = OUTPUT_DIR / 'add_face_record.txt'
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open('w', encoding='utf-8') as archivos:
        if response.status_code == 200:
            archivos.write('OK')
            return 'OK'

        error_detail = ''
        try:
            payload = response.json()
            # Hikvision responses usually include subStatusCode/responseStatusStrg keys
            error_detail = payload.get('subStatusCode') or payload.get('responseStatusStrg') or payload
        except ValueError:
            error_detail = response.text

        error_msg = f'{response.status_code} {error_detail} - Error al procesar'
        archivos.write(error_msg)
        return error_msg
