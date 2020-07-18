from utility import multiply, divide, max
from shopping.more_shopping.shopping_cart import buy

if __name__ == '__main__':  # executes if this file is being run
    print(multiply(2, 3))  # => 6
    print(divide(2, 3))  # => 0.666666666666666
    print(buy('apple'))  # ['apple']
    print(max())  # oops
    print(__name__)  # __main__

