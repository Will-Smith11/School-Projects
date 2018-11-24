import pygame
import sys
import time
import random
import Final_Project

def showScore(choice=1):
    SFont = pygame.font.SysFont('monaco', 32)
    Ssurf = SFont.render("Score  :  {0}".format(score), True, (0,0,0))
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (320, 100)
    playSurface.blit(Ssurf, Srect)


def main():
    global score,playSurface
 
    playSurface = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Snake Game")
    
    snakePos = [100, 50]
    snakeBody = [[100, 50], [90, 50], [80, 50]]
    foodPos = [400, 50]
    foodSpawn = True
    direction = 'RIGHT'
    changeto = ''
    score = 0
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                Final_Project.game_slection_screen()


            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    changeto = 'RIGHT'
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    changeto = 'LEFT'
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    changeto = 'UP'
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    changeto = 'DOWN'
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        if changeto == 'RIGHT' and direction != 'LEFT':
            direction = changeto
        if changeto == 'LEFT' and direction != 'RIGHT':
            direction = changeto
        if changeto == 'UP' and direction != 'DOWN':
            direction = changeto
        if changeto == 'DOWN' and direction != 'UP':
            direction = changeto

        if direction == 'RIGHT':
            snakePos[0] += 10
        if direction == 'LEFT':
            snakePos[0] -= 10
        if direction == 'DOWN':
            snakePos[1] += 10
        if direction == 'UP':
            snakePos[1] -= 10

        snakeBody.insert(0, list(snakePos))
        if snakePos == foodPos:
            foodSpawn = False
            score += 1
        else:
            snakeBody.pop()
        if foodSpawn == False:
            foodPos = [random.randrange(1, 800 // 10) * 10, random.randrange(1, 600 // 10) * 10]
            foodSpawn = True

        playSurface.fill((255,255,255))
       
        for pos in snakeBody:
            pygame.draw.rect(playSurface, (0,255,0), pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(playSurface, (165, 42, 42), pygame.Rect(foodPos[0], foodPos[1], 10, 10))

       
        if snakePos[0] >= 800 or snakePos[0] < 0:
            running = False
            Final_Project.game_slection_screen()

        if snakePos[1] >= 600 or snakePos[1] < 0:
            running = False
            Final_Project.game_slection_screen()

        for block in snakeBody[1:]:
            if snakePos == block:
                running = False
                Final_Project.game_slection_screen()
        showScore()
        pygame.display.flip()
        
        clock.tick(18)
