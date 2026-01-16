import pygame

class Ship:
	""""A class to manage the ship"""

	def __init__(self, ai_game):
		""""initialise the ship and its starting position"""
		self.screen = ai_game.screen
		self.SR = ai_game.screen.get_rect()
		#Load the ship image and get its rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()


		# Start each new ship at the buttom center of the screen.
		self.rect.midbottom = self.SR.midbottom

	def blitme(self):
		""""draw the ship at its current location"""
		self.screen.blit(self.image,self.rect)
