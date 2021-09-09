file = open('write.txt', 'w')


name = input('What is your name? ')
file.write(name)


file.close()