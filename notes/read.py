file = open('read.txt', 'r')
f = file.readlines()

new_list = []

for line in f:
    new_list.append(line.strip())

print(*new_list)

file.close()