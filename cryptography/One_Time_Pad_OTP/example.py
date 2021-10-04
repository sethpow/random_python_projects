from random import randint


ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ!?@$%^&*)(`~-+=|\/;:"<>[]}{,.1234567890#'
# generate random numbers equal to this len; add rand num to the index number, and get the final value letter by index #


def encrypt(text, key):
    text = text.upper()
    cipher_text = ''

    # consider all plain_text char's; enumerate returns the index and item
    for index, char in enumerate(text):
        # value with which we shift the given letter
        key_index = key[index]
        # given letter in plain_text
        char_index = ALPHABET.find(char)
        # encrypted letter = char's value in plain_text + rand val (using %)
        cipher_text += ALPHABET[(char_index + key_index) % len(ALPHABET)]
    
    return cipher_text


def decrypt(cipher, key):
    plain = ''

    for index, char in enumerate(cipher):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        plain += ALPHABET[(char_index - key_index) % len(ALPHABET)]

    return plain


def random_sequence(text):
    # generate random sequence of random values, same length as text
    random = []

    for _ in range(len(text)):
        random.append(randint(0, len(ALPHABET) - 1))

    return random


message = 'You are not prepared... For the Alliance! The Horde will burn... Light be with you. Azeroth must not be allowed to perish. There must always be a Lich King.'
seq = random_sequence(message)
print(f'Original  message: {message.upper()}')
cipher = encrypt(message, seq)
print(f'Encrypted message: {cipher}')
decrypted = decrypt(cipher, seq)
print(f'Encrypted message: {decrypted}')