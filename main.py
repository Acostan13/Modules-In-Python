from utility import multiply, divide, max
from shopping.more_shopping.shopping_cart import buy
import random
import sys

if __name__ == '__main__':  # executes if this file is being run
    print(multiply(2, 3))  # => 6
    print(divide(2, 3))  # => 0.666666666666666
    print(buy('apple'))  # ['apple']
    print(max())  # oops
    print(__name__)  # __main__

print(random)  # <module'random' from 'C:\\Users\\alexc\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\random.py'>
help(random)  # gives helpful information about the random package
print(dir(random))  # lists every method you can use within the random package
print(random.random())  # gives a random number between 0 and 1
print(random.randint(1, 10))  # gives a random integer inclusively between two parameters
print(random.choice([1, 2, 3, 4, 5]))  # picks a random value within the array

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)  # shuffled list

print(sys)  # <module 'sys' (built-in)>
sys.argv  # runs files from the terminal


