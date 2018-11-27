import pygame
import random
import Final_Project
import os
import data_base_fuctions

def showScore():
    font = pygame.font.SysFont('monaco', 32)
    text = font.render("Score  :  {0}".format(score), True, (0,0,0))
    location = text.get_rect()
    location.midtop = (80, 10)
    screen.blit(text, location)


def game_over_text():
    font = pygame.font.SysFont('monaco', 60 ,bold=True)
    text = font.render("GAME OVER! Your score was {0}".format(score), True,(255,0,0))
    location = text.get_rect()
    location.midtop = (400,100)
    screen.blit(text, location)


def game_over():
    mouse = Final_Project.Mouse()
    pygame.display.set_caption("Game Over")
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255,0,255))


    button = Final_Project.Enter_Box(400,400,"""click to add your score """)
    button2= Final_Project.Enter_Box(400,442,"""or to continue""")

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
                    endscreen = False
                    data_base_fuctions.dataBase_in(playerID.return_username(),"Snake",score)
                    Final_Project.game_slection_screen()
                    

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
    global score,screen
 
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Snake Game")
    background = pygame.Surface(screen.get_size())
    background = background.convert()
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
                game_over()


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
            foodPos = [random.randrange(1, 800 // 10)*10, random.randrange(1, 600 // 10)*10]
            foodSpawn = True

        screen.fill((255,255,255))
       
        for pos in snakeBody:
            pygame.draw.rect(screen, (0,255,0), pygame.Rect(pos[0], pos[1], 10, 10))
        
        pygame.draw.rect(screen, (165, 42, 42), pygame.Rect(foodPos[0], foodPos[1], 10, 10))

       
        if snakePos[0] >= 800 or snakePos[0] < 0:
            running = False
            game_over()

        if snakePos[1] >= 600 or snakePos[1] < 0:
            running = False
            game_over()

        for block in snakeBody[1:]:
            if snakePos == block:
                running = False
                game_over()
        
        showScore()
        pygame.display.flip()
        
        clock.tick(18)
