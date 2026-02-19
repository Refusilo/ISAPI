import cv2

def capture_face():
    # Crea un objeto VideoCapture asociado a la cámara web
    cap = cv2.VideoCapture(0)  # El argumento 0 indica la primera cámara disponible

    if not cap.isOpened():
        print("No se pudo abrir la cámara")
        return

    # Cargar el clasificador de detección de rostros
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    while True:
        # Lee un cuadro de la cámara
        ret, frame = cap.read()
        cv2.putText(frame, "PRESIONE ENTER PARA CAPTURAR O ESC PARA SALIR", (2, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        if ret:
            # Convierte la imagen a escala de grises para la detección de rostros
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detecta rostros en la imagen
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Hace una copia del cuadro original para guardar sin rectángulos
            frame_copy = frame.copy()

            # Dibuja un rectángulo alrededor de cada rostro detectado
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

            # Muestra la imagen de la cámara en una ventana
            cv2.imshow('Detección de rostros', frame)

            # Espera a que se presione una tecla
            key = cv2.waitKey(1)
            if key == 13:  # 13 es el código de la tecla Enter en OpenCV
                if len(faces) > 0:
                    # Si se detecta al menos un rostro, guarda la imagen capturada sin el rectángulo
                    cv2.imwrite('captura_con_rostro.jpg', frame_copy)
                    print("Imagen capturada con rostro")
                else:
                    print("No se detectó ningún rostro")
                break
            elif key == 27:  # 27 es el código de la tecla Esc en OpenCV
                print("Captura cancelada")
                break
        else:
            print("No se pudo capturar la imagen")
            break

    # Libera el objeto VideoCapture y cierra la ventana
    cap.release()
    cv2.destroyAllWindows()

# Llama a la función para capturar una imagen con detección de rostros
capture_face()
