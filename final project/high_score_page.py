import pygame
import Final_Project
import data_base_fuctions


screen = pygame.display.set_mode((800, 600))

background = pygame.image.load(Final_Project.img("Space_background.jpg"))
background.get_rect()


class Ranking_display(pygame.sprite.Sprite):
    def __init__(self, x, y, color, game):
        super().__init__()
        grab_info = data_base_fuctions.Give_Highscores(game)

        self.font = pygame.font.SysFont('monaco', 30)
        try:
            self.text = (f"Username: {grab_info.give_name(game)} --- Score: {grab_info.give_score(game)}")
    
        except:
            self.text = "error getting data"
        
        self.center = (x, y)
        self.color = color

    def update(self):
        self.image = self.font.render(self.text, 1, (self.color))
        self.rect = self.image.get_rect()
        self.rect.center = self.center




def game_over_text():
    font = pygame.font.SysFont('monaco', 60, bold=True)
    text = font.render("HIGH SCORES",True,(255,0,0))
    location = text.get_rect()
    location.midtop = (400, 50)
    screen.blit(text, location)


def main():
    mouse = Final_Project.Mouse()
    pygame.display.set_caption("Game Over")
    button = Final_Project.Enter_Box(400, 550, "Return to home page")



    high_score_aliens = Ranking_display(200,100,(0,255,255),"Aliens")
    high_score_snake = Ranking_display(600,100,(0,255,255),"Snake")


    all_sprits = pygame.sprite.Group( mouse, high_score_aliens, high_score_snake)
    button_spirte = pygame.sprite.Group(button)
    clock = pygame.time.Clock()


    endscreen = True
    while endscreen:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endscreen = False
                Final_Project.game_slection_screen()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.sprite.spritecollide(mouse, button_spirte, False):
                    endscreen = False
                    Final_Project.game_slection_screen()
                   

        clock.tick(30)

        all_sprits.clear(background, screen)
        button_spirte.clear(background, screen)
        all_sprits.update()
        button_spirte.update()
        button_spirte.draw(screen)
        all_sprits.draw(screen)

        game_over_text()

        pygame.display.flip()

