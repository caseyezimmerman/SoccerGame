import pygame
from pygame.sprite import Sprite 

class Player2(Sprite):
	def __init__(self, screen):
		super(Player2,self). __init__()
		self.image = pygame.image.load("soccer_player2.png")
		self.rect = self.image.get_rect()
		self.x = 100
		self.y = 100
		self.width = 45
		self.height = 81
		self.speed = 2
		self.screen = screen

	def draw_me(self):
		self.screen.blit(self.image, [self.x, self.y])
		self.rect.left = self.x
		self.rect.right = self.x + 45
		self.rect.top = self.y + 80
		self.rect.bottom = self.y +80