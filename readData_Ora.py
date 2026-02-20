import cx_Oracle
from datetime import datetime


class readData():
    def __init__(self, ip, user, passwd, port, sid, libdir):
        self.__username = user
        self.__password = passwd
        self.__ip = ip
        self.__port = port
        self.__sid = sid
        self.__libdir = libdir

    def conn_oracle(self):
        cx_Oracle.init_oracle_client(
            lib_dir=self.__libdir)
        self.__dsn_tns = cx_Oracle.makedsn(
            self.__ip, self.__port, service_name=self.__sid)
        # Conecta a la base de datos
        self.__conexion = cx_Oracle.connect(
            self.__username, self.__password, self.__dsn_tns, encoding="utf8", nencoding="utf8")

    def conn_commit(self):
        self.__conexion.commit()

    def conn_close(self):
        self.__conexion.close()

    def readClock(self, usuario):
        __cursor = self.__conexion.cursor()
        __sql = "SELECT * FROM SUE_USUARIO_RELOJ"
        __cursor.execute(__sql)
        resultados = __cursor.fetchall()
        __cursor.close()
        return resultados

    def insertUser(self, pin, reloj, descrip, tipo):
        __cursor = self.__conexion.cursor()
        try:
            __cursor.callproc('PROC_CARGAR_USER', [
                pin, reloj, descrip, tipo])
        finally:
            __cursor.close()
