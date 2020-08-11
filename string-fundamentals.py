# String Fundamentals

print('Meaning ' 'of' ' Life') # Implicit concatenation

print('knight\'s', "knight\"s")


s = 'a\nb\tc' # Embeds new line and tab

print(s)


# myfile = open(r'C:\new\text.dat', 'w')
# myfile = open('C:\\new\\text.dat', 'w')


path = r'C:\new\text.dat'

print(path) # User-friendly format

print(len(path)) # String length


mantra = '''Always look
on the bright
side of life.'''

print(mantra)

print('-----...more-----') # 80 dashes, the hard way
print('-' * 80) # 80 dashes, the easy way


myjob = 'hacker'

for c in myjob:
    print(c, end=' ') # Step through items, print each (3.X form)

print('k' in myjob) # Found

print('z' in myjob) # Not found

print('spam' in 'abcspamdef') # Substring search, no position returned



# Indexing and Slicing

S = 'spam'
print(S[0], S[-2]) # Indexing from front or end

print(S[1:3], S[1], S[:-1]) # Slicing: extract a section


S = 'abcdefghijklmnop'
print(S[1:10:2]) # Skipping items

print(S[::2])


S = 'hello'
print(S[::-1]) # Reversing items


S = 'abcdefg'
print(S[5:1:-1]) # Bounds roles differ


print('spam'[1:3]) # Slicing syntax

print('spam'[slice(1,3)]) # Slcie objects with index syntax + object

print('spam'[::1])

print('spam'[slice(None, None, -1)])



# String Conversion Tools

print(int('42'), str(42)) # Convert from/to string

print(repr(42)) # Convert to as-code string


S = '42'
I = 1

print(int(S) + I) # Force addition

print(S + str(I)) # Force concatenation


print(str(3.1415), float('1.5'))

text = '1.234E-10'

print(float(text))


print(ord('s'))

print(chr(115))


S = '5'
S = chr(ord(S) + 1)
print(S)

S = chr(ord(S) + 1)
print(S)


B = '1101' # Convert binary digits to integer with ord
I = 0
while B != '':
    I = I * 2 + (ord(B[0]) - ord('0'))
    B = B[1:]

print(I)


print(int('1101', 2)) # Convert binary to integer: built-in

print(bin(13)) # Convert integer to binary: built-in



# Changing Strings I

S = 'spam'
S = S + 'SPAM!' # To change a string, make a new one
print(S)

S = S[:4] + 'Burger' + S[-1]
print(S)


S = 'splot'
S = S.replace('pl', 'pamal')
print(S)


print('That is %d %s bird!' % (1, 'dead')) # Format expression: all Pythons

print('That is {0} {1} bird!'.format(1, 'dead')) # Format method in 2.6, 2.7, 3.X











