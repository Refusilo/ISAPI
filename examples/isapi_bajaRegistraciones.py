import requests
from requests.auth import HTTPDigestAuth

# Definir la URL del endpoint
url = 'http://192.168.68.200/ISAPI/AccessControl/AcsEvent?format=json'

# Definir las credenciales de autenticación
usuario = 'admin'
clave = 'ano2023-26455604'

# Definir el cuerpo de mensaje JSON a enviar
cuerpo_mensaje = {
    "AcsEventCond": {
        "searchID": "0",
        "searchResultPosition": 0,
        "maxResults": 30,
        "major": 5,
        "minor": 75,
        "startTime": "2024-04-17T01:00:00-07:00",
        "endTime": "2024-04-18T23:59:59-07:00"
    }
}

# Realizar la solicitud POST con autenticación de tipo Digest y el cuerpo de mensaje JSON
response = requests.post(url, auth=HTTPDigestAuth(usuario, clave), json=cuerpo_mensaje)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener los datos JSON de la respuesta
    json_data = response.json()
    # Procesar los datos JSON según sea necesario
    for info in json_data["AcsEvent"]["InfoList"]:
        print(f"{info['time']}\t{info['name']}\t{info['employeeNoString']}\t{info['currentVerifyMode']}")
else:
    # Si la solicitud no fue exitosa, imprimir el código de estado
    print('Error:', response.status_code)