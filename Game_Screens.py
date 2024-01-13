import pygame
import time 
import random


from config  import Variabile
from Player import Player
from config import Window
from config import Linkuri_text
from Muzica import Muzica_Fundal


click=False



def Play():
    run=True

    while run:
                
        Variabile.obstacle_count+=Variabile.clock.tick(60)
        Variabile.elapsed_time = time.time()-Variabile.start_time
        
        You_Lost_text=Variabile.FONT_LOSE.render("YOU LOSE",1,"#ebd198")

        if Variabile.obstacle_count>Variabile.obstacle_add_incc:
            for _ in range(3):
                obstacle_x=random.randint(0,Window.SCREEN_WIDTH-Variabile.obstacle_Width)
                obstacle=pygame.Rect(obstacle_x,-Variabile.obstacle_Height,Variabile.obstacle_Width,Variabile.obstacle_Height)
                Variabile.obstacles.append(obstacle)

            Variabile.obstacle_add_incc=max(30,Variabile.obstacle_add_incc-10)
            Variabile.obstacle_count=0


        Player.Movement()

        Player.Player_Clamping()

        key =pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            menu()

                
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False




        for obstacle in Variabile.obstacles[:]:
            obstacle.y+=Variabile.obstacle_vell
            if obstacle.y > Window.SCREEN_HEIGHT:
                Variabile.obstacles.remove(obstacle)
            elif obstacle.y+ Variabile.obstacle_Height >= Player.player.y and obstacle.colliderect(Player.player):
                Variabile.obstacles.remove(obstacle)
                Variabile.hit=True
                break


        if Variabile.hit:
            if Variabile.elapsed_time >Variabile.highest_score:
                Variabile.highest_score=Variabile.elapsed_time
            Variabile.screen.blit(You_Lost_text,(260,250))
            pygame.display.update()
            pygame.time.delay(2000)
            menu()       

        Player.draw(Variabile.elapsed_time,Variabile.obstacles,Variabile.highest_score)

    pygame.quit()

def menu():
    Variabile.start_time=time.time()
    Variabile.elapsed_time=0
    Variabile.hit=False
    Variabile.obstacle_count=0
    Variabile.obstacles=[]
    Player. player.center=(370,750)
    Player.angle=0

    click=False
    run=True
    while run:

        Sleight_text=Variabile.FONT_TITLE.render("Sleight",1,"#ebd198")
        Surprises_text=Variabile.FONT_TITLE.render("Surprises",1,"#ebd198")
        Nume_VladF=Variabile.FONT_NUME.render("Fraticiu Vlad",1,"#F1C568")
        Nume_VladR=Variabile.FONT_NUME.render("Raduica Vlad",0,"#F1C568")
        Variabile.screen.fill((0,0,0))
        Variabile.screen.blit(Variabile.Menu_Backround,(0,0))
        Variabile.screen.blit(Sleight_text,(230,110))
        Variabile.screen.blit(Surprises_text,(189,180))
        Variabile.screen.blit(Nume_VladF,(620,545))
        Variabile.screen.blit(Nume_VladR,(620,555))

        # Variabile.screen.blit(Variabile.Sleight_Surprises,(117.5,200))
        Variabile.clock.tick(60)

        button_1=Variabile.sprite_sheet_image_start.get_rect()
        button_1.center=(270,500)
        button_2=Variabile.sprite_sheet_image_quit.get_rect()
        button_2.center=(470,500)
        button_3=Variabile.sprite_sheet_image_links.get_rect()
        button_3.center=(70,530)

        mx,my=pygame.mouse.get_pos()

        if button_1.collidepoint((mx,my)):
            if click:
                if Variabile.hit==False:
                    Play()
        if button_2 .collidepoint((mx,my)):
            if click:
                pygame.quit()
        if button_3.collidepoint((mx,my)):
            if click:
                Links_Menu()

        click=False

        Variabile.screen.blit(Variabile.sprite_sheet_image_start,button_1)
        Variabile.screen.blit(Variabile.sprite_sheet_image_quit,button_2)
        Variabile.screen.blit(Variabile.sprite_sheet_image_links,button_3)

        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type== pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True
        pygame.display.update()

    pygame.quit()


def Links_Menu():

    click=False
    run=True

    while run:
        Variabile.screen.fill((152,156,175))

        button_1=Variabile.sprite_sheet_image_back_arrow.get_rect()
        button_1.center=(50,540)

        Variabile.screen.blit(Variabile.sprite_sheet_image_back_arrow,button_1)
        Variabile.screen.blit(Variabile.sprite_sheet_image_tree,(550,380))
        Variabile.screen.blit(Linkuri_text.text1,(10,10))
        Variabile.screen.blit(Linkuri_text.text2,(10,30))
        Variabile.screen.blit(Linkuri_text.text3,(10,50))
        Variabile.screen.blit(Linkuri_text.text4,(10,70))



        mx,my=pygame.mouse.get_pos()


        if button_1.collidepoint((mx,my)):
            if click:
                menu()
        
        click=False

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type== pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True
        pygame.display.update()

       
    pygame.quit()



    
