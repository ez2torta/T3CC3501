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
		self.cubo.angle_x = 0
		self.cubo.angle_y = 0
		self.cubo.angle_z = 0

	def update(self):
		self.cubo.update()

	def dibujar(self):
		self.cubo.get_property('MATERIAL')()
		angles = [0,1,0]
		draw_list(self.cubo.get_property('GLLIST'), self.cubo.get_position_list(), self.cubo.angle_x, angles,
              self.cubo.get_property('SIZE'), None)

	def move_left(self):
		#ToDo
		return 0

	def move_right(self):
		#ToDo
		return 0

	def move_down(self):
		self.cubo.stop()
		self.cubo.angle_x = self.cubo.angle_x + 5
		self.cubo.move_x(10)

		self.cubo.start()
		print("moviendome hacia abajo")
		#ToDo
		# return 0

	def move_up(self):

		self.cubo.stop()
		self.cubo.angle_x = self.cubo.angle_x - 5
		self.cubo.move_x(-10)

		self.cubo.start()
		print("moviendome hacia arriba")
		#ToDo
		# return 0
		
