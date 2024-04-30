import paramiko
import argparse
import shutil

def main():
    parser = argparse.ArgumentParser(description="Copiado de Archivos")
    parser.add_argument("--ifile", help="Archivo Origen")
    parser.add_argument("--ofile", help="Archivo Salida")
    parser.add_argument("--host", help="Servidor Destino")
    parser.add_argument("--port", help="Puerto")
    parser.add_argument("--user", help="Usuario")
    parser.add_argument("--pass", help="Clave")
    args = parser.parse_args()
    
    return args.ifile, args.ofile, args.host, args.user, args.passwd

def copiar_archivo(origen, destino):
    try:
        shutil.copyfile(origen, destino)
        print(f"Archivo copiado de '{origen}' a '{destino}'")
    except FileNotFoundError:
        print("Error: Archivo de origen no encontrado.")
    except PermissionError:
        print("Error: Permiso denegado para escribir en el destino.")

def subir_archivo_sftp(ruta_local, ruta_remota, servidor, puerto, usuario, clave):
    # Conexión al servidor SFTP
    cliente = paramiko.SSHClient()
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cliente.connect(servidor, port=puerto, username=usuario, password=clave)

    # SFTP
    sftp = cliente.open_sftp()

    # Subir archivo
    sftp.put(ruta_local, ruta_remota)

    # Cerrar conexión
    sftp.close()
    cliente.close()

if __name__ == "__main__":
    ifile, ofile, host, port, user, passwd = main()    
    subir_archivo_sftp(ifile, ofile, host, port, user, passwd)
    