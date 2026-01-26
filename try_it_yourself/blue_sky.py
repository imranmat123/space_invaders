import sys

import pygame
from alien_invasion import settings as s
from dinosaur import Dinosaur

class blue_sky:

	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((1200,800 ))
		self.color = s.settings()
		pygame.display.set_caption("blue sky")
		self.dino = Dinosaur(self)
		self.clock = pygame.time.Clock()

	def run_game(self):
		while True:
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					sys.exit()
				elif e.type == pygame.KEYDOWN:
					if e.key == pygame.K_d:
						self.dino.moving_right = True
					elif e.key == pygame.K_a:
						self.dino.moving_left = True
					elif e.key == pygame.K_w:
						self.dino.moving_up = True
					elif e.key == pygame.K_s:
						self.dino.moving_down = True
				elif e.type == pygame.KEYUP:
					if e.key == pygame.K_d:
						self.dino.moving_right = False
					elif e.key == pygame.K_a:
						self.dino.moving_left = False
					elif e.key == pygame.K_w:
						self.dino.moving_up = False
					elif e.key == pygame.K_s:
						self.dino.moving_down = False
			self.dino.update()
			pygame.display.flip()
			self.screen.fill((0,255,255))
			self.dino.blitme()
			self.clock.tick(60)


if __name__ == '__main__':
	sky = blue_sky()
	sky.run_game()


