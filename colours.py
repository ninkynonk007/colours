import pygame
from random import randint
import time
pygame.init()
screen = pygame.display.set_mode((640,480))
background = pygame.Surface(screen.get_size())
background.fill((255,255,255))
background = background.convert()
screen.blit(background, (0,0))
font = pygame.font.Font(None,36)

flag = 1

mainloop = 1
while (mainloop == 1):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			mainloop = False
		elif event.type == pygame.KEYDOWN:
			if (flag == 0):
				flag = 1
			else:
				flag = 0
	if (flag == 1):
		r = randint(0,255)
		g = randint(0,255)
		b = randint(0,255)
		textr = 255 - r
		textg = 255 - g
		textb = 255 - b
		text= font.render("R(" + str(r) + ") G(" + str(g) + ") B(" + str(b) + ")", 1, (textr, textg, textb))
		background.fill((r,g,b))
		textpos = text.get_rect()
		textpos.x = randint(0,400)
		textpos.y = randint(0,350)
		background.blit(text, textpos)
		background = background.convert()
		screen.blit(background, (0,0))
		pygame.display.flip()
	time.sleep(1)
