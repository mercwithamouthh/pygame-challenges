import pygame
pygame.init()

x = 400
y = 400

#colors
white = [255, 255, 255]
black = [0, 0, 0]
gray = [130, 130, 130]
yellow = (255,193,89)

#set up screen
DISPLAY = pygame.display.set_mode([x,y])
pygame.display.set_caption('Text on screen')

running = True

font = pygame.font.Font(None, 20)

font2 = pygame.font.Font(None, 50)

font3 = pygame.font.Font(None, 80)



while running:
    DISPLAY.fill(yellow)

    text = font.render("small", True, white)
    DISPLAY.blit(text, [100, 50])

    text2 = font2.render("medium", True, gray)
    DISPLAY.blit(text2, [100, 110])

    text3 = font3.render("large", True, black)
    DISPLAY.blit(text3, [100,200])
    pygame.display.flip()
