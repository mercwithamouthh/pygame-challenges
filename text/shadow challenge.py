import pygame
pygame.init()

x = 400
y = 400

#colors
white = [255, 255, 255]
black = [0, 0, 0]
gray = [130, 130, 130]

#set up screen
DISPLAY = pygame.display.set_mode([x,y])
pygame.display.set_caption('Text on screen')

running = True

font = pygame.font.Font(None, 72)
#need to add a font variable

while running:
    DISPLAY.fill(black)

    text2 = font.render("Shadow", True, gray)
    DISPLAY.blit(text2, [102, 102])

    text = font.render("Shadow", True, white)
    DISPLAY.blit(text, [100, 100])

    pygame.display.flip()