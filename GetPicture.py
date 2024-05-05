import requests
from requests.auth import HTTPDigestAuth

def GetPicture(url, usuario, clave, ruta_destino):
    try:
        # Descargar el certificado del servidor
        response = requests.get(url, auth=HTTPDigestAuth(usuario, clave))
        with open("certificado.pem", "wb") as cert_file:
            cert_file.write(response.content)
        
        # Utilizar el certificado descargado para realizar la solicitud
        response = requests.get(url, auth=HTTPDigestAuth(usuario, clave), verify="certificado.pem")
        
        # Resto del código para guardar la imagen...

        # Verificar si la descarga fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Guardar la imagen en el archivo especificado
            with open(ruta_destino, 'wb') as file:
                file.write(response.content)
            print("Imagen descargada exitosamente.")
        else:
            print("Error al descargar la imagen. Código de estado:", response.status_code)
    except Exception as e:
        print("Error:", str(e))
