"""Docstring."""
from datetime import datetime


def jdefault(o):
    """TODO docstring."""
    return o.__dict__


class Result:
    """docstring for Result."""

    def __init__(self, quantity, hits, logest_streak):
        """Constructor."""
        self.quantity = quantity
        self.hits = hits
        self.final_grade = (float)((hits * 100) / quantity)
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M')
        self.longest_streak = logest_streak
