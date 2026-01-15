import sys

import pygame

from settings import settings

class AlienInvasion:
	""""class to handle game assess and behavior"""
	def __init__(self):
		pygame.init()
		self.settings = settings()
		self.screen = pygame.display.set_mode(size=(self.settings.screen_width,
													self.settings.screen_hight))
		self.clock = pygame.time.Clock()
		pygame.display.set_caption("Alien Invasion")


	def run_game(self):
		""""start main loop for the game"""
		while True:
			# watch out for KBM events
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					sys.exit()
			# make most recent draw screen avilable
			pygame.display.flip()
			self.clock.tick(60)
			self.screen.fill(self.settings.bg_color)

if __name__ == '__main__':
	# make a game instance, and run the game
	ai = AlienInvasion()
	ai.run_game()
