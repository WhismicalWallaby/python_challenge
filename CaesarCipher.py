import string

letters = [char for char in string.ascii_letters]


def caesar_decoder(message, key):
    translated = ''

    for char in message:
        if char in letters:
            translated += letters[(letters.index(char) - key) % len(letters)]
        else:
            translated += char

    return translated
