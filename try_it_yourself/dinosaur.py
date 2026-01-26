import pygame.image


class Dinosaur:

	def __init__(self,background):
		self.screen = background.screen
		self.screen_rect = background.screen.get_rect()

		self.image = pygame.image.load('../images/d3.png')
		self.rect = self.image.get_rect()

		self.rect.center = self.screen_rect.center

		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False


	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		if self.moving_right == True:
			self.rect.x += 10
		elif self.moving_left == True:
			self.rect.x -= 10
		elif self.moving_up == True:
			self.rect.y -= 10
		elif self.moving_down == True:
			self.rect.y += 10
