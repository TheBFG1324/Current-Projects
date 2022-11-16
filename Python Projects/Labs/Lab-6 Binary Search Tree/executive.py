# executive.py
from poke import Poke


class Executive:
    def __init__(self, input_file):
        file = open(input_file)
        self.poke_matrix = []
        for line in file:
            new_poke = Poke(line.split())
            self.poke_matrix.append(new_poke)
