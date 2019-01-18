"""Wills Space invaders game attempt"""
import pygame
import random
import Final_Project
import os
import data_base_fuctions
import time



pygame.init()
screen = pygame.display.set_mode((800,600))



def img(img=str):
    return os.path.join(os.path.dirname(os.path.dirname( __file__ )), 'pictures','{}'.format(img))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(img("player.png"))
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 560
    def update(self):       
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x +=8
        if keys[pygame.K_LEFT]:
            self.rect.x -=8

        if self.rect.x >785:
            self.rect.x = 785
        if self.rect.x < 15:
            self.rect.x = 15
    
    def get_pos_x(self):
        return self.rect.x


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(img("bullet.png"))
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 9


class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(img("alien.png"))
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.x += 9
        if self.rect.x > 780:
            self.rect.y += 100
            self.rect.x = 20
    def get_pos(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y


class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(img("bomb.png"))
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.y += 9

def showScore():
    font = pygame.font.SysFont('monaco', 32)
    text = font.render("Score  :  {0}".format(score), True, (255,255,255))
    location = text.get_rect()
    location.midtop = (80, 10)
    screen.blit(text, location)


def game_over_text():
    font = pygame.font.SysFont('monaco', 60, bold=True)
    text = font.render("GAME OVER! Your score was {0}".format(score), True,(255,0,0))
    location = text.get_rect()
    location.midtop = (400,100)
    screen.blit(text, location)


def game_over():
    mouse = Final_Project.Mouse()
    pygame.display.set_caption("Game Over")
    
    button = Final_Project.Enter_Box(400,400,"""click to add your score """)
    button2= Final_Project.Enter_Box(400,442,"""your name needs to be 3 characters""")

    all_sprits = pygame.sprite.Group(mouse)
    button_spirte = pygame.sprite.Group(button,button2)
    clock = pygame.time.Clock()
    
    playerID = Final_Project.Username_Box(300,250,300,50)
    print_to_screen = [playerID]
    
    endscreen = True
    while endscreen:
        screen.blit(background,(0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endscreen = False
                Final_Project.game_slection_screen()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.sprite.spritecollide(mouse,button_spirte, False):
                    if playerID.has_val:
                        endscreen = False
                        data_base_fuctions.dataBase_in(playerID.return_username(),"Aliens",score)
                        Final_Project.game_slection_screen()
                    else:
                        pass

            for box in print_to_screen:
                box.handle_event(event)


        for box in print_to_screen:
            box.update()
        
        
        for box in print_to_screen:
            box.draw(screen)


        clock.tick(30)
        
        all_sprits.clear(background,screen)
        button_spirte.clear(background,screen)
        all_sprits.update()
        button_spirte.update()
        button_spirte.draw(screen)
        all_sprits.draw(screen)
        
        game_over_text()
        
        pygame.display.flip()
          

def main():
    global score, background
    pygame.display.set_caption("Space Invaders")
    background = pygame.image.load(img("Space_background.jpg"))
    background.get_rect()

    reload_time = pygame.time.get_ticks()

    score = 0
    player = Player()
    all_sprites = pygame.sprite.Group()
    bullet_list = pygame.sprite.Group()
    alien_list = pygame.sprite.Group()
    bomb_list = pygame.sprite.Group()
    all_sprites.add(player)
    
    
    clock = pygame.time.Clock()
    keepygameoing = True
    while keepygameoing:
        current_time = pygame.time.get_ticks()
        

        
        screen.blit(background,(0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepygameoing = False
                
            if current_time - reload_time > 600:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    bullet = Bullet()
                
                    bullet.rect.x = player.rect.x
                    bullet.rect.y = player.rect.y
                
                    all_sprites.add(bullet)
                    bullet_list.add(bullet)
                    reload_time = current_time
                
            
        if score <=75:
            if random.randint(0,30) == 5:
                alien = Alien()
                
                alien.rect.x = 20
                alien.rect.y = 20

                all_sprites.add(alien)
                alien_list.add(alien)
        elif score >=76 and score <=140:
            if random.randint(0,25) == 5:
                alien = Alien()
                
                alien.rect.x = 20
                alien.rect.y = 20

                all_sprites.add(alien)
                alien_list.add(alien)

        elif score >= 140:
            if random.randint(0,20) == 5:
                alien = Alien()
                
                alien.rect.x = 20
                alien.rect.y = 20

                all_sprites.add(alien)
                alien_list.add(alien)



        if random.randint(0,35) == 5:
            bomb = Bomb()
            try:
                for x in alien_list.sprites():
                    x = 0
                    x += 1
                rand = random.randint(0,x)
                randalien = alien_list.sprites()[rand]
                bomb.rect.x = randalien.get_pos()
                all_sprites.add(bomb)
                bomb_list.add(bomb)  
            except:
                pass
        
        all_sprites.update()

        
        for enemy in alien_list.sprites():
            
            location = pygame.sprite.spritecollide(player,alien_list,True)
            
            for hit in location:
                game_over()
                keepygameoing = False
               
        

        for bullet in bullet_list:
 
            block_hit_list = pygame.sprite.spritecollide(bullet, alien_list, True)

            for block in block_hit_list:
                bullet_list.remove(bullet)
                all_sprites.remove(bullet)
                score += 1
            if bullet.rect.y < -10:
                bullet_list.remove(bullet)
                all_sprites.remove(bullet)

        for bomb in bomb_list:
            bomb_hit_list = pygame.sprite.spritecollide(player, bomb_list,True)

            for explode in bomb_hit_list:
                bomb_list.remove(bomb)
                all_sprites.remove(bomb)
             
                game_over()
                keepygameoing = False
                

            if bomb.rect.y > 600:
                bomb_list.remove(bomb)
                all_sprites.remove(bomb)        
       
        showScore()
        clock.tick(30)
        all_sprites.draw(screen)
        pygame.display.flip()






