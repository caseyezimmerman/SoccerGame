import pygame
from pygame.sprite import Sprite 
import time

class Fan(Sprite):
	def __init__(self, screen):
		super(Fan,self). __init__()
		self.image = pygame.image.load("fan_image.png")
		#self.rect = pygame.Rect(100, 100, 50, 100)
		self.rect = self.image.get_rect()
		self.x = 0
		self.y = 575
		self.dx = 10
		self.width = 47
		self.height = 85
		self.speed = 10
		self.screen = screen
		self.direction = 1
		# self.stunned = False
		# self.when_stunned = time.time()

	def draw_me(self):
		#self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		self.rect.left = self.x -20
		self.rect.right = self.x + 20
		self.rect.top = self.y -20
		self.rect.bottom = self.y +20
		self.screen.blit(self.image, [self.x, self.y])