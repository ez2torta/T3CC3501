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


class Cubo(object):


	def __init__(self):
		self.textures = [
		    load_texture('ejemplo_data/metal-texture.jpg'),
		    load_texture('ejemplo_data/metal-normal.jpg'),
		    load_texture('ejemplo_data/metal-bump.jpg')
		]
		self.cubo = Particle()
		self.cubo.add_property('GLLIST', create_cube_textured(self.textures))
		self.cubo.add_property('SIZE', [80, 80, 80])
		self.cubo.add_property('MATERIAL', material_silver)
		self.cubo.set_name('Cubo')

	def update(self):
		self.cubo.update()

	def dibujar(self):
		self.cubo.get_property('MATERIAL')()
		draw_list(self.cubo.get_property('GLLIST'), self.cubo.get_position_list(), 0, None,
              self.cubo.get_property('SIZE'), None)
