from pygame import mixer
from os import path
from random import choice

notes_folder = path.dirname(path.abspath(__file__)) + '/notes/{note}.mp3'
current_note = ''

def play_note(self):
    mixer.init()
    mixer.music.load(notes_folder.format(note='a'))
    mixer.music.play()
