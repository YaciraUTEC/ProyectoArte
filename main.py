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

# Cargar el modelo .fbx y asignar una textura
modelo = load_model('Classicsofadesign.obj')
modelo1=load_model('Lamp.glb')
modelo2=load_model('mesa.obj')
modelo3=load_model('cajon.obj')
modelo4=load_model('vasa.obj')
                                              #   (adelante,arriba o abajo,costados)
sala = Entity(model=modelo, scale=30, texture='im.jpg', position=(-90, 10, -380))
lampara = Entity(model=modelo1, scale=35, texture='lampara.png', position=(-90, 5, -250))
mesa = Entity(model=modelo2, scale=28, texture='madera.jpg', position=(-10, 5, -350))
#librero = Entity(model=modelo3, scale=0.6, texture='madera1.jpg', position=(90, 5, -350))
librero = Entity(model=modelo3, scale=60, texture='madera1.jpg', position=(90, 5, -350))
jarron = Entity(model=modelo4, scale=20, texture='patron.jpeg', position=(-10, 27, -350))
sala.rotation_y = -180  # Rotar la entidad en el eje Y
librero.rotation_y =-90
jarron.rotation_x =-90
player = FirstPersonController(speed=150, position=(0, 100,-900), scale=30)  # Nueva posición del jugador
Sky()

def input(key):
    if key == 'escape':
        quit()

# Crear el suelo 
platform = Entity(model="cube", collider="box", texture="piso", scale=(500, 1, 2000), position=(0, 0, 0))



#lado izquierdo

wall_1_1 = Entity(model='cube', scale=(15, 240, 5), color=color.white, collider='box')
wall_1_1.x = -125
wall_1_1.z = -500
wall_1_1.y = 120

#lado derecho
wall_1_1 = Entity(model='cube', scale=(15, 240, 5), color=color.white, collider='box')
wall_1_1.x = 125
wall_1_1.z = -500
wall_1_1.y = 120

#lado central inferior
wall_1_1 = Entity(model='cube', scale=(235, 50, 5), color=color.white, collider='box')
wall_1_1.x = 0
wall_1_1.z = -500
wall_1_1.y = 25

#lado central superior
wall_1_1 = Entity(model='cube', scale=(235, 30, 5), color=color.white, collider='box')
wall_1_1.x = 0
wall_1_1.z = -500
wall_1_1.y = 225
#----------------------------------------------------------------

#Costado izquierdo
wall_1_1 = Entity(model='cube', scale=(5, 240, 400), color=color.white, texture = "pared sala.jpeg", collider='box')
wall_1_1.x = -128
wall_1_1.z = -300
wall_1_1.y = 120

#Costado derecho
wall_1_1 = Entity(model='cube', scale=(5, 240, 400), color=color.white, texture = "fondo_sala.jpg", collider='box')
wall_1_1.x = 128
wall_1_1.z = -300
wall_1_1.y = 120
#colocar imagenes para la fachada                                            - derecha + inquierda   
                                                                                    #costado , #arriba abajo ,adelande y atras                                                    
img1= Entity(model="cube",scale=(35,35,0), texture="corazon.png",collider="box",position=(-100, 25,-505))
img2= Entity(model="cube",scale=(20,20,0), texture="mensaje.png",collider="box",position=(-60, 25,-505))
img3= Entity(model="cube",scale=(20,20,0), texture="enviar.png",collider="box",position=(-20, 25,-505))
img4= Entity(model="cube",scale=(22,22,0), texture="guardar.png",collider="box",position=(105, 25,-505))
img5= Entity(model="cube",scale=(20,20,0), texture="perfil.png",collider="box",position=(-100, 220,-505))
img6= Entity(model="cube",scale=(60,20,0), texture="nombre.png",collider="box",position=(-60, 220,-505))
img7= Entity(model="cube",scale=(18,18,0), texture="check.png",collider="box",position=(-20, 220,-505))
img8= Entity(model="cube",scale=(16,15,0), texture="puntos.png",collider="box",position=(112, 220,-505))



#-------------------parte trasera
#lado izquierdo

wall_1_1 = Entity(model='cube', scale=(100, 240, 5), color=color.white, texture = "sala1.jpeg", collider='box')
wall_1_1.x = -81
wall_1_1.z = -105
wall_1_1.y = 120

#lado derecho
wall_1_1 = Entity(model='cube', scale=(100, 240, 5), color=color.white, texture = "sala1.jpeg", collider='box')
wall_1_1.x = 81
wall_1_1.z = -105
wall_1_1.y = 120


#lado central superior
wall_1_1 = Entity(model='cube', scale=(65, 80, 5), color=color.white, texture = "sala2.jpeg", collider='box')
wall_1_1.x = 0
wall_1_1.z = -105
wall_1_1.y = 200


#HABITACION 2
#Costado izquierdo
wall_1_1 = Entity(model='cube', scale=(100, 240, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = -81
wall_1_1.z = -99.5
wall_1_1.y = 120

#lado derecho
wall_1_1 = Entity(model='cube', scale=(100, 240, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = 81
wall_1_1.z = -99.5
wall_1_1.y = 120


#lado central superior
wall_1_1 = Entity(model='cube', scale=(65, 80, 5), color=color.white, texture = "wall4.jpg", collider='box')
wall_1_1.x = 0
wall_1_1.z = -99.5
wall_1_1.y = 200

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
