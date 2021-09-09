name = input('What is your name?\n')

file = open('myfile.txt', mode='w', )

file.write(name)
file.close()

file = open('myfile.txt', mode='r')
file.read()



isOld = True