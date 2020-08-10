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







