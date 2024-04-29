from PIL import Image
import os

def reducir_a_200kb(imagen_path):
    # Cargar la imagen
    imagen = Image.open(imagen_path)
    
    # Calcular la calidad inicial basada en el tamaño original
    calidad = 95
    
    # Reducir la calidad iterativamente hasta que el tamaño de archivo sea menor o igual a 200 KB
    while True:
        # Guardar la imagen con la calidad actual
        imagen.save(imagen_path, optimize=True, quality=calidad)
        
        # Comprobar el tamaño del archivo
        tamano_archivo = os.path.getsize(imagen_path) / 1024  # Convertir bytes a kilobytes
        if tamano_archivo <= 200:
            break  # Si el tamaño es menor o igual a 200 KB, salimos del bucle
        
        # Si el tamaño es mayor a 200 KB, reducimos la calidad en un 5%
        calidad -= 5
        if calidad <= 5:
            break  # No podemos reducir más la calidad
        
    print(f"La imagen ha sido reducida a {tamano_archivo:.2f} KB")
