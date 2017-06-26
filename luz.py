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


class Luz(object):


	def __init__(self):
		self.luz = Particle(1000, -1000, 1000)
		self.luz.set_name('Luz fija')
		self.luz.add_property('GLLIST', create_cube())
		self.luz.add_property('SIZE', [50, 50, 50])
		self.luz.add_property('MATERIAL', material_silver)

	def update(self):
		self.luz.update()

	def dibujar(self):
		self.luz.exec_property_func('MATERIAL')
		glLightfv(GL_LIGHT1, GL_POSITION, self.luz.get_position_list())
		# noinspection PyArgumentEqualDefault
		draw_list(self.luz.get_property('GLLIST'), self.luz.get_position_list(), 0,
		          None, self.luz.get_property('SIZE'),
		          None)
