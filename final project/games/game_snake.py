""""Will's snake game for final project"""
import pygame
import random
import time


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 300
    
    def update(self):       
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x +=5
        if keys[pygame.K_LEFT]:
            self.rect.x -=5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        if self.rect.x >800:
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = 800
       
        if self.rect.y > 600:
            self.rect.y = 0
        if self.rect.y <0:
            self.rect.y = 600

                    






pygame.init()
screen = pygame.display.set_mode((800,600))

def main():
    pygame.display.set_caption("snake game")
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,255))

    snake = Snake()

    allSprites = pygame.sprite.Group(snake)

    clock = pygame.time.Clock()
    keepygameoing = True

    while keepygameoing:

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepygameoing = False
        screen.blit(background,(0, 0))

        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()


