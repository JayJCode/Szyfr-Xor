"""
Szyfr XOR:

Wzory:
E(k, m) = k XOR m
D(k, c) = k XOR c
m1 XOR m2 = c1 XOR c2

Definicje:
E (encryption):  funkcja szyfrujaca
D (decryption):  funkcja odszyfrujaca
k (key): klucz
m1, m2 (message): tekst jawny
c1, c2 (ciphertext): tekst zaszyfrowany

Pomoce:
znak spacji = 0b00100000
male litery = 0b011...
wynik xor dwoch malych liter = 0b000...
wynik xor spacji i malej litery = 0b010...

"""
from utils import Utils
import logging


def m1_xor_m2(m1: str, m2: str) -> str:
    return binary(chr(int(m1, 2) ^ int(m2, 2)))


def binary(c: str) -> str:
    return bin(ord(c))[2:].zfill(8)


class Xor:
    def __init__(self):
        self.utils = Utils()
        self.space = "00100000"
        self.line_length = 64

    def prepare_text(self) -> None:
        orig_text = self.utils.read("orig.txt").replace('\n', ' ')
        filtered_text = ""
        for char in orig_text:
            if char in self.utils.dictionary_small_letters:
                filtered_text += char
            elif char in self.utils.dictionary_big_letters:
                filtered_text += char.lower()
            elif char == ' ':
                filtered_text += char
            else:
                continue
        plain_text = [filtered_text[i:i + self.line_length] for i in range(0, len(filtered_text), self.line_length)]
        self.utils.write('plain.txt', '\n'.join(plain_text))

    def encrypt(self) -> None:
        with open('plain.txt', 'r', encoding='utf-8') as f:
            plain_text = f.readlines()
        key = self.utils.read("key.txt")
        self.utils.write("crypto.txt", "")
        for line in plain_text:
            encrypted_line = ''
            for index, char in enumerate(line):
                bin_char = binary(char)
                bin_key = binary(key[index % len(key)])
                encrypted_line += m1_xor_m2(bin_char, bin_key)
            self.utils.append("crypto.txt", encrypted_line + '\n')

    def check_correctness(self) -> None:
        decrypt_text = self.utils.read("decrypt.txt")
        plain_text = self.utils.read("plain.txt")
        correctness = 0
        mistakes = 0
        unknown = 0

        for index in range(len(plain_text)):
            if decrypt_text[index] == '_':
                unknown += 1
            elif decrypt_text[index] == plain_text[index]:
                correctness += 1
            elif decrypt_text[index] != plain_text[index]:
                print(f"Bledny znak: {decrypt_text[index]} w miejscu {index} powinno byc {plain_text[index]}")
                mistakes += 1

        print(f"Poprawne: {correctness/len(plain_text)}%, Bledy: {mistakes/len(plain_text)}%, Nieznane: {unknown/len(plain_text)}%")

    def value_check(self, crypto_text, array_of_results, line_index, index) -> None:
        if line_index >= len(crypto_text) - 2:
            return None
        m1 = crypto_text[line_index][index:index + 8]
        m2 = crypto_text[line_index + 1][index:index + 8]
        if m1_xor_m2(m1, m2) == '00000000':
            # value2 = value1
            array_of_results[line_index][index // 8] = 'K'
            array_of_results[line_index + 1][index // 8] = 'K'
            if ' ' == array_of_results[line_index][index // 8]:
                array_of_results[line_index + 1][index // 8] = ' '
            elif 'W' == array_of_results[line_index][index // 8]:
                array_of_results[line_index + 1][index // 8] = 'W'
            elif 'L' == array_of_results[line_index][index // 8]:
                array_of_results[line_index + 1][index // 8] = 'L'
        elif m1_xor_m2(m1, m2)[0:3] == '000':
            # litera x2
            if 'K' == array_of_results[line_index][index // 8]:
                array_of_results[line_index - 1][index // 8] = 'L'
            if 'W' == array_of_results[line_index][index // 8]:
                array_of_results[line_index - 1][index // 8] = ' '
                m2_char = chr(int(m1_xor_m2(
                    m1_xor_m2(crypto_text[line_index - 1][index:index + 8], crypto_text[line_index][index:index + 8]),
                    self.space), 2))
                array_of_results[line_index][index // 8] = m2_char
                m3_char = chr(int(m1_xor_m2(m1_xor_m2(crypto_text[line_index - 1][index:index + 8],
                                                      crypto_text[line_index + 1][index:index + 8]), self.space), 2))
                array_of_results[line_index + 1][index // 8] = m3_char
            else:
                array_of_results[line_index][index // 8] = 'L'
                array_of_results[line_index + 1][index // 8] = 'L'
        elif m1_xor_m2(m1, m2)[0:3] == '010':
            # value2 | value1 => spacja | litera
            array_of_results[line_index][index // 8] = 'W'
            array_of_results[line_index + 1][index // 8] = 'W'
            if ' ' == array_of_results[line_index][index // 8]:
                array_of_results[line_index + 1][index // 8] = 'L'
            elif 'L' == array_of_results[line_index][index // 8]:
                array_of_results[line_index + 1][index // 8] = ' '
        self.value_check(crypto_text, array_of_results, line_index + 1, index)

    def cryptoanalysis(self) -> None:
        with open('crypto.txt', 'r', encoding='utf-8') as f:
            crypto_text = [line.strip() for line in f.readlines()]
        self.utils.write("decrypt.txt", "")
        crypto_length = len(crypto_text)
        array_of_results = [['_' for _ in range(self.line_length)] for _ in range(len(crypto_text))]

        for index in range(0, (self.line_length - 1) * 8, 8):
            self.value_check(crypto_text, array_of_results, 0, index)

        for line in array_of_results:
            for i in range(len(line)):
                if line[i] == 'K':
                    line[i] = '_'
                elif line[i] == 'W':
                    line[i] = '_'
                elif line[i] == 'L':
                    line[i] = '_'

        result = "\n".join("".join(line) for line in array_of_results)

        for row_index in range(len(crypto_text)):
            crypto_text[row_index] = crypto_text[row_index][:-1]

        for col in range(self.line_length):
            col_key = ""
            for row in range(crypto_length-1):
                if array_of_results[row][col] != '_':
                    col_key = m1_xor_m2(crypto_text[row][col*8:col*8+8], binary(array_of_results[row][col]))
                    col_key = chr(int(col_key, 2))

            if col_key != "":
                for row in range(len(array_of_results)):
                    max = len(crypto_text[row])
                    if col*8+8 < max:
                        if array_of_results[row][col] == '_':
                            array_of_results[row][col] = chr(int(m1_xor_m2(crypto_text[row][col*8:col*8+8], binary(col_key)), 2))
                    else:
                        array_of_results[row][col] = ""

        result = "\n".join("".join(line) for line in array_of_results)

        self.utils.write("decrypt.txt", result)
        self.check_correctness()