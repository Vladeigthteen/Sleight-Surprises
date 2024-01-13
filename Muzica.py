import pygame


def Muzica_Fundal():
    
    music=pygame.mixer.music.load('Music/main music.mp3')
    music=pygame.mixer.music.set_volume(0.15)
    pygame.mixer.music.play(-1)

def Efect_Intoarcere():
    truning_effect=pygame.mixer.Sound('Music/turn efect.wav')