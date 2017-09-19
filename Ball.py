import pygame
from pygame.sprite import Sprite 
from Player import Player
import random

class Ball(Sprite):
	def __init__(self, screen):
		super(Ball,self). __init__()
		self.image = pygame.image.load("soccer_ball2.png")
		self.rect = self.image.get_rect()
		self.x = random.randrange(1, 900)
		self.y = random.randrange(1, 500)
		self.width = 20
		self.height = 20
		self.speed = 0
		self.screen = screen


	def draw_me(self):
		self.screen.blit(self.image, [self.x, self.y])
		self.rect.left = self.x
		self.rect.right = self.x
		self.rect.top = self.y
		self.rect.bottom = self.y

	# def checkCollision(self, sprite1, sprite2):
	# 	col = pygame.sprite.collide_rect(sprite1, sprite2)
	# 	if col == True:
	# 		self.x += 1
        	