""""will's password generator + storage system"""
import sqlite3 as sq
import random
import string
import pygame
import hashlib


pygame.init()
screen = pygame.display.set_mode((800, 600))
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 25)


def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()


class Password_Box:
    def __init__(self, text=''):
        self.rect = pygame.Rect(220, 130, 100, 30)
        self.color = color_inactive
        self.text = ""
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        
            self.color = color_active if self.active else color_inactive
        
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    dataBase_in()
                    
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)
    def return_password(self):
        return self.text

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)


class Username_Box:

    def __init__(self, text = ''):
        self.rect = pygame.Rect(220, 100, 100, 30)
        self.color = color_inactive
        self.text = ""
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
      
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        
            self.color = color_active if self.active else color_inactive
        
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)
    
    def return_username(self):
        return self.text

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
        


class Mouse(pygame.sprite.Sprite):
    def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((30,30))
            self.image.fill((255,0,0))
            self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.center = pygame.mouse.get_pos()



class Enter_Box(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,50))
        self.image.fill((255,0,255))
        self.rect = self.image.get_rect()
        self.rect.centerx = 255
        self.rect.centery = 255
        self.font =  pygame.font.SysFont("areal",30)
        self.text = "press enter to continue"
    def update(self):
        self.image = self.font.render(self.text,1,(255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = ((255,255))


class Label(pygame.sprite.Sprite):
    def __init__(self,x,y,text=''):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("areal",30)
        self.text = text
        self.center = (x,y)

    def update(self):
        self.image = self.font.render(self.text,1,(255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = self.center




username_box = Username_Box().return_username()
password_box = Password_Box().return_password()

screen_us = Username_Box()
screen_pw = Password_Box()
 
def game_intro():
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    
    enter = Enter_Box()
    mouse_loc = Mouse()

    
    
    
    label1 = Label(100,110,"your username")
    label2 = Label(100,140,"your password")
    print_to_screen = [screen_pw, screen_us]
    all_labels = pygame.sprite.Group(label1, label2, enter,mouse_loc)
    
    continue_box = pygame.sprite.Group(enter)

    intro = True
    clock = pygame.time.Clock()
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                if pygame.sprite.spritecollide(mouse_loc,continue_box, False): 
                    dataBase_in()
                    intro = False
                    main()
                                   
            
            for box in print_to_screen:
                box.handle_event(event)

        largeText = pygame.font.Font('freesansbold.ttf',30)
        TextSurf, TextRect = text_objects("Will's Cool game in the process", largeText)
        TextRect.center = ((400),(300))
        

        for box in print_to_screen:
            box.update()
        
        screen.fill((30,30,30))
        
        for box in print_to_screen:
            box.draw(screen)
        

        all_labels.clear(screen,background)
        all_labels.update()
        all_labels.draw(screen)   
        screen.blit(TextSurf, TextRect)
        
        
    
        pygame.display.flip()
        clock.tick(60)



def main():
    clock = pygame.time.Clock()
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255,0,255))

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            

        screen.blit(background,(0,0))
        pygame.display.flip()
        clock.tick(30)
  
  
    


""" Second part of project"""



def dataBase_in():

    db = sq.connect('Game_Username_and_Password.db')
    c = db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS player_data(username, password)")
    c.execute("INSERT INTO player_data(username, password)VALUES(:username, :password)",
            {'username':username_box,'password':password_box})

    db.commit()




def dataBase_out():

    db = sq.connect('Password_Bank.db')
    c = db.cursor()
    w = 0
    stop = False
    while stop == False:
        try:
            c.execute("SELECT * FROM"+" "+username)
            data = c.fetchall()[w][0]
            
        except: 
            if w == 500:
                print("\n\nError... no password found for the website "+" "+values.request_website_name())
                stop == True
        
        if data != request_website:
            w = w+1
        
        if data == request_website:
            c.execute("SELECT * FROM"+" "+username)
            print("\n"+c.fetchall()[w][1]+" "+"is your password for"+values.request_website_name())
            stop = True
    db.commit()





if __name__ =="__main__":
    game_intro()
 








