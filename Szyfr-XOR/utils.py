"""
Potrzebne parametry i funkcje pomocnicze
"""

class Utils:

    def __init__(self):
        self.dictionary_small_letters = {chr(i): i - 97 for i in range(97, 123)}
        self.dictionary_big_letters = {chr(i): i - 65 for i in range(65, 91)}

    def read(self, file: str) -> str:
        with open(file, "r") as p:
            return p.read()

    def write(self, file: str, text: str) -> None:
        with open(file, "w") as p:
            p.write(text)

    def append(self, file: str, text: str) -> None:
        with open(file, "a") as p:
            p.write(text)