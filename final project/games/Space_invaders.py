"""Wills Space invaders game attempt"""
import pygame
import random
import Final_Project
pygame.init()
screen = pygame.display.set_mode((800,600))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("/Users/davesmith/Desktop/Python/final school project/School-Projects-master 2/final project/pictures/player.jpeg")
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 560
    def update(self):       
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x +=7
        if keys[pygame.K_LEFT]:
            self.rect.x -=7

        if self.rect.x >785:
            self.rect.x = 785
        if self.rect.x < 15:
            self.rect.x = 15
    
    def get_pos_x(self):
        return self.rect.x

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("/Users/davesmith/Desktop/Python/final school project/School-Projects-master 2/final project/pictures/bullet.jpeg")
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 10

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("/Users/davesmith/Desktop/Python/final school project/School-Projects-master 2/final project/pictures/alien.png")
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.x += 5
        if self.rect.x > 780:
            self.rect.y += 20
            self.rect.x = 20
    def get_pos(self):
        return self.rect.x

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("/Users/davesmith/Desktop/Python/final school project/School-Projects-master 2/final project/pictures/bomb.png")
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.y += 10

def main():
    pygame.display.set_caption("Space Invaders")
    background = pygame.image.load("/Users/davesmith/Desktop/Python/final school project/School-Projects-master 2/final project/pictures/Space_background.jpg")
    background.get_rect()

    player = Player()

    
    all_sprites = pygame.sprite.Group()
    
    bullet_list = pygame.sprite.Group()
    
    alien_list = pygame.sprite.Group()

    bomb_list = pygame.sprite.Group()

    all_sprites.add(player)

    

    clock = pygame.time.Clock()
    keepygameoing = True
    while keepygameoing:

        clock.tick(120)
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

        if random.randint(0,30) == 1:
            bomb = Bomb()
            try:
                bomb.rect.x = alien.get_pos()
            except:
                pass
            all_sprites.add(bomb)
            bomb_list.add(bomb)

        
        all_sprites.update()




        for bullet in bullet_list:
 
            block_hit_list = pygame.sprite.spritecollide(bullet, alien_list, True)

            for block in block_hit_list:
                bullet_list.remove(bullet)
                all_sprites.remove(bullet)
            
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
        
        all_sprites.draw(screen)

        pygame.display.flip()






