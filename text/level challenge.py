import pygame
pygame.init()

x = 400
y = 400

#colors
white = [255, 255, 255]
black = [0, 0, 0]
red = (176,34,6)
yellow = (255,193,89)

#set up screen
DISPLAY = pygame.display.set_mode([x,y])
pygame.display.set_caption('Text on screen')

running = True

font = pygame.font.Font(None, 24)
#need to add a font variable

while running:
    DISPLAY.fill(black)

    text = font.render("Level 1", True, white)
    DISPLAY.blit(text, [100, 100])

    text2 = font.render("Level 2", True, red)
    DISPLAY.blit(text2, [200, 200])

    text3 = font.render("Level 3", True, yellow)
    DISPLAY.blit(text3, [300,300])
    pygame.display.flip()
