from ursina import *
import cv2
import numpy as np
from PIL import Image
import os

app = Ursina()

# Inicializar la captura de video con OpenCV
cap = cv2.VideoCapture(0)

# Verificar si la cámara se abrió correctamente
if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

# Definir una textura inicial
ret, frame = cap.read()
if not ret:
    print("Error: No se pudo leer el frame de la cámara.")
    exit()

# Convertir de BGR a RGB y voltear la imagen
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
frame = np.flip(frame, axis=1)

# Crear una imagen PIL desde el frame
image = Image.fromarray(frame)
texture = Texture(image)

# Definir la entidad espejo
mirror = Entity(model='quad', scale=(2, 2), position=(0, 1, -3), texture=texture)

# Definir un bloque en Ursina para mostrar la imagen capturada
captured_image_block = Entity(model='quad', scale=(2, 2), position=(2.5, 1, -3), texture=None)

def update():
    global frame

    ret, frame = cap.read()
    if ret:
        # Convertir de BGR a RGB y voltear la imagen
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.flip(frame, axis=1)

        # Actualizar la textura del espejo
        image = Image.fromarray(frame)
        mirror.texture = Texture(image)

def input(key):
    if key == 'escape':
        cap.release()
        app.quit()

    elif key == 't':
        # Tomar una foto
        ret, frame = cap.read()
        if ret:
            # Guardar la imagen capturada
            filename = 'captured_photo.png'
            cv2.imwrite(filename, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            
            # Mostrar la imagen capturada en el bloque de Ursina
            captured_image_block.texture = filename
            captured_image_block.scale = (1.5, 1)

app.run()
