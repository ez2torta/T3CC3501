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
		self.cubo.angle = 0
		self.angle_rotation = [0,0,0]


	def update(self):
		self.cubo.update()

	def position(self):
		return self.cubo.get_position_list()

	def dibujar(self):
		self.cubo.get_property('MATERIAL')()
		
		# print(angles)
		draw_list(self.cubo.get_property('GLLIST'), self.cubo.get_position_list(), self.cubo.angle, self.angle_rotation,
              self.cubo.get_property('SIZE'), None)

	def move_left(self):
		self.angle_rotation = [1,0,0]
		self.cubo.angle = self.cubo.angle + 2
		self.cubo.move_y(-2)
		#ToDo
		# return 0

	def move_right(self):
		self.angle_rotation = [1,0,0]
		self.cubo.angle = self.cubo.angle - 2
		self.cubo.move_y(+2)
		#ToDo
		# return 0

	def move_down(self):
		self.angle_rotation = [0,1,0]
		self.cubo.angle = self.cubo.angle + 2
		self.cubo.move_x(2)

		#ToDo
		# return 0

	def move_up(self):
		self.angle_rotation = [0,1,0]
		self.cubo.angle = self.cubo.angle - 2
		self.cubo.move_x(-2)

		#ToDo
		# return 0


	def subir(self):
		self.cubo.move_z(160)
		pass

	def bajar(self):
		self.cubo.move_z(-160)
		pass
