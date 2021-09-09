from asyncronous.main import greet

from math import sqrt
import math
from myModule import print_name
import myModule

# other folders
import sys
sys.path.insert(1, './async')
# from async.main import greet


# both work
print(int(math.sqrt(9)))
print(sqrt(81))

myModule.print_name('Seth')

greet()