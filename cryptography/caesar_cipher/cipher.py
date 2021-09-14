ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ!?'
KEY = 15


def encrypt(plain_text):
    # encrypted message
    cipher_text = ''
    plain_text = plain_text.upper()

    for character in plain_text:
        # normal index
        index = ALPHABET.find(character)
        # encrypted index
        index = (index + KEY) % len(ALPHABET)
        cipher_text += ALPHABET[index]
    return cipher_text


def decrypt(cipher_text):
    plain_text = ''

    for character in cipher_text:
        index = ALPHABET.find(character)
        index = (index - KEY) % len(ALPHABET)
        plain_text += ALPHABET[index]
    return plain_text
    

encrypted = encrypt('A sphinx is a beautiful creature!')
print(encrypted)
print(decrypt(encrypted))