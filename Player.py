import pygame
from pygame.sprite import Sprite 

class Player(Sprite):
	def __init__(self, screen):
		super(Player,self). __init__()
		self.image = pygame.image.load("soccer_player.png")
		self.rect = self.image.get_rect()
		self.x = 900
		self.y = 100
		self.width = 50
		self.height = 80
		self.speed = 10
		self.screen = screen

	def draw_me(self):
		self.rect.left = self.x -10
		self.rect.right = self.x + 20
		self.rect.top = self.y -10 
		self.rect.bottom = self.y + 80
		self.screen.blit(self.image, [self.x, self.y])

	def update(self):
		self.rect.topleft = self.x, self.y
		