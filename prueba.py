# coding=utf-8

# Importación de librerías
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


def revisar_keys():
    # Comprueba las teclas presionadas
    keys = pygame.key.get_pressed()

    # Moverse en el eje X
    if keys[K_UP]:
        cubo.move_up()
    elif keys[K_DOWN]:
        cubo.move_down()

    # Moverse en el eje Y
    if keys[K_LEFT]:
        cubo.move_left()
    elif keys[K_RIGHT]:
        cubo.move_right()

    # Acerca / aleja la cámara
    if keys[K_n]:
        camera.close()
    elif keys[K_m]:
        camera.far()

# Constantes
AXES_LENGTH = 700
CAMERA_PHI = 45
CAMERA_RAD = 1700.0
CAMERA_ROT_VEL = 2.5
CAMERA_THETA = 56
FPS = 60
NUM_LIGHTS = 2
WINDOW_SIZE = [800, 600]

# Se inicia ventana
initPygame(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Ejemplo Ejes mas Cubo',
           centered=True)
initGl(transparency=False, materialcolor=False, normalized=True, lighting=True,
       numlights=NUM_LIGHTS,
       perspectivecorr=True, antialiasing=True, depth=True, smooth=True,
       texture=True, verbose=False)
reshape(*WINDOW_SIZE)
# noinspection PyArgumentEqualDefault
initLight(GL_LIGHT0)
initLight(GL_LIGHT1, ambient=AMBIENT_COLOR_RED, diffuse=DIFFUSE_COLOR_RED,
          specular=SPECULAR_COLOR_RED)
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
axis = create_axes(AXES_LENGTH)  # Ejes
camera = CameraR(CAMERA_RAD, CAMERA_PHI,
                 CAMERA_THETA)  # Cámara del tipo esférica


matriz = Matriz()

cubo = Cubo()


luz_fija = Luz()
# Bucle principal
while True:

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
        glCallList(axis)
        glEnable(GL_LIGHTING)
    else:
        glCallList(axis)

    # Se actualizan modelos
    luz_fija.update()
    matriz.update()
    cubo.update()

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
    matriz.dibujar()
    program.stop()

    revisar_keys()

    pygame.display.flip()


