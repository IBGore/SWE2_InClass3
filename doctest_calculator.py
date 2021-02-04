#Doctest requires program is ran with -v
#Run program with "python3 doctest_calculator.py  -v"

"""
Addition Tests
>>> c.add(2, 1)
3

>>> c.add(1.1, 0)
1.1

>>> c.add(-1, 1)
0

>>> c.add(-10, -3)
-13


Subtraction Tests
>>> c.subtract(10, 9)
1

>>> c.subtract(10, 2.5)
7.5

>>> c.subtract(3, 5)
-2

>>> c.subtract(2, -1)
3


Multiplication
>>> c.multiply(2, 1)
2

>>> c.multiply(200, 0)
0

>>> c.multiply(0, -3)
0

>>> c.multiply(1.5, -1)
-1.5


Division
>>> c.divide(200, 1)
200.0

>>> c.divide(2, -2)
-1.0

>>> c.divide(5, 2)
2.5


>>> c.divide(3,0)
Traceback (most recent call last):
...
ZeroDivisionError: division by zero
"""
import calculator as c

if __name__ == "__main__":
    
    import doctest
    doctest.testmod()