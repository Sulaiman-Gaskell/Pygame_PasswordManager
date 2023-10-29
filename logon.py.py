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


qText = "Quit"
quitS = my_font.render(qText, True, (0,0,0))
quit_rect = quitS.get_rect()
quit_rect.center = (100,215)


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
                run = False

            if quit_rect.collidepoint(mouse_pos):
                go = 1
                run = False

        elif event.type == QUIT:
            run = False


    pygame.display.flip()
            
if go == 1:
    print()
else:
    nScreen = pygame.display.set_mode((800, 600))
    anotherFont = pygame.font.SysFont('Comic Sans MS', 30)

    uText = "Username"
    usernameS = anotherFont.render(uText, True, (255,255,255))
    username_rect = loginS.get_rect()
    username_rect.center = (340,165)

    username = ""
    input_box = pygame.Rect(300, 230, 200, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False


    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:  
                        print("Username:", username)#######
                        username = ""  
                    elif event.key == pygame.K_BACKSPACE:  
                        username = username[:-1]
                    else:
                        username += event.unicode

        
        nScreen.fill((0, 0, 0))

        
        txt_surface = my_font.render(username, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        nScreen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        nScreen.blit(usernameS, username_rect)
        pygame.draw.rect(nScreen, color, input_box, 2)

        pygame.display.flip()
    


 
