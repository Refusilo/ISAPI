import requests
from requests.auth import HTTPDigestAuth
import base64

class HikvisionAPI:
    def __init__(self, ip, username, password):
        self.base_url = f'http://{ip}/ISAPI'
        self.auth = HTTPDigestAuth(username, password)

    def get_device_info(self):
        url = f'{self.base_url}/System/deviceInfo'
        response = requests.get(url, auth=self.auth)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error: {response.status_code} - {response.text}')

    def get_user_list(self, start_position=0, max_results=30):
        url = f'{self.base_url}/AccessControl/UserInfo/Search?format=json'
        json_data = {
            "searchResultPosition": start_position,
            "maxResults": max_results
        }
        response = requests.post(url, auth=self.auth, json=json_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error: {response.status_code} - {response.text}')

    def add_user(self, user_id, name, card_no, user_type="normal"):
        url = f'{self.base_url}/AccessControl/UserInfo/Record?format=json'
        json_data = {
            "UserInfo": {
                "employeeNo": user_id,
                "name": name,
                "userType": user_type,
                "Valid": {
                    "beginTime": "2020-01-01T00:00:00",
                    "endTime": "2030-12-31T23:59:59"
                },
                "RightPlan": [{
                    "doorNo": 1,
                    "planTemplateNo": 1
                }],
                "CardList": [{
                    "cardNo": card_no,
                    "cardType": "normalCard"
                }]
            }
        }
        response = requests.post(url, auth=self.auth, json=json_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error: {response.status_code} - {response.text}')

    def delete_user(self, user_id):
        url = f'{self.base_url}/AccessControl/UserInfo/Delete?format=json'
        json_data = {
            "UserInfoDelCond": {
                "EmployeeNoList": [user_id]
            }
        }
        response = requests.put(url, auth=self.auth, json=json_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error: {response.status_code} - {response.text}')

    def get_user_fingerprint(self, user_id):
        url = f'{self.base_url}/AccessControl/Fingerprint/UserFPInfo/Search?format=json'
        json_data = {
            "searchResultPosition": 0,
            "maxResults": 10,
            "EmployeeNo": user_id
        }
        response = requests.post(url, auth=self.auth, json=json_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error: {response.status_code} - {response.text}')

    def capture_fingerprint(self, user_id, finger_index):
        url = f'{self.base_url}/AccessControl/Fingerprint/Capture'
        json_data = {
            "EmployeeNo": user_id,
            "FingerPrintNo": finger_index,
            "CaptureMode": "1"
        }
        response = requests.post(url, auth=self.auth, json=json_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error: {response.status_code} - {response.text}')

    def get_event_list(self, start_time, end_time, start_position=0, max_results=30):
        url = f'{self.base_url}/AccessControl/Event/Search?format=json'
        json_data = {
            "searchResultPosition": start_position,
            "maxResults": max_results,
            "condition": {
                "StartTime": start_time,
                "EndTime": end_time
            }
        }
        response = requests.post(url, auth=self.auth, json=json_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error: {response.status_code} - {response.text}')

    def set_device_parameters(self, parameters):
        url = f'{self.base_url}/System/DeviceConfig'
        response = requests.put(url, auth=self.auth, json=parameters)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error: {response.status_code} - {response.text}')

    def reboot_device(self):
        url = f'{self.base_url}/System/reboot'
        response = requests.put(url, auth=self.auth)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error: {response.status_code} - {response.text}')

    def get_device_status(self):
        url = f'{self.base_url}/System/status'
        response = requests.get(url, auth=self.auth)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error: {response.status_code} - {response.text}')

    # Métodos para reconocimiento facial
    def add_face(self, user_id, image_path):
        url = f'{self.base_url}/Intelligent/FDLib/FDSetUp'
        with open(image_path, 'rb') as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        json_data = {
            "faceLibType": "blackFD",
            "FDID": "1",
            "faceList": [{
                "FPID": user_id,
                "name": user_id,
                "faceURL": f"data:image/jpeg;base64,{base64_image}"  # Imagen en base64
            }]
        }
        response = requests.post(url, auth=self.auth, json=json_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error: {response.status_code} - {response.text}')

    def search_face(self, image_path):
        url = f'{self.base_url}/Intelligent/FDLib/FDSearch'
        with open(image_path, 'rb') as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        json_data = {
            "searchResultPosition": 0,
            "maxResults": 10,
            "faceLibType": "blackFD",
            "FDID": "1",
            "snap": {
                "faceURL": f"data:image/jpeg;base64,{base64_image}"  # Imagen en base64
            }
        }
        response = requests.post(url, auth=self.auth, json=json_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error: {response.status_code} - {response.text}')

# Ejemplo de uso
if __name__ == '__main__':
    ip = '192.168.1.201'
    username = 'admin'
    password = 'contraseña'

    hik_api = HikvisionAPI(ip, username, password)

    # Obtener información del dispositivo
    try:
        device_info = hik_api.get_device_info()
        print("Información del dispositivo:", device_info)
    except Exception as e:
        print(e)

    # Listar usuarios
    try:
        user_list = hik_api.get_user_list()
        print("Lista de usuarios:", user_list)
    except Exception as e:
        print(e)

    # Agregar usuario
    try:
        user_id = '12345'
        name = 'John Doe'
        card_no = '67890'
        new_user = hik_api.add_user(user_id, name, card_no)
        print("Nuevo usuario agregado:", new_user)
    except Exception as e:
        print(e)

    # Eliminar usuario
    try:
        delete_response = hik_api.delete_user(user_id)
        print("Usuario eliminado:", delete_response)
    except Exception as e:
        print(e)

    # Obtener huella digital de usuario
    try:
        fingerprint_info = hik_api.get_user_fingerprint(user_id)
        print("Información de huella digital:", fingerprint_info)
    except Exception as e:
        print(e)

    # Capturar huella digital
    try:
        capture_response = hik_api.capture_fingerprint(user_id, 1)
        print("Captura de huella digital:", capture_response)
    except Exception as e:
        print(e)

    # Obtener lista de eventos
    try:
        events = hik_api.get_event_list("2023-01-01T00:00:00Z", "2023-01-31T23:59:59Z")
        print("Lista de eventos:", events)
    except Exception as e:
        print(e)

    # Agregar rostro desde archivo local
    try:
        image_path = "path/to/face_image.jpg"
        add_face_response = hik_api.add_face(user_id, image_path)
        print("Rostro agregado:", add_face_response)
    except Exception as e:
        print(e)

    # Buscar rostro desde archivo local
    try:
        search_face_response = hik_api.search_face(image_path)
        print("Resultado de búsqueda de rostro:", search_face_response)
    except Exception as e:
        print(e)
