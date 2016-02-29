from pygame import mixer
from os import path
from random import choice

class Events:

    def __init__(self):
        self.notes_folder = path.dirname(path.abspath(__file__)) + '/notes/{note}.mp3'
        self.current_note = ''
        self.quantity = 0
        self.down_counter = 0
        self.hits = 0

    def set_up_training(self, quantity):
        self.quantity = quantity # quantity of times it will execute de training
        self.down_counter = quantity # counter till its finished the training
        self.hits = 0 # number of right choices
        self.play_random_note()

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
        if note == self.current_note:
            self.hits = self.hits + 1
        if self.down_counter != 0:
            self.play_random_note() # play next random note
        return self.current_note.upper()

    def calculate_result(self):
        return  (float)((self.hits * 100) / self.quantity)
