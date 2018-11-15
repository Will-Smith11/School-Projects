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


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
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
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)
    def password(self):
        "yeet"

    def username(self):
        "yeet"
    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)




class Label(pygame.sprite.Sprite):
    def __init__(self,x,y,text=''):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("areal",30)
        self.text = text
        self.center = (x,y)

    def update(self):
        self.image = self.font.render(self.text,1,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center



def game_intro():
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,255))
    input_box1 = InputBox(220, 100, 100, 30)
    input_box2 = InputBox(220, 130, 100, 30)
    label1 = Label(100,110,"your username")
    label2 = Label(100,140,"your password")
    print_to_screen = [input_box1, input_box2]
    all_labels = pygame.sprite.Group(label1, label2)
    
    intro = True
    clock = pygame.time.Clock()
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
        clock.tick(15)



def main():
    clock = pygame.time.Clock()
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,0))

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            

        screen.blit(background,( 0,0))
        pygame.display.flip()
        clock.tick(30)
  
  
  #  username = input("what is your name?")
   # username = username.lower()
    #values = Website_Data_Input()
    #values.pw_generator(int(input("how many digits do you want the password to be?")))
    #values.set_webname(input("what is the website you want a password generated for"))
    #request = input("do you want to get a password for a website? yes, no")
    #request = request.lower()
    #if request == ("yes"):
     #   request_website = values.request_website_pw(input("what website do you want a password for?"))
      #  dataBase_out()
    #else:
     #   dataBase_in()


""" Second part of project"""




# add encription to
class Website_Data_Input:
    password = ""
    website_name = ""
    name = ""
    request_website = ""
    def __init__(self, password = None, website_name = None, name = "error", request_website = "google"):
        self.password = password
        self.website_name = website_name
        self.name = name
        self.request_website = request_website
    def set_name(self, name):
        self.name = name
    def giv_name(self):
        return self.name

    def pw_generator(self,size=20, chars=string.ascii_uppercase + string.digits + string.hexdigits+string.ascii_lowercase):
        self.password =  ''.join(random.choice(chars) for _ in range(size))

    def give_password(self):
        return self.password

    def set_webname(self, website):
        self.website_name = website.lower()

    def give_website(self):
        return self.website_name
    def request_website_pw(self,request_website):
        self.request_website = request_website
        return self.request_website
        
    def request_website_name(self):
        return self.request_website

def dataBase_in():
    w = 0
    db = sq.connect('Password_Bank.db')
    c = db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS"+" "+username+"(website, password)")
    stop = False
    while stop == False:
        
        try:
            c.execute("SELECT * FROM"+" "+username)
            check = c.fetchall()[w][0]

        
        except:
            
            if w == 500:
                
                c.execute("INSERT INTO"+" "+username+" "+"(website, password) VALUES(:website, :password)",
                        {'website':values.give_website(), 'password':values.give_password()})
                
                print(values.give_password()+" "+ "is your new password for"+" "+values.give_website())
                stop = True
        
        try:
            if check != values.give_website():
                w = w +1

            if check == values.give_website():
                print("Website Password already in DB")
                stop = True
        except:
            c.execute("INSERT INTO"+" "+username+" "+"(website, password) VALUES(:website, :password)",
                        {'website':values.give_website(), 'password':values.give_password()})
            print(values.give_password()+" "+ "is your new generated password for"+" "+values.give_website())
            stop = True
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
 








