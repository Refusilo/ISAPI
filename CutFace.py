import cv2

def CutFace(imagen_path, margen=0.2):
    # Cargar la imagen
    imagen = cv2.imread(imagen_path)

    # Crear un detector de rostros
    detector_rostros = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convertir la imagen a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Detectar rostros en la imagen
    rostros = detector_rostros.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Si se detecta al menos un rostro
    if len(rostros) > 0:
        # Tomar solo el primer rostro detectado
        (x, y, w, h) = rostros[0]

        # Calcular el margen alrededor del rostro
        margen_x = int(w * margen)
        margen_y = int(h * margen)

        # Calcular las coordenadas de la esquina superior izquierda del recuadro
        x_recorte = max(0, x - margen_x)
        y_recorte = max(0, y - margen_y)

        # Calcular las coordenadas de la esquina inferior derecha del recuadro
        x_fin = min(imagen.shape[1], x + w + margen_x)
        y_fin = min(imagen.shape[0], y + h + margen_y)

        # Recortar la imagen con margen
        rostro_recortado = imagen[y_recorte:y_fin, x_recorte:x_fin]

        # Guardar el rostro recortado en el archivo original
        cv2.imwrite(imagen_path, rostro_recortado)
