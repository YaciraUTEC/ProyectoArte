from turtle import position
from ursina import *
import pygame
from pydub import AudioSegment
from ursina.prefabs.first_person_controller import FirstPersonController



app = Ursina()
modelos_glb = []

def aparecer_modelo():
    # Crear una nueva instancia del modelo cada vez que se haga clic
    modelo_instancia = Entity(
        model='Emoji.glb',  # Reemplaza 'nombre_del_modelo.glb' con tu archivo .glb
        scale=(20, 20, 20),  # Escala del modelo según sea necesario
        position=(random.uniform(190, 150), random.uniform(-100, 100), random.uniform(-505, -750)),  # Posición aleatoria dentro de la habitación
        collider='mesh',
        color=color.random_color()
    )
    modelos_glb.append(modelo_instancia)  # Agregar la instancia a la lista de modelos



# Asegúrate de manejar la lógica de la aplicación Ursina y renderizar la ventana.
def update():
    pass


player = FirstPersonController(speed=150, position=(50, 0, 50), scale=20)  # Nueva posición del jugador
Sky()

def input(key):
    if key == 'escape':
        quit()

# Crear el suelo del museo
platform = Entity(model="cube", collider="box", texture="piso", scale=(500, 1, 2000), position=(0, 0, 0))



#lado izquierdo

wall_1_1 = Entity(model='cube', scale=(20, 240, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = -120
wall_1_1.z = -500
wall_1_1.y = 120

#lado derecho
wall_1_1 = Entity(model='cube', scale=(20, 240, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = 120
wall_1_1.z = -500
wall_1_1.y = 120

#lado central inferior
wall_1_1 = Entity(model='cube', scale=(220, 50, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = 0
wall_1_1.z = -500
wall_1_1.y = 25

#lado central superior
wall_1_1 = Entity(model='cube', scale=(220, 30, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = 0
wall_1_1.z = -500
wall_1_1.y = 225
#----------------------------------------------------------------

#Costado izquierdo
wall_1_1 = Entity(model='cube', scale=(5, 240, 400), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = -128
wall_1_1.z = -300
wall_1_1.y = 120

#Costado derecho
wall_1_1 = Entity(model='cube', scale=(5, 240, 400), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = 128
wall_1_1.z = -300
wall_1_1.y = 120



#-------------------parte trasera
#lado izquierdo

wall_1_1 = Entity(model='cube', scale=(100, 240, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = -81
wall_1_1.z = -100
wall_1_1.y = 120

#lado derecho
wall_1_1 = Entity(model='cube', scale=(100, 240, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = 81
wall_1_1.z = -100
wall_1_1.y = 120


#lado central superior
wall_1_1 = Entity(model='cube', scale=(220, 80, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = 0
wall_1_1.z = -100
wall_1_1.y = 200


#HABITACION 2
#Costado izquierdo

wall_1_1 = Entity(model='cube', scale=(5, 240, 300), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = -128
wall_1_1.z = 52
wall_1_1.y = 120


#Costado derecho
wall_1_1 = Entity(model='cube', scale=(5, 240, 300), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = 128
wall_1_1.z = 52
wall_1_1.y = 120

#-------------------parte trasera
#lado izquierdo

wall_1_1 = Entity(model='cube', scale=(100, 240, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = -80.5
wall_1_1.z = 200
wall_1_1.y = 120

#lado derecho
wall_1_1 = Entity(model='cube', scale=(100, 240, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = 80.5
wall_1_1.z = 200
wall_1_1.y = 120

#lado central superior
wall_1_1 = Entity(model='cube', scale=(220, 80, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = 0
wall_1_1.z = 200
wall_1_1.y = 200



#Habitación 3
#Costado izquierdo

wall_1_1 = Entity(model='cube', scale=(5, 240, 200), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = -128
wall_1_1.z = 300
wall_1_1.y = 120

#Costado derecho
wall_1_1 = Entity(model='cube', scale=(5, 240, 200), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = 128
wall_1_1.z = 300
wall_1_1.y = 120

#-------------------parte trasera
#lado izquierdo

wall_1_1 = Entity(model='cube', scale=(100, 240, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = -80.5
wall_1_1.z = 400
wall_1_1.y = 120

#lado derecho
wall_1_1 = Entity(model='cube', scale=(100, 240, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = 80.5
wall_1_1.z = 400
wall_1_1.y = 120

#lado central superior
wall_1_1 = Entity(model='cube', scale=(220, 80, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = 0
wall_1_1.z = 400
wall_1_1.y = 200

#Habitación 4
#Costado izquierdo

wall_1_1 = Entity(model='cube', scale=(5, 240, 150), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = -128
wall_1_1.z = 475
wall_1_1.y = 120

#Costado derecho
wall_1_1 = Entity(model='cube', scale=(5, 240, 150), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = 128
wall_1_1.z = 475
wall_1_1.y = 120

#-------------------parte trasera
#lado izquierdo
wall_1_1 = Entity(model='cube', scale=(100, 240, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = -80.5
wall_1_1.z = 550
wall_1_1.y = 120


#lado derecho
wall_1_1 = Entity(model='cube', scale=(100, 240, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = 80.5
wall_1_1.z = 550
wall_1_1.y = 120

#lado central superior
wall_1_1 = Entity(model='cube', scale=(220, 80, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = 0
wall_1_1.z = 550
wall_1_1.y = 200
app.run()
