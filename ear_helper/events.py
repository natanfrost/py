"""Docstring."""
from pygame import mixer
from os import path
from random import choice
import xml.etree.ElementTree as ET


class Events:
    """Here lies the main methods used in main form."""

    def __init__(self):
        """Constructor of class."""
        self.notes_folder = path.dirname(
            path.abspath(__file__)) + '/notes/{note}.mp3'
        self.current_note = ''
        self.quantity = 0
        self.down_counter = 0
        self.hits = 0
        self.longest_streak = 0
        self.actual_streak = 0

    def set_up_training(self, quantity):
        """Set up to start training."""
        # quantity of times it will execute the training
        self.quantity = quantity
        self.down_counter = quantity  # counter till its finished the training
        self.hits = 0  # number of right choices
        self.play_random_note()

    def play_note(self, note):
        """Play a specific chord."""
        mixer.init()
        mixer.music.load(self.notes_folder.format(note=note))
        mixer.music.play()
        if self.current_note != note:
            self.current_note = note

    def define_random_priority(self):
        """Define the random priority to choose a chord."""
        tree = ET.parse(path.dirname(
            path.abspath(__file__)) + '/estatistic.xml')
        root = tree.getroot()
        result = ''
        for child in root:
            chord = child.attrib['name']
            for erros in child.iter('wrong_times'):
                wrong_times = int(erros.text)
                if wrong_times == 0:
                    result += chord
                else:
                    result += chord * wrong_times
        return result

    def play_random_note(self):
        """Play a random chord."""
        note = choice(self.define_random_priority())
        self.play_note(note)

    def check_note(self, note):
        """Check if the note that user chooose is right."""
        # decrementa o contador que eh quem controla a finalizacao do processo
        self.down_counter = self.down_counter - 1
        if note == self.current_note:
            self.hits = self.hits + 1
            self.actual_streak = self.actual_streak + 1
            if self.actual_streak > self.longest_streak:
                self.longest_streak = self.actual_streak
        else:
            self.actual_streak = 0
        return self.current_note.upper()

    def calculate_result(self):
        """Calculate the result of the training session."""
        return (float)((self.hits * 100) / self.quantity)
