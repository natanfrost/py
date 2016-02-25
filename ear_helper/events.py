from pygame import mixer
from os import path
from random import choice

class Events:

    def __init__(self, quantity, first_note):
        self.notes_folder = path.dirname(path.abspath(__file__)) + '/notes/{note}.mp3'
        self.current_note = ''
        self.hits = 0
        self.quantity = quantity
        self.down_counter = quantity
        self.play_note(first_note)

    def play_note(self, note):
        mixer.init()
        mixer.music.load(self.notes_folder.format(note=note))
        mixer.music.play()
        if self.current_note != note:
            self.current_note = note

    def play_random_note(self):
        note = choice('abcdefg')
        self.play_note(note)

    def check_note(self, note):
        self.down_counter = self.down_counter - 1 # decrementa o contador que eh quem controla a finalizacao do processo
        self.play_random_note() # toca proxima nota
        if note == self.current_note:
            self.hits = self.hits + 1
        return self.current_note

    def calculate_result(self):
        return  (float)((self.hits * 100) / self.quantity)
