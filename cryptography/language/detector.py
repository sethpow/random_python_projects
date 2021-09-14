import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'english_words.txt')

english_words = []
dictionary = open(my_file, 'r')


def get_data():
    for word in dictionary.read().split('\n'):
        english_words.append(word)

    dictionary.close()


def count_words(text):
    text = text.upper()
    words = text.split(' ')
    matches = 0

    for word in words:
        if word in english_words:
            matches += 1
    
    return matches


def is_english(text):
    matches = count_words(text)

    if (float(matches) / len(text.split(' '))) * 100 >= 80:
        print('true')
        return True
    else:
        print('false')
        return False


get_data()
text = 'My little brother is super duper smelly and it is nasty YEET'
# text = 'yo quiero comer un pollo'
is_english(text)