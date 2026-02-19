import argparse
import json
from pathlib import Path

from requests.auth import HTTPDigestAuth

from src.AddFaceRecord import addFaceRecord
from src.CreateUser import CreateUser
from src.DeleteFaceRecord import DeleteFaceRecord
from src.DeleteUser import DeleteUser
from src.GetPicture import GetPicture
from src.ListUser import ListUser
from src.ReadEvents import ReadEvents
from src.project_paths import IMAGES_DIR, INPUT_DIR


def resolve_path(path_value, base_dir):
    if not path_value:
        return None
    candidate = Path(path_value).expanduser()
    if candidate.is_file():
        return candidate
    fallback = base_dir / path_value
    if fallback.is_file():
        return fallback
    return candidate


def read_json(json_file):
    if not json_file:
        raise ValueError("Debe indicar --json_file")
    path = resolve_path(json_file, INPUT_DIR)
    if not path or not path.exists():
        raise FileNotFoundError(f'No se encontró el archivo JSON: {json_file}')
    with path.open('r', encoding='utf-8') as archivo:
        return json.load(archivo)


def main():
    parser = argparse.ArgumentParser(description="Sistema de Lectura Relojes HIKVision")
    parser.add_argument("--order", required=True, help="Orden a ejecutar")
    parser.add_argument("--host", required=True, help="Servidor destino")
    parser.add_argument("--user", required=True, help="Usuario del equipo")
    parser.add_argument("--passwd", required=True, help="Clave del equipo")
    parser.add_argument("--json_file", required=False, help="Ruta del JSON de entrada")
    parser.add_argument("--file", required=False, help="Archivo auxiliar (ej: imagen)")
    args = parser.parse_args()
    return args

class hikvision():
    def __init__(self, user, password, url, ifile, json) -> None:
        self.__user = user #usuario de hikvision
        self.__password = password #clave de hikvision
        self.__url = url #url del servidor "http://xxx.xxx.xxx.xxx"
        self.__ifile = ifile #Archivo del json de entrada
        self.__json_data = json

    def generar_auth (self):
        auth = HTTPDigestAuth(self.__user, self.__password)
        return auth

    def listUser (self):
        auth = self.generar_auth()
        ListUser(self.__url, auth, self.__json_data)
        
    def CreateUser(self):
        auth = self.generar_auth()
        CreateUser(self.__url, auth, self.__json_data)
    
    def addFaceRecord(self):
        auth = self.generar_auth()
        if not self.__ifile:
            raise ValueError("Debe indicar --file con la imagen a enviar.")
        resultado = addFaceRecord(self.__url, auth, self.__ifile, self.__json_data)
        print (resultado)

    def DeleteFaceRecord(self):
        auth = self.generar_auth()
        DeleteFaceRecord(self.__url, auth, self.__json_data)
    
    def ReadEvents(self):
        #auth = self.generar_auth()
        ReadEvents(self.__url, self.__user, self.__password, self.__json_data)
    
    def DeleteUser(self):
        #auth = self.generar_auth()
        DeleteUser(self.__url, self.__user, self.__password, self.__json_data)
        
    def GetPicture(self):
        if not self.__ifile:
            raise ValueError("Debe indicar --file con la ruta destino de la imagen.")
        GetPicture(self.__url, self.__user, self.__password, self.__ifile)

if __name__ == '__main__':
    args = main()
    json_data = read_json(args.json_file) if args.json_file else {}
    file_path = resolve_path(args.file, IMAGES_DIR) if args.file else args.file
    if args.file and (file_path is None or not Path(file_path).exists()):
        raise FileNotFoundError(f'No se encontró el archivo auxiliar: {args.file}')

    hv = hikvision(args.user, args.passwd, args.host, str(file_path) if file_path else None, json_data)
    order = (args.order or '').lower()
    print (f'Parametros {args.order}')
    if order == 'listuser':
        hv.listUser()
    if order == 'createuser':
        hv.CreateUser()
    if order == 'addfacerecord':
        hv.addFaceRecord()
    if order == 'readevents':
        hv.ReadEvents()
    if order == 'deleteuser':
        hv.DeleteUser()
