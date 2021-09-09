x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x2 = [ele *2 for ele in x if (ele % 2 == 0 and ele != 10)]

# print(x2)




for (index, num) in enumerate(x):
    print(index, num*2)