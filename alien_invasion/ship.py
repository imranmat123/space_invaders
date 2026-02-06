import pygame

class Ship:
	""""A class to manage the ship"""

	def __init__(self, ai_game):
		""""initialise the ship and its starting position"""
		self.setting = ai_game.settings
		self.screen = ai_game.screen
		self.SR = ai_game.screen.get_rect()

		#Load the ship image and get its rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Start each new ship at the buttom center of the screen.
		self.rect.midbottom = self.SR.midbottom

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		#moving for left and right
		self.move_left = False
		self.move_right = False
		self.move_up = False
		self.move_down = False




	def movement_settings(self):

		if self.move_right and  self.rect.right > self.SR.right:
			self.move_right = False
		elif self.move_left and  self.rect.left < 0:
			self.move_left = False
		elif self.move_down and self.rect.bottom > 799:
			self.move_down = False
		elif self.move_up and self.rect.top < 0:
			self.move_up = False






		if self.move_right:
			self.x = self.x + self.setting.speed
		if self.move_left:
			self.x = self.x - self.setting.speed
		if self.move_up:
			self.y = self.y - self.setting.speed
		if self.move_down:
			self.y = self.rect.y + self.setting.speed

		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		""""draw the ship at its current location"""
		self.screen.blit(self.image,self.rect)
