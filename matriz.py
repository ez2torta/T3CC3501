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
import numpy as np

class Matriz(object):

	def __init__(self):
		self.textures = [
		    load_texture('ejemplo_data/metal-texture.jpg'),
		    load_texture('ejemplo_data/metal-normal.jpg'),
		    load_texture('ejemplo_data/metal-bump.jpg')
		]
		# Matrix de 20 x 20
		self.matrix = np.ones((20,20))
		self.cube_matrix = []
		for x in xrange(self.matrix.shape[0]):
		    for y in xrange(self.matrix.shape[1]):
		        integer = self.matrix[x, y]
		        a = 1600-160*x #posicion x
		        b = 1600-160*y #posicion y
		        c = -160 #altura en el eje z?!?!
		        cubo = Particle(a,b,c)
		        cubo.add_property('GLLIST', create_cube_textured(self.textures))
		        cubo.add_property('SIZE', [80, 80, 80])
		        cubo.add_property('MATERIAL', material_white_rubber)
		        self.cube_matrix.append(cubo)



	def update(self):
		for x in self.cube_matrix:
			x.update()

	def dibujar(self):
		for x in self.cube_matrix:
			x.get_property('MATERIAL')()
			draw_list(x.get_property('GLLIST'), x.get_position_list(), 0, None,
            	x.get_property('SIZE'), None)
