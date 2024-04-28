import requests
import json
from requests.auth import HTTPDigestAuth
from types import SimpleNamespace
import argparse

from AddFaceRecord import addFaceRecord
from DeleteFaceRecord import DeleteFaceRecord
from CreateUser import CreateUser
from DeleteUser import DeleteUser
from ListUser import ListUser
from ReadEvents import ReadEvents

def readJson(json_file):
        with open(json_file, 'r') as archivo:
            json_data = json.load(archivo)
        return json_data

def main():
    parser = argparse.ArgumentParser(description="Sistema de Lectura Relojes HIKVision")
    parser.add_argument("--order", help="Orden a Ejecutar")
    parser.add_argument("--host", help="Servidor Destino")
    parser.add_argument("--user", help="Usuario")
    parser.add_argument("--passwd", help="Clave")
    parser.add_argument("--json_file", help="JSON de Entrada")
    parser.add_argument("--file", help="Archivo Varios")
    args = parser.parse_args()
    
    return args.order, args.host, args.user, args.passwd, args.json_file, args.file

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
        resultado = addFaceRecord(self.__url, auth, self.__ifile, self.__json_data)
        print (resultado)

    def DeleteFaceRecord(self):
        auth = self.generar_auth()
        DeleteFaceRecord(self.__url, auth, self.__json_data)
    
    def ReadEvents(self):
        #auth = self.generar_auth()
        ReadEvents(self.__url, self.__user, self.__password, self.__json_data)

if __name__ == '__main__':
    order, host, user, passwd, json_file, file = main()
    #host = 'http://192.168.68.200'
    #user = 'admin'
    #passwd = 'ano2023-26455604'
    json_data = readJson(json_file)
    hv = hikvision(user, passwd, host, file, json_data)
    opt = str(order).upper
    print (f'Parametros {order}')
    if order == 'listuser':
        hv.listUser()
    if order == 'createuser':
        hv.CreateUser()
    if order == 'addfacerecord':
        hv.addFaceRecord()
    if order == 'readevents':
        hv.ReadEvents()
        
        #comentario