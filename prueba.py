from ursina import *
from PIL import Image
import cv2
import numpy as np

# Función para abrir la cámara
def abrir_camara():
    cap = cv2.VideoCapture(0)  # Cambia a 1 si no funciona
    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara.")
        exit()
    return cap

# Inicializa la aplicación Ursina
app = Ursina()

# Captura de video de la cámara
cap = abrir_camara()

# Definir un bloque para mostrar el feed de la cámara
captured_image_block = Entity(model='quad', scale=(5, 3), position=(0, 0, 5), texture=None)

def update():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convertir de BGR a RGB
        frame = np.flip(frame, axis=1)  # Voltear la imagen para simular un espejo
        image = Image.fromarray(frame)
        captured_image_block.texture = Texture(image)

    # Movimiento de la cámara
    if held_keys['w']:
        camera.position.z -= 0.1
    if held_keys['s']:
        camera.position.z += 0.1
    if held_keys['a']:
        camera.position.x -= 0.1
    if held_keys['d']:
        camera.position.x += 0.1

def input(key):
    if key == 'escape':
        cap.release()
        app.userExit()
    elif key == 't':
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.flip(frame, axis=1)
            filename = 'captured_photo.png'
            Image.fromarray(frame).save(filename)  # Guardar la imagen en formato compatible
            captured_image_block.texture = filename  # Mostrar la imagen capturada

# Ejecuta la aplicación
app.run()

# Libera la captura de video
cap.release()
