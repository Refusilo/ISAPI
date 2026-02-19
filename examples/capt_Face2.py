import cv2

def capture_face():
    # Crea un objeto VideoCapture asociado a la cámara web
    cap = cv2.VideoCapture(0)  # El argumento 0 indica la primera cámara disponible

    if not cap.isOpened():
        print("No se pudo abrir la cámara")
        return

    # Cargar el clasificador de detección de rostros
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Cargar el clasificador de detección de ojos
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    
    while True:
        # Lee un cuadro de la cámara
        ret, frame = cap.read()
        cv2.putText(frame, "PRESIONE ENTER PARA CAPTURAR", (1, 1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        if ret:
            # Convierte la imagen a escala de grises para la detección de rostros
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detecta rostros en la imagen
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]

                # Detecta ojos en la región de interés de la cara
                eyes = eye_cascade.detectMultiScale(roi_gray)

                # Dibuja un rectángulo alrededor de cada ojo detectado
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

                # Si se detectan dos ojos, calcula el ángulo entre ellos
                if len(eyes) == 2:
                    eye1_x, eye1_y, eye1_w, eye1_h = eyes[0]
                    eye2_x, eye2_y, eye2_w, eye2_h = eyes[1]

                    eye1_center = (eye1_x + eye1_w // 2, eye1_y + eye1_h // 2)
                    eye2_center = (eye2_x + eye2_w // 2, eye2_y + eye2_h // 2)

                    # Calcula la pendiente (dy/dx) de la línea entre los dos ojos
                    dx = eye2_center[0] - eye1_center[0]
                    dy = eye2_center[1] - eye1_center[1]

                    if dx != 0:
                        angle = abs(dy / dx)
                    else:
                        angle = 90  # Si dx es 0, asumimos un ángulo de 90 grados

                    if angle < 0.1:  # Ajusta este umbral según sea necesario
                        # Si el ángulo es pequeño, asumimos que la cara está mirando a la cámara
                        cv2.putText(frame, "Mirando a la cámara", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            cv2.imshow('Detección de rostros', frame)

            key = cv2.waitKey(1)
            if key == 13:  # 13 es el código de la tecla Enter en OpenCV
                break
            elif key == 27:  # 27 es el código de la tecla Esc en OpenCV
                print("Captura cancelada")
                break
        else:
            print("No se pudo capturar la imagen")
            break

    cap.release()
    cv2.destroyAllWindows()

capture_face()
