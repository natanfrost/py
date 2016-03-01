from os import path

def jdefault(o):
    return o.__dict__

class Result:
    """docstring for Result"""
    def __init__(self, quantity, hits):
        self.quantity = quantity
        self.hits = hits
        self.final_grade = (float)((hits * 100) / quantity)
