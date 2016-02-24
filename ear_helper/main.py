import pygame
from pygame import mixer, display, event
from os import path
from time import sleep
from random import choice
import sys

notes_folder = path.dirname(path.abspath(__file__)) + '/notes/{note}.mp3'
current_note = ''

def play_note(note):
    running = True
    mixer.init()
    mixer.music.load(notes_folder.format(note=note))
    while running:
        mixer.music.play()
        sleep(3)
        running = False


times = int(raw_input('How many times: '))
acertos = 0
vezes = 0

display.set_mode((300, 100))
display.set_caption('text')
font = pygame.font.SysFont('Arial', 36)
text = font.render("Hello There", 1, (10, 10, 10))
textpos = text.get_rect()
textpos.centerx = background.get_rect().centerx
background.blit(text, textpos)

while times != 0:
    random_note = choice('abcdefg')
    play_note(random_note)
    continua = True
    while continua:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    note = 'a'
                    continua = False
                elif event.key == pygame.K_b:
                    note = 'b'
                    continua = False
                elif event.key == pygame.K_c:
                    note = 'c'
                    continua = False
                elif event.key == pygame.K_d:
                    note = 'd'
                    continua = False
                elif event.key == pygame.K_e:
                    note = 'e'
                    continua = False
                elif event.key == pygame.K_f:
                    note = 'f'
                    continua = False
                elif event.key == pygame.K_g:
                    note = 'g'
                    continua = False
                elif event.key == pygame.K_SPACE:
                    play_note(random_note)

    if note == random_note:
        acertos = acertos + 1
    else:
        print random_note
    times = times - 1
    vezes = vezes + 1

porcentagem = (100 * acertos) / vezes

#print 'Acertou %i de %i\n%d%% de aproveitamento.' % (acertos, vezes, porcentagem)
