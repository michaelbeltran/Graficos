#!/usr/bin/python
import pygame, sys, pygame.gfxdraw
import math
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

class Graficos(object):
	def __init__(self, width, height):
		self.unidad = 10
		self.width = width
		self.height = height
		self.size = width+1, height+1
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption("Graficos")
		self.screen.fill((255,255,255))
		self.plano()
		self.ecuacion()
		pygame.display.update()
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()
	def plano(self):
		unidad = self.unidad
		pygame.gfxdraw.hline(self.screen, 0, self.width, self.height/2, BLACK)
		pygame.gfxdraw.vline(self.screen, self.width/2, 0, self.height, BLACK)
		for i in range(0, self.width+1, unidad):
			pygame.gfxdraw.vline(self.screen, i, (self.height/2)+4, (self.height/2)-4, BLACK)
		for j in range(0, self.height+1, unidad):
			pygame.gfxdraw.hline(self.screen, (self.width/2)-4, (self.width/2)+4, j, BLACK)
	def punto(self, x, y):
		x = x*self.unidad+self.width/2.0
		y = -y*self.unidad+self.height/2.0
		pygame.gfxdraw.pixel(self.screen, int(x), int(y), BLACK)
		print x, y, "|",
	def ecuacion(self):
		k=0
		for i in range(0, 10):#(-self.width/self.unidad, self.width/self.unidad):
			for j in range(self.unidad):
				k += 0.1
				#self.punto(k, math.tan(k))
				self.punto(k,k)
			print ""
def main():
	grafi = Graficos(600,600)

if __name__ == "__main__":
	main()
