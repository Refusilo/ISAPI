from pathlib import Path

import requests
from requests.auth import HTTPDigestAuth

from .project_paths import CERTS_DIR

def GetPicture(url, usuario, clave, ruta_destino):
    try:
        CERTS_DIR.mkdir(parents=True, exist_ok=True)
        cert_path = CERTS_DIR / 'hikvision_server.pem'
        # Descargar el certificado del servidor
        response = requests.get(url, auth=HTTPDigestAuth(usuario, clave))
        with cert_path.open("wb") as cert_file:
            cert_file.write(response.content)
        
        # Utilizar el certificado descargado para realizar la solicitud
        response = requests.get(url, auth=HTTPDigestAuth(usuario, clave), verify=str(cert_path))
        
        # Resto del código para guardar la imagen...

        # Verificar si la descarga fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Guardar la imagen en el archivo especificado
            destination = Path(ruta_destino)
            destination.parent.mkdir(parents=True, exist_ok=True)
            with destination.open('wb') as file:
                file.write(response.content)
            print("Imagen descargada exitosamente.")
        else:
            print("Error al descargar la imagen. Código de estado:", response.status_code)
    except Exception as e:
        print("Error:", str(e))
