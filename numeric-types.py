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