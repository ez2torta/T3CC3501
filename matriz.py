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
			load_texture('ejemplo_data/blanco.jpg'),
		]
		# Matrix de 20 x 20

		# self.matrix = np.ones((self.x,self.y))
		self.matrix = np.matrix([
								[0,1,1,0,0,0,1,0],
								[0,1,0,1,0,0,0,1],
								[0,1,1,1,0,0,0,1],
								[0,1,1,1,0,0,0,1],
								[0,2,2,1,1,1,1,1],
								[0,2,2,1,1,1,1,1],
								[0,1,1,1,0,0,0,1],
								[0,1,0,1,0,0,0,1],
								])
		self.x = self.matrix.shape[0]
		self.y = self.matrix.shape[1]
		self.cube_matrix = []
		for x in xrange(self.x):
			for y in xrange(self.y):
				integer = self.matrix[x, y]
				if integer == 0:
					continue
				if integer == 1:
					cubo = self.create_cube(x,y,0)
					self.cube_matrix.append(cubo)
				elif integer == 2:
					cubo = self.create_cube(x,y,0)
					cubo2 = self.create_cube(x,y,160)
					self.cube_matrix.append(cubo)
					self.cube_matrix.append(cubo2)

	def update(self):
		for x in self.cube_matrix:
			x.update()

	def dibujar(self):
		for x in self.cube_matrix:
			x.get_property('MATERIAL')()
			draw_list(x.get_property('GLLIST'), x.get_position_list(), 0, None,
				x.get_property('SIZE'), None)

	def create_cube(self,x,y,z):
		a = self.x*160/2-160*x #posicion x
		b = self.y*160/2-160*y #posicion y
		c = -160+z #altura en el eje z?!?!
		cubo = Particle(a,b,c)
		cubo.add_property('GLLIST', create_cube())
		cubo.add_property('SIZE', [80, 80, 80])
		cubo.add_property('MATERIAL', material_white_plastic)
		return cubo


	def sobre(self, x, y, z):
		for c in self.cube_matrix:
			if self.encima_cubo(c, x, y, z):
				# return True
				return True
		return False

	def intersects(self, x, y, z):
		for c in self.cube_matrix:
			if self.collides(c, x, y, z):
				# return True
				return True
		return False

	def collides(self, c, x, y, z):
		pos_x = c.get_x()
		pos_y = c.get_y()
		pos_z = c.get_z()
		if (pos_x-80 <= x and x <= pos_x+80) and (pos_y-80 <= y and y <= pos_y+80) and(pos_z-80 <= z and z <= pos_z+80):
			return True
		else:
			return False

	def encima_cubo(self, c, x, y, z):
		pos_x = c.get_x()
		pos_y = c.get_y()
		pos_z = c.get_z()
		if (pos_x-80 <= x and x <= pos_x+80) and (pos_y-80 <= y and y <= pos_y+80) and (pos_z+80 <= z and z <= pos_z+160):
			return True
		else:
			return False


	def hay_cubo_debajo(self, x, y, z):
		for c in self.cube_matrix:
			pos_x = c.get_x()
			pos_y = c.get_y()
			pos_z = c.get_z()
			if (pos_x-80 <= x and x <= pos_x+80) and (pos_y-80 <= y and y <= pos_y+80) and (pos_z+240 <= z and z <= pos_z+320):
				return True
		return False

	def hay_cubo_arriba(self,  x, y, z):
		for c in self.cube_matrix:
			pos_x = c.get_x()
			pos_y = c.get_y()
			pos_z = c.get_z()
			if (pos_x-80 <= x and x <= pos_x+80) and (pos_y-80 <= y and y <= pos_y+80) and (pos_z == z):
				return True
		return False



