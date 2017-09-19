import pygame
from pygame.sprite import Sprite 
import time

class Defense(Sprite):
	def __init__(self, screen):
		super(Defense,self). __init__()
		self.image = pygame.image.load("soccer_player2.png")
		#self.rect = pygame.Rect(100, 100, 50, 100)
		self.rect = self.image.get_rect()
		self.x = 100
		self.y = 100
		self.width = 50
		self.height = 85
		self.speed = 2
		self.screen = screen
		self.stunned = False
		self.when_stunned = time.time()

	def draw_me(self):
		#self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		self.rect.left = self.x -20
		self.rect.right = self.x + 20
		self.rect.top = self.y -20
		self.rect.bottom = self.y +20
		self.screen.blit(self.image, [self.x, self.y])

	def update(self):
		self.rect.topleft = self.x, self.y
		
		