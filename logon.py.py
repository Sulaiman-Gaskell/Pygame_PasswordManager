import pygame
from pygame.locals import *
import pygame.font
import subprocess

class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()
        self.surf = pygame.Surface((50, 30))
        
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
 

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((200, 400))

my_font = pygame.font.SysFont('Comic Sans MS', 10)
lText = "Login"
loginS = my_font.render(lText, True, (0,0,0))
login_rect = loginS.get_rect()
login_rect.center = (100,165)
#lClick = pygame.rect(75,150,50,30)

qText = "Quit"
quitS = my_font.render(qText, True, (0,0,0))
quit_rect = quitS.get_rect()
quit_rect.center = (100,215)
#qClick = pygame.rect(75,200,50,30)

login = Square()
quit = Square()

run = True

while run:
    screen.blit(login.surf,(75,150))
    screen.blit(quit.surf,(75,200))
    screen.blit(loginS, login_rect)
    screen.blit(quitS,quit_rect)

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()

            if login_rect.collidepoint(mouse_pos):
                go = 0
                screen.fill((0,0,0))

            if quit_rect.collidepoint(mouse_pos):
                go = 1
                run = False

        elif event.type == QUIT:
            run = False


    pygame.display.flip()
            
if go == 1:
    print()
else:
    run = True
    while run:
        pygame.display.flip()

