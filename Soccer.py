import pygame
from pygame.sprite import Group, groupcollide
from math import fabs, hypot
from Player import Player
from Ball import Ball
from Defense import Defense
import random
import time
from time import clock
from Fan import Fan
from Cup import Cup


#from Soccer_player import Soccer_player

pygame.init()

screen_size = (1280, 665)
screen = pygame.display.set_mode(screen_size)

background_image = pygame.image.load("soccer2.jpg")
#player_image = pygame.image.load("soccer_player.png")
# soccer_ball = pygame.image.load("soccer_ball.png")
pygame.display.set_caption("Soccer Game!")
pygame.mixer.music.load("music.wav")
pygame.mixer.music.play(-1)
FPS = 60

player = Player(screen)
defense = Defense(screen)
ball = Ball(screen)
fan = Fan(screen)



players = Group()
players.add(player)
balls = Group()
balls.add(ball)
defenses = Group()
defenses.add(defense)
cups = Group()


ball_place = True
score = 2

black = (0, 0, 0)


#ball_rect = pygame.Rect(ball.x, ball.y, ball.width, ball.height)
player_rect = pygame.Rect(player.x, player.y, player.width, player.height)

# player = {
# 	"x": 200,
# 	"y": 100,
# 	"speed": 10
# }

# ball = {
# 	"x": 490,
# 	"y": 180,
# 	"speed": 1
# }

keys = {
	"up": 273,
	"down": 274,
	"right": 275,
	"left": 276
}

keys_down = {
	"up": False,
	"down": False,
	"left": False,
	"right": False
}

def gameOver():
	myFont = pygame.font.SysFont("monaco", 72)
	GOsurf = myFont.render("Game Over", True, black) ##true is to make it antialiased 
	GOrect = GOsurf.get_rect()
	GOrect.midtop = (360, 15)
	screen.blit(GOsurf, GOrect)
	pygame.display.flip()
	showScore(0)
	time.sleep(4)
	pygame.quit()

def Winner():
	wFont = pygame.font.SysFont("monaco", 72)
	Wsurf = wFont.render("Congratulations you reached level 10, you WIN!!", True, black) ##true is to make it antialiased 
	Wrect = Wsurf.get_rect()
	Wrect.midtop = (600, 15)
	screen.blit(Wsurf, Wrect)
	pygame.display.flip()
	showScore(0)
	time.sleep(4)
	pygame.quit()
	

def showScore(choice=1):
	sFont = pygame.font.SysFont("monaco", 24)
	Ssurf = sFont.render("Score: {0}" .format(score), True, black)
	Srect = Ssurf.get_rect()
	if choice == 1:
		Srect.midtop = (80, 10)
	else: 
		Srect.midtop = (360, 120)
	screen.blit(Ssurf, Srect)
	pygame.display.flip()


current_level = 1
tick = 0
tick_two = 0
game_on = True
while game_on: 
#loop through all pygame events
#this is how to exit game
	tick += 1
	tick_two += 1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False
		elif event.type == pygame.KEYDOWN:
			if event.key == keys["up"]:
				keys_down["up"] = True
			elif event.key == keys["down"]:
				keys_down["down"] = True
			elif event.key == keys["right"]:
				keys_down["right"] = True
			elif event.key == keys["left"]:
				keys_down["left"] = True
			elif event.key == 32: ##spacebar
				new_cup = Cup(screen, fan)  #instantiate an object
				cups.add(new_cup)

		elif event.type == pygame.KEYUP:
			if event.key == keys ["up"]:
				keys_down["up"] = False
			if event.key == keys ["down"]:
				keys_down["down"] = False
			if event.key == keys ["right"]:
				keys_down["right"] = False
			if event.key == keys ["left"]:
				keys_down["left"] = False

			

	if keys_down["up"]:
		if player.y > 0:
			player.y -= player.speed
	elif keys_down["down"]:
		if player.y < 660:
			player.y += player.speed
	if keys_down["left"]:
		if player.x > 0:
			player.x -= player.speed
	elif keys_down["right"]:
		if player.x < 1270:
			player.x += player.speed

	
	#print defense.x, defense.y

	# distance_between = fabs(player.x - ball.x) + fabs(player.y - ball.y)
	# if distance_between < 32:
	# 	print "Collision"
	# else:
	# 	print "Not touching"

	screen.blit(background_image, [0,0])
	fan.draw_me()


	for player in players:
	#update the bad guy based on where the player is
		player.update()
		player.draw_me()

	player.draw_me()

	for cup in cups:
		cup.draw_me()
		cup.update()

	for ball in balls:
		#ball.update()
		ball.draw_me()

	for defense in defenses:
		defense.update()
		defense.draw_me()
		dx = defense.x - ball.x
		dy = defense.y - ball.y
		dist = hypot(dx,dy)

		dx = dx / dist
		dy = dy / dist

		defense.x -= dx * defense.speed  ##to make him run away just change to += instead of -=
		defense.y -= dy * defense.speed
		if defense.stunned == True:
			defense.speed = 0
		if tick_two % 90 == 0:
			defense.stunned = False
			defense.speed = 2 

	result = groupcollide(players, balls, False, True)
	if result:
		balls.add(Ball(screen))
		score += 1
		ball_place = False

	result = groupcollide(defenses, balls, False, True)
	if result:
		balls.add(Ball(screen))
		score -= 1
		ball_place = False

	result = groupcollide(cups, defenses, True, False)
	if result:
		for cup,defenses_hit in result.iteritems():
			defenses_hit[0].stunned = True
	

	if score == 4 and current_level == 1:
		defenses.add(Defense(screen))
		defense.speed += 1
		current_level = 2
	if score == 7 and current_level == 2:
		defenses.add(Defense(screen))
		defense.speed += 1
		current_level = 3
	if score == 10 and current_level == 3:
		defenses.add(Defense(screen))
		defense.speed += 1
		current_level = 4
	if score == 13 and current_level == 4:
		defenses.add(Defense(screen))
		defense.speed += 1.5
		current_level = 5
	if score == 15 and current_level == 5:
		defenses.add(Defense(screen))
		defense.speed += 2
		player.speed += 2
		current_level = 6
	if score == 17 and current_level == 6:
		defenses.add(Defense(screen))
		defense.speed += 2
		current_level = 7
	if score == 20 and current_level == 7:
		defenses.add(Defense(screen))
		defense.speed += 2
		current_level = 8
	if score == 23 and current_level == 8:
		defenses.add(Defense(screen))
		defense.speed += 2
		current_level = 9
	if score == 25 and current_level == 9:
		defenses.add(Defense(screen))
		defense.speed += 2
		current_level = 10

	

	if tick % .5 == 0:
		fan.x += fan.speed * fan.direction  ##makes monster move away from us
		
	if tick % .5 == 0 and fan.x >= 1200:
 		fan.direction = fan.direction * -1

 	if tick % .5 == 0 and fan.x <= 0:
 		fan.direction = fan.direction * -1
		


	# if ball_place == False:
	# 	ball.x = random.randrange(1, 900)
	# 	ball.y = random.randrange(1, 500)
	# ball_place = True

	
		

	# if ball_rect.colliderect(player_rect):
	# 	print "Collide"

	# for p in players:
	# 	if pygame.sprite.collide_rect(ball, player):
	# 		if(player.dir =="left"):
	# 			ball.x += 1
	# 		if(player.dir =="right"):
	# 			ball.x -= 1
	# 		if(player.dir =="up"):
	# 			ball.y += 1
	# 		if(player.dir =="down"):
	# 			ball.y -= 1





	# dx = ball["x"] - player["x"]
	# dy = ball["y"] - player["y"]
	# dist = hypot(dx,dy)

	# dx = dx / dist
	# dy = dy / dist

	# ball ["x"] += dx * ball["speed"]  ##to make him run away just change to += instead of -=
	# ball ["y"] += dy * ball["speed"]
	# 	elif event.type == pygame.KEYDOWN:
	# 		#print "User pressed a key!"
	# 		if event.key == keys["up"]: ##273 is the up arrow key
	# 			#player['y'] -= player['speed']
	# 			#print "key is pressed"
	# 			keys_down["up"] == True
	# 		elif event.key == keys["down"]:
	# 			#player ['y'] += player ["speed"]
	# 			keys_down["down"] == True
	# 		elif event.key == keys["right"]:
	# 			#player ['x'] += player['speed']
	# 			keys_down["right"] == True
	# 		elif event.key == keys["left"]:
	# 			#player['x'] -= player['speed']
	# 			keys_down["left"] == True


	# 	elif event.type == pygame.KEYUP:
	# 		if event.key == keys["up"]:
	# 			keys_down["up"] = False
	# 		if event.key == keys["down"]:
	# 			keys_down["down"] = False
	# 		if event.key == keys["right"]:
	# 			keys_down["right"] = False
	# 		if event.key == keys["left"]:
	# 			keys_down["left"] = False

	# if keys_down["up"]:
	# 	player["y"] -= player["speed"]
	# elif keys_down["down"]:
	# 	player["y"] += player["speed"]
	# if keys_down["left"]:
	# 	player["x"] -= player["speed"]
	# elif keys_down["right"]:
	# 	player["x"] += player["speed"]

	
	
	#player.draw_me()
	#ball.draw_me()




	#ball.checkCollision(ball, player)
	#screen.blit(player_image, [player["x"], player["y"]])
	#screen.blit(soccer_ball, [ball["x"], ball["y"]])
	showScore()
	pygame.display.flip()

	if score == 0:
		gameOver()

	if current_level == 10:
		Winner()

	# if score < 0:
	# 	gameOver
	

	

	