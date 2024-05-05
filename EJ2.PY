import os
from PIL import Image

def jpg2bmp(path):
    try:
        if not os.path.isdir(path):
            print("La ruta especificada no es una carpeta.")
            return
        file_path = os.listdir(path)
        for img in file_path:
            img_path = os.path.join(path, img)
            if os.path.isfile(img_path) and img.lower().endswith('.jpg'):
                imagen = Image.open(img_path)
                ruta_bmp = os.path.splitext(img_path)[0] + ".bmp"
                imagen.save(ruta_bmp, 'BMP')
                print(f"Imagen {img} convertida exitosamente a BMP.")
    except Exception as e:
        print("Error:", str(e))

# Ejemplo de uso
file_path = r"F:\Clientes\florida\tarjado\fotos"
jpg2bmp(file_path)
