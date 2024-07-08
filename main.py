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

# Cargar el modelo .obj y asignar una textura
modelo = load_model('Classicsofadesign.obj')
modelo1=load_model('Lamp.glb')
modelo2=load_model('mesa.obj')
modelo3=load_model('tv_table.obj')
modelo4=load_model('vasa.obj')
modelo5=load_model('tele.obj')
modelo6=load_model('planta.obj')
modelo7=load_model('velas.obj')
modelo8=load_model('reloj.fbx')
modelo9=load_model('Classicsofadesign.obj')
modelo10=load_model('cojin.obj')
modelo11=load_model('cojin.obj')
modelo12=load_model('cojin.obj')
modelo13=load_model('cojin.obj')
modelo14=load_model('librero.obj')
modelo15=load_model('lab.FBX')

                                              #   (adelante,arriba o abajo,costados)
sala = Entity(model=modelo, scale=30, texture='im.jpg', position=(-90, 10, -390))
lampara = Entity(model=modelo1, scale=35, texture='lampara.png', position=(-90, 5, -250))
planta = Entity(model=modelo6, scale=0.7, texture='planta.png', position=(-90, 5, -460))
mesa = Entity(model=modelo2, scale=28, texture='madera.jpg', position=(-15, 5, -360))
#librero = Entity(model=modelo3, scale=0.6, texture='madera1.jpg', position=(90, 5, -350))
estante = Entity(model=modelo3, scale=60, texture='im5.jpg', position=(110, 5, -350))
tele = Entity(model=modelo5, scale=15, texture='im3.png', position=(110, 55, -365))
jarron = Entity(model=modelo4, scale=20, texture='patron.jpeg', position=(-10, 27, -350))
velas = Entity(model=modelo7, scale=30, texture='vela.jpg', position=(-10, 27, -370))
reloj = Entity(model=modelo8, scale=0.35, texture='metal.png', position=(-80, 90, -110))
sillon2 = Entity(model=modelo9, scale=(25,30,15), texture='im.jpg', position=(-30, 5, -270))
librero=Entity(model=modelo14, scale=0.6, texture='im5.jpg', position=(110, 5, -210))
laberinto = Entity(model=modelo15, scale=(0.08, 0.05, 0.08), texture='pared.jpg', position=(0, 0, 52))
                                                             #(costados,,adelante)
cojin=Entity(model=modelo10, scale=5, texture='patron.jpeg', position=(-28, 15, -272))
cojin2=Entity(model=modelo11, scale=5, texture='patron2.jpg', position=(0, 15, -272))
cojin3=Entity(model=modelo12, scale=5, texture='patron.jpeg', position=(-90, 18, -320))

cojin4=Entity(model=modelo13, scale=5, texture='patron2.jpg', position=(-80, 18, -400))


cojin.rotation_x =45
cojin.rotation_y =-40

cojin2.rotation_x =45
cojin2.rotation_y =40

cojin3.rotation_x =45
cojin3.rotation_y =-40

cojin4.rotation_x =45
cojin4.rotation_y =-120


sillon2.rotation_y =-90
sala.rotation_y = -180  # Rotar la entidad en el eje Y
tele.rotation_y =-90
jarron.rotation_x =-90
librero.rotation_y =-90
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
wall_1_1 = Entity(model='cube', scale=(5, 240, 400), color=color.white, texture = "pared sala.jpeg", collider='box')
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

l1= Entity(model="cube",scale=(0,21,35), texture="libros.png",collider="box",position=(90, 20, -210))
l2= Entity(model="cube",scale=(0,21,35), texture="libros1.png",collider="box",position=(90, 20, -175))
l3= Entity(model="cube",scale=(0,21,35), texture="libros2.png",collider="box",position=(90, 20, -245))
l4= Entity(model="cube",scale=(0,21,35), texture="libros3.png",collider="box",position=(90, 55, -245))
l5= Entity(model="cube",scale=(0,21,35), texture="libros4.png",collider="box",position=(90, 55, -210))
l6= Entity(model="cube",scale=(0,21,35), texture="libro5.png",collider="box",position=(90, 55, -175))
l7= Entity(model="cube",scale=(0,21,35), texture="libros3.png",collider="box",position=(90, 85, -210))
l8= Entity(model="cube",scale=(0,21,35), texture="libros2.png",collider="box",position=(90, 85, -175))
l9= Entity(model="cube",scale=(0,21,35), texture="libros1.png",collider="box",position=(90, 85, -245))

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



left_wall = Entity(model='cube', scale=(5, 240, 200), color=color.white, texture="mirror.jpg", collider='box')
left_wall.x = -128
left_wall.z = 300
left_wall.y = 120

# Costado derecho
right_wall = Entity(model='cube', scale=(5, 240, 200), color=color.white, texture="mirror.jpg", collider='box')
right_wall.x = 128
right_wall.z = 300
right_wall.y = 120

# Parte trasera
# Lado izquierdo
left_back_wall = Entity(model='cube', scale=(100, 240, 5), color=color.white, texture="wall4.jpg", collider='box')
left_back_wall.x = -80.5
left_back_wall.z = 400
left_back_wall.y = 120

# Lado derecho
right_back_wall = Entity(model='cube', scale=(100, 240, 5), color=color.white, texture="wall4.jpg", collider='box')
right_back_wall.x = 80.5
right_back_wall.z = 400
right_back_wall.y = 120

# Lado central superior
center_back_wall = Entity(model='cube', scale=(220, 80, 5), color=color.white, texture="wall4.jpg", collider='box')
center_back_wall.x = 0
center_back_wall.z = 400
center_back_wall.y = 200

# Elementos adicionales para representar la falsedad en redes sociales
cel1 = Entity(model='cube', texture='cel1.png', scale=(2, 80, 30), position=(-110, 40, 220))
cel1.rotation_y = -45

#fake_likes_screen = Entity(model='quad', scale=(60, 40), texture="fakelikes", position=(0, 180, 350))
fake_comments_screen = Entity(model='cube', scale=(60,125, 10), texture="celular.png", position=(0, 70, 300))
def switch_publication():
    p1.visible = not p1.visible
    p2.visible = not p2.visible
p1=Entity(
    model='quad', 
    scale=(50, 50), 
    texture="publicacion", 
    position=(0, 85, 294),
    collider='box',
    on_click=switch_publication
    )
p2=Entity(
    model='quad', 
    scale=(50, 50), 
    texture="publicacion2", 
    position=(0, 85, 294),
    collider='box',
    on_click=switch_publication,
    visible=False)
#fake_likes_screen1 = Entity(model='quad', scale=(60, 40), texture="emoji", position=(20, 150, 200))
                                                                        #delante y atras,arriba y abajo, costados     
cel2 = Entity(model='cube', texture='cel2', scale=(2, 80, 30), position=(110, 40, 220))
cel2.rotation_y = -145
cel3 = Entity(model='cube', texture='cel3',scale=(2, 80, 30), position=(80, 40, 210))
cel3.rotation_y = -90

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
