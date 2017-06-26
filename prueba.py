# coding=utf-8

# Importación de librerías
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from pygltoolbox.glpython import *
from pygltoolbox.opengl_lib import *
from pygltoolbox.camera import *
from pygltoolbox.particles import *
from pygltoolbox.figures import *
from pygltoolbox.materials import *
from pygltoolbox.textures import *
from pygltoolbox.shader import *
from cubo import Cubo
from luz import Luz
from matriz import Matriz
from prisma import Prisma




# Constantes
AXES_LENGTH = 700
CAMERA_PHI = 45
CAMERA_RAD = 1500.0
CAMERA_ROT_VEL = 2.5
CAMERA_THETA = 45
FPS = 60
NUM_LIGHTS = 2
WINDOW_SIZE = [1280, 720]

# Se inicia ventana
pygame.font.init()
surface = initPygame(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Ejemplo Ejes mas Cubo',
           centered=True)

initGl(transparency=False, materialcolor=False, normalized=True, lighting=True,
       numlights=NUM_LIGHTS,
       perspectivecorr=True, antialiasing=True, depth=True, smooth=True,
       texture=True, verbose=False)
reshape(*WINDOW_SIZE)
# noinspection PyArgumentEqualDefault
initLight(GL_LIGHT0)
initLight(GL_LIGHT1, ambient=DEFAULT_AMBIENT_COLOR, diffuse=DEFAULT_AMBIENT_COLOR,
          specular=DEFAULT_AMBIENT_COLOR)
clock = pygame.time.Clock()

# Se cargan texturas
textures = [
    load_texture('ejemplo_data/metal-texture.jpg'),
    load_texture('ejemplo_data/metal-normal.jpg'),
    load_texture('ejemplo_data/metal-bump.jpg')
]

# Se carga el shader
program = load_shader('ejemplo_data/', 'normalMapShader', [NUM_LIGHTS],
                      [3, NUM_LIGHTS])
program.set_name('NormalMap Shader')

# Se crean objetos
# axis = create_axes(AXES_LENGTH)  # Ejes
camera = CameraR(CAMERA_RAD, CAMERA_PHI,
                 CAMERA_THETA)  # Cámara del tipo esférica

prisma = Prisma()
matriz = Matriz()
cubo = Cubo()

luz_fija = Luz()
# Bucle principal

pygame.mixer.set_num_channels(8)
prismas_totales = len(prisma.cube_matrix)
voice = pygame.mixer.Channel(5)
moving_effect = pygame.mixer.Sound('moving.wav')
coin_effect = pygame.mixer.Sound('coin.wav')

def revisar_keys():
    # Comprueba las teclas presionadas
    keys = pygame.key.get_pressed()

    # Moverse en el eje X
    if keys[K_UP]:
        cubo.move_up()
        camera.move_center_x(-1)
        if not voice.get_busy():
            voice.play(moving_effect)
        

    elif keys[K_DOWN]:
        cubo.move_down()
        camera.move_center_x(+1)
        if not voice.get_busy():
            voice.play(moving_effect)
    # Moverse en el eje Y
    if keys[K_LEFT]:
        cubo.move_left()
        camera.move_center_y(-1)
        if not voice.get_busy():
            voice.play(moving_effect)
    elif keys[K_RIGHT]:
        cubo.move_right()
        camera.move_center_y(+1)
        if not voice.get_busy():
            voice.play(moving_effect)
    # Acerca / aleja la cámara
    if keys[K_n]:
        camera.close()
    elif keys[K_m]:
        camera.far()


def main():

    contador_prismas = 0
    run = True
    file = "vangelis.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1) # If the loops is -1 then the music will repeat indefinitely.
    while run:

        # Se comprueban eventos
        for event in pygame.event.get():
            if event.type == QUIT:  # Cierra la aplicación
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # Cierra la aplicación
                    exit()

        # Crea contador, limpia ventana, establece cámara
        clock.tick(FPS)
        clearBuffer()
        camera.place()

        if islightEnabled():
            glDisable(GL_LIGHTING)
            # glCallList(axis)
            glEnable(GL_LIGHTING)
        else:
            glCallList(axis)

        # Se actualizan modelos
        luz_fija.update()
        cubo.update()

        posicion = cubo.position()

        if (prisma.intersects(posicion[0],posicion[1],posicion[2])):
            # print("Intersecté Prisma")
            contador_prismas = contador_prismas + 1
            print("Prismas : "+str(contador_prismas) + " / "+ str(prismas_totales))
            coin_effect.play()
            if(contador_prismas == prismas_totales):
                print("Felicidades! Capturaste todos los prismas")
                print("Juego Terminado")
                run = False
        if (matriz.intersects(posicion[0],posicion[1],posicion[2]) and matriz.hay_cubo_arriba(posicion[0],posicion[1],posicion[2])):
            cubo.subir()
        if not (matriz.sobre(posicion[0],posicion[1],posicion[2])):
            if(matriz.hay_cubo_debajo(posicion[0],posicion[1],posicion[2])):
                cubo.bajar()
            else:
                print("No estas pisando ningun cubo y has caído en el vacío eterno")
                print("Juego Terminado")
                run = False

        else:
            prisma.update()
            matriz.update()

            # Dibuja luces
            luz_fija.dibujar()

            # Dibuja modelos
            program.start()
            program.uniformi('toggletexture', True)
            program.uniformi('togglebump', True)
            program.uniformi('toggleparallax', True)

            for i in range(3):
                program.uniformi('texture[{0}]'.format(i), i)
            # noinspection PyArgumentEqualDefault
            cubo.dibujar()
            prisma.dibujar()
            matriz.dibujar()
            program.stop()

            revisar_keys()

        pygame.display.flip()

main()
