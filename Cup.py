import pygame
from pygame.sprite import Sprite 

class Cup(Sprite):
	def __init__(self, screen, fan):
		super(Cup,self). __init__()
		self.screen = screen
		self.image = pygame.image.load("cup.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = fan.x
		self.rect.top = fan.y
		self.speed = 10
		self.direction = 1 
		self.x = self.rect.x
		self.y = self.rect.y

	def update(self):
		if self.direction == 1: #up
			self.y -= self.speed #change the y, each time update is run, by bullet speed
			self.rect.y = self.y #update rect position
		# elif self.direction == 2: #right
		# 	self.x += self.speed #change the y, each time update is run, by bullet speed
		# 	self.rect.x = self.x #update rect position
		# elif self.direction == 3: #down
		# 	self.y += self.speed #change the y, each time update is run, by bullet speed
		# 	self.rect.y = self.y #update rect position
		# else: #left
		# 	self.x -= self.speed #change the y, each time update is run, by bullet speed
		# 	self.rect.x = self.x

	def draw_me(self):
		#self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		self.rect.left = self.x 
		self.rect.right = self.x 
		self.rect.top = self.y 
		self.rect.bottom = self.y 
		self.screen.blit(self.image, [self.x, self.y])