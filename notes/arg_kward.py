# unpack
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(x)
print(*x)


# arg kwarg
def defined(*args, **kwargs):
    print(*args)
    print(kwargs)

defined(1, 23, 34, 54, one=3, two=8)