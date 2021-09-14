ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ!?@$%^&*)(`~-+=|\/;:"<>[]}{,.1234567890#'

def vigenere_encrypt(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper()

    cipher_text = ''
    
    # track letters of key
    key_index = 0

    for char in plain_text:
        # number of shifts = index of the char in the alphabet + index of char in the key
        index = (ALPHABET.find(char) + ALPHABET.find(key[key_index])) % len(ALPHABET)
        # keep appending the encrypted char to cipher_text
        cipher_text = cipher_text + ALPHABET[index]
        # inc key index to move to the next letter
        key_index = key_index + 1
        # start index over
        if key_index == len(key):
            key_index = 0

    return cipher_text


def vigenere_decrypt(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = key.upper()
    plain_text = ''
    # track key letters
    key_index = 0

    for char in cipher_text:
        #                              find the key letter by using its index
        index = (ALPHABET.find(char) - ALPHABET.find(key[key_index])) % len(ALPHABET)
        plain_text = plain_text + ALPHABET[index]
        key_index = key_index + 1
        if key_index == len(key):
            key_index = 0

    return plain_text


text = 'BLAKE SMELLS LIKE A FART, AND HIS EYEBROWS ARE ON FLEEK... YEET! IS HE HUMAN...?!'
key = 'PEPPA_PIG'

cipher = vigenere_encrypt(text, key)
print(cipher)
print(vigenere_decrypt(cipher, key))