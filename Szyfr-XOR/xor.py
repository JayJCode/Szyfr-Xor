"""
Program szyfrujaco-deszyfrujacy.
Napisany na potrzeby zaliczenia 3 laboratoriow.
Termin: 06 kwietnia 2025.
Autor: Jan Janowicz
"""
from xor_class import Xor
import argparse


def argparse_init() -> argparse.Namespace:
    """
    Przyklad uzycia: python xor.py -e
    """
    parser = argparse.ArgumentParser()

    # Uzytkownik powinien wybrac jedna z 3 opcji mozliwych akcji
    parser.add_argument("-e", "--encryption", action="store_true", help="Szyfrowanie")
    parser.add_argument("-p", "--prepare", action="store_true", help="Przygotowanie tekstu")
    parser.add_argument("-k", "--krypto", action="store_true", help="Kryptoanaliza wylacznie w oparciu o kryptogram")

    return parser.parse_args()

def algorithm_choice(args: argparse.Namespace) -> None:
    """
    Funkcja wybiera algorytm szyfrowania w zaleznosci od wyboru uzytkownika.
    """
    xor = Xor()
    if (args.encryption and args.prepare or args.encryption and args.krypto or args.prepare and args.krypto
        or args.encryption and args.prepare and args.krypto):
        raise ValueError("Wybierz tylko jedna akcje")
    elif args.encryption:   xor.encrypt()
    elif args.prepare:      xor.prepare_text()
    elif args.krypto:       xor.cryptoanalysis()
    else:                   raise ValueError("Brak wartosci: musisz wybrac jedna z opcji akcji (-e, -p, -k)")

def main():
    args = argparse_init()
    algorithm_choice(args)

main()