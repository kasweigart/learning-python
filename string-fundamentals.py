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



# String Methods

S = 'spammy'
S = S[:3] + 'xx' + S[5:] # Slice sections from S
print(S)


S = 'spammy'
S = S.replace('mm', 'xx') # Replace all mm with xx in S
print(S)


print('aa$bb$cc$dd'.replace('$', 'SPAM'))


S = 'xxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM') # Search for position
print(where) # Occurs at offset 4

S = S[:where] + "EGGS" + S[(where + 4):]
print(S)


S = 'xxxxSPAMxxxxSPAMxxxx'
print(S.replace('SPAM', 'EGGS')) # Replace all

print(S.replace('SPAM', 'EGGS', 1)) # Replace one


S = 'spammy'
L = list(S)
print(L)

L[3] = 'x' # Works for lists not strings
L[4] = 'x'

print(L)


S = ''.join(L)
print(S)


print('SPAM'.join(['eggs', 'sausage', 'ham', 'toast']))


line = 'aaa bbb ccc'
col1 = line[0:3]
col3 = line[8:]
print(col1)
print(col3)


line = 'aaa bbb  ccc'
cols = line.split()
print(cols)


line = 'bob,hacker,40'
print(line.split(','))


line = "i'mSPAMaSPAMlumberjack"
print(line.split('SPAM'))


line = 'The knights who say Ni!\n'
print(line.rstrip())
print(line.upper())
print(line.isalpha())
print(line.endswith('Ni!\n'))
print(line.startswith('The'))


print(line)
print(line.find('Ni') != -1) # Search via call or expression
print('Ni' in line)
sub = 'Ni!\n'
print(line.endswith(sub)) # End test via method call or slice
print(line[-len(sub):] == sub)


print('That is %d %s bird!' % (1, 'dead')) # Format expression


exclamation = 'Ni!'
print('The knights who say %s' % exclamation) # String substitution

print('%d %s %g you' % (1, 'spam', 4.0)) # Type-specific substitutions 

print('%s -- %s -- %s' % (42, 3.14159, [1,2,3])) # All types match a %s target


x = 1234
res = 'integers: ...%d...%-6d...%06d' % (x,x,x)
print(res)


x = 1.23456789
print(x) # Shows more digits before 2.7 and 3.1

print('%e | %f | %g' % (x,x,x))
print('%E' % x)


print('%-6.2f | %05.2f | %+06.1f' % (x,x,x))

print('%s' % x, str(x))

print('%f, %.2f, %.*f' % (1/3.0, 1/3.0, 4, 1/3.0))


print('%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'})


reply = '''
Greetings...
Hello %(name)s!
Your age is %(age)s
'''
values = {'name': 'Bob', 'age': 40}
print(reply % values)


food = 'spam'
qty = 10
print(vars())


print('%(qty)s more %(food)s' % vars()) # Variables are keys in vars()


template = '{0}, {1} and {2}' # By position
print(template.format('spam', 'ham', 'eggs'))

template = '{motto}, {pork} and {food}'  # By keyword
print(template.format(motto='spam', pork='ham', food='eggs'))

template = '{motto}, {0} and {food}'
print(template.format('ham', motto='spam', food='eggs'))

template = '{}, {} and {}' # By relative position
print(template.format('spam', 'ham', 'eggs'))


template = '%s, %s and %s' # Same via expression
print(template % ('spam', 'ham', 'eggs'))

template = '%(motto)s, %(pork)s and %(food)s'
print(template % dict(motto='spam', pork='ham', food='eggs'))


print('{motto}, {0} and {food}'.format(42, motto=3.14, food=[1,2]))


X = '{motto}, {0} and {food}'.format(42, motto=3.14, food=[1,2])
print(X)

print(X.split(' and '))

Y = X.replace('and', 'but under no circumstances')
print(Y)


import sys

print('My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'}))

print('My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'}))


somelist = list('SPAM')
print(somelist)


print('first={0[0]}, third={0[2]}'.format(somelist))

print('first={0}, last={1}'.format(somelist[0], somelist[-1]))

parts = somelist[0], somelist[-1], somelist[1:3]
print('first={0}, last={1}, middle={2}'.format(*parts))


print('{0:10} = {1:10}'.format('spam', 123.4567)) # In Python 3.3

print('{0:>10} = {1:<10}'.format('spam', 123.4567))

print('{0.platform:>10} = {1[kind]:<10}'.format(sys, dict(kind='laptop')))




