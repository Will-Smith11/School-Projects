"""Wills Space invaders game attempt"""
import pygame
import random
import Final_Project
import os


pygame.init()
screen = pygame.display.set_mode((800,600))




    

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname( __file__ )), 'pictures','player.png')).convert_alpha()
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
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'pictures','bullet.png')).convert_alpha()
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 10

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'pictures','alien.png')).convert_alpha()
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.x += 5
        if self.rect.x > 780:
            self.rect.y += 100
            self.rect.x = 20
    def get_pos(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'pictures','bomb.png')).convert_alpha()
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.y += 7

def showScore():
    font = pygame.font.SysFont('monaco', 32)
    text = font.render("Score  :  {0}".format(score), True, (0,0,0))
    location = text.get_rect()
    location.midtop = (80, 10)
    screen.blit(text, location)


def main():
    global score
    pygame.display.set_caption("Space Invaders")
    background = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname( __file__ )), 'pictures','Space_background.jpg')).convert_alpha()
    background.get_rect()

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

        
        screen.blit(background,(0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepygameoing = False
                Final_Project.game_slection_screen()
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                bullet = Bullet()
            
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
            
                all_sprites.add(bullet)
                bullet_list.add(bullet)
            

        if random.randint(0,30) == 5:
            alien = Alien()
            
            alien.rect.x = 20
            alien.rect.y = 20

            all_sprites.add(alien)
            alien_list.add(alien)

        if random.randint(0,20) == 5:
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
                keepygameoing = False
                Final_Project.game_slection_screen()
        

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
                keepygameoing = False
                Final_Project.game_slection_screen()

            if bomb.rect.y > 600:
                bomb_list.remove(bomb)
                all_sprites.remove(bomb)        
       
        showScore()
        clock.tick(30)
        all_sprites.draw(screen)
        pygame.display.flip()






