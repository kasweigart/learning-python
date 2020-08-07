# Other Core Types

X = set('spam') # Make a set out of a sequence
Y = {'h', 'a', 'm'} # Make a set out of literals

print(X, Y) # A tuple of two sets without parentheses
print(X & Y) # Intersection
print(X | Y) # Union
print(X - Y) # Difference
print(X > Y) # Superset

print({n ** 2 for n in [1,2,3,4]}) # Set comprehensions

print(list(set([1,2,1,3,1]))) # Filtering out duplicates
print(set('spam') - set('ham')) # Finding differences in collections
print(set('spam') == set('asmp')) # Order-neutral equality ('spam'=='asmp' False)

print('p' in set('spam'))

print(1/3) # Floating-point
print((2/3)+(1/2))

import decimal # Decimals fixed position
d = decimal.Decimal('3.141')
print(d + 1)

from fractions import Fraction # Fractions: numerator+demoninator
f = Fraction(2,3)
print(f + 1)
print(f + Fraction(1,2))

print(1 > 2, 1 < 2) # Booleans
print(bool('spam')) # Object's boolen value

x = None # None placeholder
print(x)

L = [None] * 100 # Initialize a list of 100 Nones
print(L)

print(type(L)) # Types: type of L is list type object
print(type(type(L))) # Even types are objects

if type(L) == type([]): # Type testing, if you must...
    print('yes')

if type(L) == list: # Using the type name
    print('yes')

if isinstance(L, list): # Object-oriented tests
    print('yes')

class Worker:
    def __init__(self, name, pay): # Initialize when created
        self.name = name # Self is the new object
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1] # Split strings on blanks
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent) # Update pay in place

bob = Worker('Bob Smith', 50000) # Make two instances
sue = Worker('Sue Jones', 60000) # Each had name and pay attrs
print(bob.lastName()) # Call method: bob is self

print(sue.lastName()) # sue is the self subject

sue.giveRaise(.1) # Update sue's pay
print(sue.pay)