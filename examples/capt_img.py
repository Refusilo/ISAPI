import cv2
import pyautogui

def capture_image():
    # Crea un objeto VideoCapture asociado a la cámara web
    cap = cv2.VideoCapture(0)  # El argumento 0 indica la primera cámara disponible

    if not cap.isOpened():
        print("No se pudo abrir la cámara")
        return

    while True:
        # Lee un cuadro de la cámara
        ret, frame = cap.read()

        if ret:
            # Muestra la imagen de la cámara en una ventana
            cv2.imshow('Cámara', frame)
            # Centra la ventana en el monitor
            cv2.moveWindow('Cámara', pyautogui.size()[0]//2 - frame.shape[1]//2, pyautogui.size()[1]//2 - frame.shape[0]//2)

            # Espera a que se presione una tecla
            key = cv2.waitKey(1)
            if key == 13:  # 13 es el código de la tecla Enter en OpenCV
                # Guarda la imagen capturada en un archivo
                cv2.imwrite('captura.jpg', frame)
                print("Imagen capturada con éxito")
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

# Llama a la función para capturar una imagen
capture_image()
