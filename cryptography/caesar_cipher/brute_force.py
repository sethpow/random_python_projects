ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ!?'


def crack_cipher(cipher_text):
    for key in range(len(ALPHABET)):
        plain_text = ''

        for character in cipher_text:
            index = ALPHABET.find(character)
            index = (index - key) % len(ALPHABET)
            plain_text += ALPHABET[index]
        print(f'With key {key}, the result is: {plain_text}.')

    # return plain_text


crack_cipher('POEBWX JOXEOPOQTPGFXUG!ORDTPFGDTM')