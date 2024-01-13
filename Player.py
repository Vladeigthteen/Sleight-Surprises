import pygame
from config import Variabile
from config import Window
from config import Player_config

pygame.font.init()


class Player:

    sprite_sheet_image = pygame.transform.scale(pygame.image.load('Assets/player.png').convert_alpha(),(138,80))
    player = sprite_sheet_image.get_rect()
    player.center=(370,750)

    def fliped_player(angle):
        return pygame.transform.flip(Player.sprite_sheet_image,angle,0)
    
    angle =0
    def draw(elasped_time,obstacles,highest_score):
        pygame.display.update()
        Variabile.screen.blit(Variabile.Backround,(0,0))
        time_text = Variabile.FONT.render(f"Time: {round(elasped_time)}s",1,"#ebd198")

        highest_score_text= Variabile.FONT.render(f"Highest Score: {round(highest_score)}s",1,"#ebd198")
        


        Variabile.screen.blit(Player.sprite_sheet_image,Player.player)
        Variabile.screen.blit(Variabile.Backround,(0,0)) 
        player_fliped=Player.fliped_player(Player.angle)
        Variabile.screen.blit(player_fliped,Player.player)
        for obstacle in obstacles:
            pygame.draw.rect(Variabile.screen,"white",obstacle)
        

        Variabile.screen.blit(highest_score_text,(450,20))

        Variabile.screen.blit(time_text,(10,20))
        

    def Player_Clamping():
        Player.player.clamp_ip(pygame.Rect(0, 0, Window.SCREEN_WIDTH - 6, Window.SCREEN_HEIGHT - 20))
    


    def Movement():

        key =pygame.key.get_pressed()
        if key[pygame.K_a]==True or key[pygame.K_LEFT]==True:
            Player.player.move_ip(-Player_config.PLAYER_VEL,0)
            Player.angle=0
            
        if key[pygame.K_d]==True or key[pygame.K_RIGHT]==True:
            Player.player.move_ip(Player_config.PLAYER_VEL,0)
            Player.angle=1
    
        if key[pygame.K_s]==True or key[pygame.K_DOWN]==True:
            Player. player.move_ip(0,Player_config.PLAYER_VEL)
        
        if key[pygame.K_w]==True or key[pygame.K_UP]==True:
            Player.player.move_ip(0,-Player_config.PLAYER_VEL)