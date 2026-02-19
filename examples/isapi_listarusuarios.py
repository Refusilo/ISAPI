
import requests
from requests.auth import HTTPDigestAuth

# Definir la URL del endpoint
url = 'http://192.168.68.201/ISAPI/AccessControl/UserInfo/Search?format=json'

# Definir las credenciales de autenticación
usuario = 'admin'
clave = 'Admin2023$'

# Definir el cuerpo de mensaje JSON a enviar
cuerpo_mensaje = {
    "UserInfoSearchCond":
    {
        "searchID":"0",
        "searchResultPosition":10,
        "maxResults":500
    }
}

# Realizar la solicitud POST con autenticación de tipo Digest y el cuerpo de mensaje JSON
response = requests.post(url, auth=HTTPDigestAuth(usuario, clave), json=cuerpo_mensaje)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener los datos JSON de la respuesta
    json_data = response.json()
    # Procesar los datos JSON según sea necesario
    #print(json_data)
    
    for info in json_data["UserInfoSearch"]["UserInfo"]:   
        print(f"{info['employeeNo']}\t{info['name']}\t{info['userType']}\t{info['Valid']['beginTime']}\t{info['Valid']['endTime']}")
    # print("cantidad de empleados:",len(json_data["UserInfoSearch"]["UserInfo"]))
else:
    # Si la solicitud no fue exitosa, imprimir el código de estado
    print('Error:', response.status_code)






    