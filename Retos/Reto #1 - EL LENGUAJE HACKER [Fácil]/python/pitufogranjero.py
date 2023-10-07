# Escribe un programa que reciba un texto y transforme lenguaje natural a
# "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
# se caracteriza por sustituir caracteres alfanuméricos.
# - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
# con el alfabeto y los números en "leet".
# (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

leet = {
    'a': '4',
    'b': '8',
    'c': '<',
    'd': '|)',
    'e': '3',
    'f': '|=',
    'g': '9',
    'h': '#',
    'i': '1',
    'j': '_|',
    'k': '|<',
    'l': '1',
    'm': '|\/|',
    'n': '|\|',
    'o': '0',
    'p': '|>',
    'q': '(_,)',
    'r': '|2',
    's': '5',
    't': '7',
    'u': '|_|',
    'v': '\/',
    'w': '\/\/',
    'x': '><',
    'y': '¥',
    'z': '2',
    '1': 'L',
    '2': 'Z',
    '3': 'E',
    '4': 'A',
    '5': 'S',
    '6': 'b',
    '7': 'T',
    '8': 'B',
    '9': 'g',
    '0': 'O'
}

def hackerLang(message: str):
    print(leet)
    for char in message:
        if char in leet:
            message = message.replace(char, leet[char])
    print(message)

hackerLang('Escribe un programa que reciba un texto y transforme lenguaje natural')
