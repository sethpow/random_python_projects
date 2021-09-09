def math_stuff(x, y, z=None): # params
    if z != None:
        return (x*z, x+z)
    else:
        return (x*y, x+y)


r1, r2 = math_stuff(5, 20, 100)
print(r1) # args
print(r2)

# --------------------------------------

