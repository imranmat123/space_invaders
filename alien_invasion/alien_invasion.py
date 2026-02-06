import sys

import pygame

from ship import Ship
from settings import settings

class AlienInvasion:
	""""class to handle game assess and behavior"""
	def __init__(self):
		pygame.init()
		self.settings = settings()
		self.screen = pygame.display.set_mode(size=(self.settings.screen_width,
													self.settings.screen_hight))
		self.clock = pygame.time.Clock()
		self.ship = Ship(self)
		pygame.display.set_caption("Alien Invasion")


	def run_game(self):
		""""start main loop for the game"""
		while True:
			# watch out for KBM events
			self._check_events()
			# make most recent draw screen avilable
			self._update_screen()
			self.clock.tick(60)

	def _update_screen(self):
		""""update screen helper function"""
		self.ship.blitme()
		pygame.display.flip()
		self.screen.fill(self.settings.bg_color)
		self.ship.movement_settings()


	def _check_events(self):
		""""check events helper function"""
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				sys.exit()
			elif e.type == pygame.KEYDOWN:
				if e.key == pygame.K_d:
					self.ship.move_right = True
				if e.key == pygame.K_a:
					self.ship.move_left = True
				if e.key == pygame.K_w:
					self.ship.move_up = True
				if e.key == pygame.K_s:
					self.ship.move_down = True

			elif e.type == pygame.KEYUP:
				if e.key == pygame.K_d:
						self.ship.move_right = False
				if e.key == pygame.K_a:
						self.ship.move_left = False
				if e.key == pygame.K_w:
						self.ship.move_up = False
				if e.key == pygame.K_s:
						self.ship.move_down = False



if __name__ == '__main__':
	# make a game instance, and run the game
	ai = AlienInvasion()
	ai.run_game()
