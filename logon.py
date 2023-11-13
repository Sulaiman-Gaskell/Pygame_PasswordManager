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
lText = 'Login'
loginS = my_font.render(lText, True, (0,0,0))
login_rect = loginS.get_rect()
login_rect.center = (100,165)


qText = 'Quit'
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
    f = open('U+P.txt','a')


    nScreen = pygame.display.set_mode((800, 600))
    anotherFont = pygame.font.SysFont('Comic Sans MS', 30)

    uText = 'Username:'
    usernameS = anotherFont.render(uText, True, (255,255,255))
    username_rect = usernameS.get_rect()
    username_rect.center = (400,65)

    pText = 'Password:'
    passwordS = anotherFont.render(pText, True,(255,255,255))
    password_rect = passwordS.get_rect()
    password_rect.center = (400,215)


    showAll = Square()
    sText = 'Show all:'
    showAllS = anotherFont.render(sText, True, (255,255,255))
    showAll_rect = showAllS.get_rect()
    showAll_rect.center = (400, 400)

    username = ""
    password = ""
    username_box = pygame.Rect(300, 100, 200, 40)
    password_box = pygame.Rect(300, 250, 200, 40)
    color_inactive = pygame.Color('white')
    color_active = pygame.Color('green')
    color = color_inactive
    active = None

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
    
                    if showAll_rect.collidepoint(mouse_pos):
                        print(open('U+P.txt').read())
                    
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if username_box.collidepoint(event.pos):
                        active = username_box
                        color = color_active
                    elif password_box.collidepoint(event.pos):
                        active = password_box
                        color = color_active
                    else:
                        active = None
                        color = color_inactive

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if active == username_box:
                            print('Username:', username)
                            f.write(username + ', ')
                        else:
                            print('Password:',password)
                            f.write(password + '\n')
                        username = ""
                        password = ""
                    elif event.key == pygame.K_BACKSPACE:
                        if active == username_box:
                            username = username[:-1]
                        else:
                            password = password[:-1]
                    else:
                        if active == username_box:
                            username += event.unicode
                        else:
                            password += event.unicode

   
        screen.fill((0, 0, 0))

      
        txt_surface_username = anotherFont.render(username, True, color)
        txt_surface_password = anotherFont.render('*' * len(password), True, color)
        
        username_box.w = max(200, txt_surface_username.get_width() + 10)
        password_box.w = max(200, txt_surface_password.get_width() + 10)
        
        nScreen.blit(txt_surface_username, (username_box.x + 5, username_box.y + 5))
        nScreen.blit(txt_surface_password, (password_box.x + 5, password_box.y + 5))
        nScreen.blit(usernameS, username_rect)
        nScreen.blit(passwordS, password_rect)
        nScreen.blit(showAllS, showAll_rect)
        
        pygame.draw.rect(screen, color, username_box, 2)
        pygame.draw.rect(screen, color, password_box, 2)

        pygame.display.flip()
    


 
