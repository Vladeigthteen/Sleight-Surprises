import pygame
import time

pygame.font.init()

class Window:
    SCREEN_WIDTH=735
    SCREEN_HEIGHT=575


class Variabile:

    highest_score=0


    start_time=time.time()
    elapsed_time=0


    obstacle_add_incc=2000
    obstacle_count=0
    obstacles=[]
    obstacle_vell=3
    obstacle_Width=10
    obstacle_Height=20
    hit=False

    FONT=pygame.font.Font("Fonts/Pixel_Font.TTF",20)
    FONT_TITLE=pygame.font.Font("Fonts/Pixel_Font.TTF",50)
    FONT_LOSE=pygame.font.Font("Fonts/Pixel_Font.TTF",30)
    FONT_NUME=pygame.font.Font("Fonts/Pixel_Font.TTF",10)
    clock= pygame.time.Clock()
    Backround=pygame.transform.scale(pygame.image.load('Backround.png'),(Window.SCREEN_WIDTH,Window.SCREEN_HEIGHT))
    screen = pygame.display.set_mode((Window.SCREEN_WIDTH,Window.SCREEN_HEIGHT),pygame.RESIZABLE)
    icon= pygame.image.load('Assets/santa-claus.png')
    Menu_Backround=pygame.transform.scale(pygame.image.load('Menu_BG.png'),(Window.SCREEN_WIDTH,Window.SCREEN_HEIGHT))
    Sleight_Surprises=pygame.transform.scale(pygame.image.load('Assets/Sleight_Surprises.png'),(517.5,120.5))
    You_Lost=pygame.transform.scale(pygame.image.load('Assets/You Lost!.png'),(400,400))
    sprite_sheet_image_start = pygame.transform.scale(pygame.image.load('Play_Button.png').convert_alpha(),(70,70))
    sprite_sheet_image_quit = pygame.transform.scale(pygame.image.load('Quit_Button.png').convert_alpha(),(70,70))
    sprite_sheet_image_links=pygame.transform.scale(pygame.image.load('Links_Button.png').convert_alpha(),(100,100))
    sprite_sheet_image_back_arrow=pygame.transform.scale(pygame.image.load('Back_arrow.png').convert_alpha(),(50,50))
    sprite_sheet_image_tree=pygame.transform.scale(pygame.image.load('Christmas Tree.png').convert_alpha(),(200,200))



class Linkuri_text:
    FONT=pygame.font.Font("Fonts/Pixel_Font.TTF",16)
    text1=FONT.render("- https://void1gaming.itch.io/christmas-music-pack",1,"#ebd198")
    text2=FONT.render("- https://www.flaticon.com/search?word=christmas",1,"#ebd198")
    text3=FONT.render("- https://brunizitu.itch.io/save-the-christmas",1,"#ebd198")
    text4=FONT.render("- https://docs.python.org/3/library/time.html",1,"#ebd198")


class Player_config:
    PLAYER_WIDTH=3
    PLAYER_HEIGHT=1.5
    PLAYER_VEL=13


def Display():
    pygame.display.set_icon(Variabile.icon)
    pygame.display.set_caption('Sleight Surprises')
    Variabile.Backround
    Variabile.screen 
