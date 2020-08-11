# Numeric Display Types


num = 1 / 3.0 
print(num) # Print explicitly

print('%e' % num) # String formatting expression

print('%4.2f' % num) # Alternative floating-point format

print('{0:4.2f}'.format(num)) # String formatting method


print(repr('spam')) # Used by echoes: as-code form
print(str('spam')) # Used by print: user-friendly form



# Hex, Octal, Binary: Literals and Conversions

print(0o1, 0o20, 0o377) # Octal literals: base 8, digits 0-7

print(0x01, 0x10, 0xFF) # Hex literals: base 16, digits 0-9/A-F

print(0b1, 0b10000, 0b11111111) # Binary literals: base 2, digits 0-1


print(0xFF, (15 * (16 ** 1)) + (15 * (16 ** 0))) # How hex/binary map to decimal

print(0x2F, (2 * (16 ** 1)) + (15 * (16 ** 0)))

print(0xF, 0b1111, (1 * (2 ** 3) + 1 * (2 ** 2) + 1 * (2 ** 1) + 1 * (2 ** 0)))


print(oct(64), hex(64), bin(64)) # Numbers => digit strings


print(64, 0o100, 0x40, 0b1000000) # Digits => numbers in scripts and strings

print(int('64'), int('100', 8), int('40', 16), int('1000000', 2))

print(int('0x40', 16), int('0b1000000', 2)) # Literal forms are supported too


print(eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000'))


print('{0:o}, {1:x}, {2:b}'.format(64, 64, 64)) # Numbers => digits

print('%o, %x, %x, %X' % (64, 64, 255, 255))


print(0o1, 0o20, 0o377) # New octal format in 2.6+ (same as 3.X)



# Bitwise Operations

x = 1 # 1 decimal is 0001 in bits
print(x << 2) # Shift left 2 bits: 0100
print(x | 2) # Bitwise OR (either bit=1): 0011
print(x & 1) # Bitwise AND (both bits=1): 0001

X = 0b0001 # Binary literals
print(X << 2) # Shift left
print(bin(X << 2)) # Binary digit string

print(bin(X | 0b010)) # Bitwise OR: either

print(bin(X & 0b1)) # Bitwise AND: both


X = 0xFF # Hex literals
print(bin(X))

print(X ^ 0b10101010 ) # Bitwise XOR: either but not both

print(int('01010101', 2)) # Digits=>number: string to int per base

print(hex(85)) # Number=>digits: Hex digit string


X = 99
print(bin(X), X.bit_length(), len(bin(X)) - 2)
print(bin(256), (256).bit_length(), len(bin(256)) - 2)



# Other Built-in Numeric Tools

import math
print(math.pi, math.e) # Common constants

print(math.sin(2 * math.pi / 180)) # Sine, tangent, cosine

print(math.sqrt(144), math.sqrt(2)) # Square root

print(pow(2, 4), 2**4, 2.0**4.0) # Exponentation (power)

print(abs(-42.0), sum((1,2,3,4))) # Absolute value, summation

print(min(3,1,2,4), max(3,1,2,4)) # Minimum, maximum


print(math.floor(2.567), math.floor(-2.567)) # Floor (next-lower intger)

print(math.trunc(2.567), math.trunc(-2.567)) # Truncate (drop decimal digits)

print(int(2.567), int(-2.567)) # Truncate (integer conversion)

print(round(2.567), round(2.467), round(2.567, 2)) # Round

print('%.1f' % 2.567, '{0:.2f}'.format(2.567)) # Round for display


print(math.sqrt(144)) # Module

print(144 ** .5) # Expression

print(pow(144, .5)) # Built-in


print(math.sqrt(1234567890)) # Large numbers

print(1234567890 ** .5)

print(pow(1234567890, .5))


import random
print(random.random()) # Random floats, integers, choices, shuffles

print(random.randint(1,10))

print(random.randint(1,10))


print(random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life']))
print(random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life']))

suits = ['hearts', 'clubs', 'diamonds', 'spades']

print(suits)

random.shuffle(suits)

print(suits)



# Other Numeric Types

print(0.1 + 0.1 + 0.1 - 0.3) # Python 3.3

from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))


import decimal

print(decimal.Decimal(1) / decimal.Decimal(7)) # Default: 28 digits

decimal.getcontext().prec = 4 # Fixed precision

print(decimal.Decimal(1) / decimal.Decimal(7))

print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3)) # Closer to 0


import decimal

print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))


from fractions import Fraction

x = Fraction(1,3) # Numerator, denomimator
y = Fraction(4,6) # Simplified to 2,3 by greatest common denominator

print(x)
print(y)


print(x + y)
print(x - y) # Results are exact: numerator, denominator
print(x * y)


print(Fraction('.25'))
print(Fraction('1.25'))
print(Fraction('.25') + Fraction('1.25'))


a = 1 / 3.0 # Only as accurate as floating-point hardware
b = 4 / 6.0 # Can lose precision over many calculations

print(a)
print(b)


print(a + b)
print(a - b)
print(a * b)


print((2.5).as_integer_ratio()) # float object method

f = 2.5

z = Fraction(*f.as_integer_ratio()) # Convert flaot -> fraction: two args

print(z) # Same as Fraction(5, 2)


print(x) # x from prior interaction

print(x + z) # 5/2 + 1/3 = 15/6 + 2/6


print(float(x)) # Convert fraction -> float

print(float(z))

print(float(x + z))

print(17/6)


print(Fraction.from_float(1.75)) # Convert float -> fraction: other way

print(Fraction(*(1.75).as_integer_ratio()))


print(x)

print(x + 2) # Fraction + float -> Fraction

print(x + 2.0) # Fraction + float -> float

print(x + 1./3) # Fraction + float -> float

print(x + Fraction(4,3)) # Fraction + Fraction -> Fraction


print(4.0 / 3)

print((4.0 / 3).as_integer_ratio()) # Precision loss from float

print(x)

a = x + Fraction(*(4.0 / 3).as_integer_ratio())

print(a)

print(22517998136852479 / 13510798882111488) # 5/3 (or close to it!)

print(a.limit_denominator(10)) # Simplify to closest fraction



# Sets

x = set('abcde')
y = set('bdxyz')

print(x)

print(x - y) # Difference

print(x | y) # Union

print(x & y) # Intersection

print(x ^ y) # Symmetric difference (XOR)

print(x > y, x < y) # Superset, subset


print('e' in x) # Membership (sets)

print('e' in 'Camelot', 22 in [11,22,33]) # But works on other types too


z = x.intersection(y) # Same as x & y

print(z)

z.add('SPAM') # Insert one item

print(z)

z.update(set(['X', 'Y'])) # Merge: in-place union

print(z)

z.remove('b') # Delete one item

print(z)


for item in set('abc'):
    print(item*3)


S = set([1,2,3])

print(S | set([3,4])) # Expressions require both to be sets

# (S | [3,4]) TypeError

print(S.union([3,4])) # But their methods allow any iterable

print(S.intersection((1,3,5)))

print(S.issubset(range(-5,5)))


S1 = {1,2,3,4}

print(S1 - {1,2,3,4}) # Empty sets print differently

print(type({})) # Because {} is an empty dictionary

S = set() # Initialize an empty set

S.add(1.23)

print(S)


print(S)

# S.add([1,2,3]) TypeError: only immutable objects work in a set

# S.add({'a':1}) TypeError

S.add((1,2,3))

print(S) # No list or dict, but tuple OK

print(S | {(4,5,6), (1,2,3)}) # Union: same as S.union(...)

print((1,2,3) in S) # Membership: by complete values

print((1,4,3) in S)


print({x ** 2 for x in [1,2,3,4]}) # 3.X/2.7 set comprehension


print({x for x in 'spam'}) # Same as: set('spam')

print({c * 4 for c in 'spam'}) # Set of collected expression results

print({c * 4 for c in 'spamham'})

S = {c * 4 for c in 'spam'}

print(S | {'mmmm', 'xxxx'})

print(S & {'mmmm', 'xxxx'})


L = [1,2,1,3,2,4,5]

print(set(L))

L = list(set(L)) # Remove duplicates

print(L)

print(list(set(['yy', 'cc', 'aa', 'xx', 'dd', 'aa']))) # But order may change


print(set([1,3,5,7]) - set([1,2,4,5,6])) # Find list differences

print(set('abcdefg') - set('abdghij')) # Find string differences
 
print(set('spam') - set(['h', 'a', 'm'])) # Find differences, mixed

print(set(dir(bytes)) - set(dir(bytearray))) # In bytes but not bytearray

print(set(dir(bytearray)) - set(dir(bytes)))


L1, L2 = [1,2,5,2,4], [2,5,3,4,1]

print(L1 == L2) # Order matters in sequences

print(set(L1) == set(L2)) # Order-neutral equality

print(sorted(L1) == sorted(L2)) # Similar but results are ordered

print('spam' == 'asmp', set('spam') == set('asmp'), sorted('spam') == sorted('asmp'))


engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom', 'sue'}

print('bob' in engineers) # Is bob an engineer?

print(engineers & managers) # Who is both engineer and manager?

print(engineers | managers) # All people in either category

print(engineers - managers) # Engineers who are not managers

print(managers - engineers) # Managers who are not engineers

print(engineers > managers) # Are all managers engineers? (superset)

print({'bob', 'sue'} < engineers) # Are both engineers? (subset)

print((managers | engineers) > managers) # All people is a superset of managers

print(managers ^ engineers) # Who is one but not both?

print((managers | engineers) - (managers ^ engineers)) # Intersection!



# Booleans

print(type(True))

print(isinstance(True, int))

print(True == 1) # Same value

print(True is 1) # But a different object

print(True or False) # Same as: 1 or 0

print(True + 4) # (Hmmm)



