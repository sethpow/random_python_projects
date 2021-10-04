# DES cryptosystem implementation
# see instructor/DES.py
from Crypto.Cipher import DES


def add_padding():
    pass


def remove_padding(str, blocksize=64):
    counter = 0

    for c in str[::-1]:
        if c == '$':
            # if size of str cannot be divided by 64 w/o remainder, append to end
            counter += 1
        else:
            break

    return str[:-counter]