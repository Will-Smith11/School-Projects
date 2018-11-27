import pygame
import os
import random

pygame.init()
screen = pygame.display.set_mode((640,480))

def img(img=str):
    return os.path.join(os.path.dirname(os.path.dirname( __file__ )), 'pictures','{}'.format(img))

class Fly(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img("fly.png"))
        self.rect = self.image.get_rect()
        self.x_val = x
        self.y_val = y
    def update(self,):
        self.rect.x = self.x_val
        self.rect.y = self.y_val
        

class Mouse(pygame.sprite.Sprite):
    def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(img("cursor.png"))
            self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.center = pygame.mouse.get_pos()






def main():
    pygame.display.set_caption("Bug_killer")
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,255))

    fly = Fly(random.randint(50,750),random.randint(50,550))

    print_screen = pygame.sprite.Group(fly)

    clock = pygame.time.Clock()
    keepygameoing = True

    while keepygameoing:

        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepygameoing = False
        




        screen.blit(background,(0, 0))
        print_screen.clear(screen,background)
        print_screen.update()
        print_screen.draw(screen)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()

