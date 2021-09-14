import matplotlib.pylab as plt

LETTERS = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ!?'


def frequency_analysis(text):
    text = text.upper()
    letter_frequencies = {}

    for letter in LETTERS:
        letter_frequencies[letter] = 0

    for letter in text:
        if letter in LETTERS:
            letter_frequencies[letter] += 1

    return letter_frequencies


def plot_distribution(frequencies):
    # horizontal axis, vertical axis
    plt.bar(frequencies.keys(), frequencies.values())
    plt.show()


# frequencies = frequency_analysis('I really need to take a massive poop right now Ouch')
# plot_distribution(frequencies)
# plot_distribution(frequency_analysis('I have three max level characters that will pwn you noob'))


def crack(cipher_text):
    freq = frequency_analysis(cipher_text)

    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    key = (LETTERS.find(freq[0][0]) - LETTERS.find("E"))

    print(f'The possible key value: {key}')
    print(f'Encrypted: {cipher_text}')

    # print(freq)
    # plot_distribution(freq)


text = 'POEBWX JOXEOPOQTPGFXUG!ORDTPFGDTM'


crack(text)


# crack('I have three max level characters that will pwn you noob')