# Assignments, Expressions, and Prints



nudge = 1 # Basic Assignment

wink = 2

A, B = nudge, wink # Tuple assignment

print(A, B) # Like A = nudge; B = wink

[C, D] = [nudge, wink] # List assignment

print(C, D)


nudge = 1

wink = 2

nudge, wink = wink, nudge # Tuples: swaps values

print(nudge, wink) # Like T = nudge; nudge = wink; wink = T


[a, b, c] = (1, 2, 3) # Assign tuple of values to list of names

print(a, c)

(a, b, c) = 'ABC' # Assign string of characters to tuple

print(a, c)


string = 'SPAM'

a, b, c, d = string # Same number on both sides

print(a, d)

# a, b, c = string # ValueError: too many values to unpack (expected 3)


a, b, c = string[0], string[1], string[2:] # Index and slice

print(a, b, c)

a, b, c = list(string[:2]) + [string[2:]] # Slice and concatenate

a, b = string[:2] # Same, but simpler

c = string[2:]

print(a, b, c)

(a, b), c = string[:2], string[2:] # Nested sequences

print(a, b, c)


((a, b), c) = ('SP', 'AM') # Paired by shape and position

print(a, b, c)


for (a, b, c) in [(1, 2, 3), (4, 5, 6)]: ... # Simple tuple assignment

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: ... # Nested tuple assignment


red, green, blue = range(3)

print(red, blue)


print(list(range(3))) # list() required in Python 3.X only


L = [1, 2, 3, 4]

while L:
    front, L = L[0], L[1:] # See next section for 3.X * alternative
    print(front, L)

# front = L[0]
# L = L[1:]


seq = [1, 2, 3, 4]

a, b, c, d = seq

print(a, b, c, d)


# a, b = seq # ValueError: too many values to unpack (expected 2)


*a, b = seq

print(a)

print(b)


a, *b, c = seq

print(a)

print(b)

print(c)


a, b, *c = seq

print(a)

print(b)

print(c)


a, *b = 'spam'

print(a, b)


a, *b, c = 'spam'

print(a, b, c)


a, *b, c = range(4)

print (a, b, c)


S = 'spam'

print(S[0], S[1:]) # Slices are type-specific, * assignment always returns a list

print(S[0], S[1:3], S[3])


L = [1, 2, 3, 4]

while L:
    front, *L = L # Get first, rest without slicing
    print(front, L)


seq = [1, 2, 3, 4]

a, b, c, *d = seq

print(a, b, c, d)


a, b, c, d, *e = seq

print(a, b, c, d, e)


a, b, *e, c, d = seq

print(a, b, c, d, e)


# a, *b, c, *d = seq # SyntaxError: two starred expressions in assignment

# a, b = seq # ValueError: too many values to unpack (expected 2)

# *a = seq # SyntaxError: starred assignment target must be in a list or tuple

*a, = seq

print(a)


print(seq)

a, *b = seq # First, rest

print(a, b)


a, b = seq[0], seq[1:] # First, rest: traditional

print(a, b)


*a, b = seq # Rest, last

print(a, b)


a, b = seq[:-1], seq[-1] # Rest, last: traditional

print(a, b)


# for (a, *b, c) in [(1, 2, 3, 4,), (5, 6, 7, 8)]: ...


a, *b, c = (1, 2, 3, 4) # b gets [2, 3]


# for (a, b, c) in [(1, 2, 3), (4, 5, 6)]: # a, b, c = (1, 2, 3), ...


# for all in [(1, 2, 3, 4), (5, 6, 7, 8)]:
#     a, b, c = all[0], all[1:3], all[3]


a = b = c = 'spam'

print(a, b, c)


c = 'spam'

b = c

a = b


a = b = 0

b = b + 1

print(a, b)


a = b = []

b.append(42)

print(a, b)


a = []

b = [] # a and b do not share the same object

b.append(42)

print(a, b)


a, b = [], [] # a and b do not share the same object


# X = X + Y # Traditional form

# X += Y # Newer augmented form


x = 1

x = x + 1 # Traditional

print(x)

x += 1 # Augmented

print(x)


S = 'spam'

S += 'SPAM' # Implied concatenation

print(S)


L = [1, 2]

L = L + [3] # Concatenate: slower

print(L)

L.append(4) # Faster, but in place

print(L)


L = L + [5, 6] # Concatenate: slower

print(L)

L.extend([7, 8]) # Faster, but in place

print(L)


L += [9, 10] # MApped to L.extend([9, 10])

print(L)


L = []

L += 'spam' # += and extend allow any sequence, but + does not!

print(L)

# L = L + 'spam' # TypeError: can only concatenate list (not "str") to list


L = [1, 2]

M = L # L and M reference the same object

L = L + [3, 4] # Concatenation makes a new object

print(L, M) # Changes L but not M


L = [1, 2]

M = L

L += [3, 4] # But += really means extend

print(L, M) # M sees the in-place change too!


x = 0 # x bound to an integer object

x = 'Hello' # Now it's a string

x = [1, 2, 3] # And now it's a list


x = print('spam') # print is a function call expression in 3.X

print(x) # But it is coded as an expression statement


L = [1, 2]

L.append(3) # Append is an in-place change

print(L)


L = L.append(4) # But append returns None, not L

print(L) # So we lose our list!


print() # Display a blank line

x = 'spam'

y = 99

z = ['eggs']

print(x, y, z) # Print three objects per defaults


print(x, y, z, sep='') # Suppress seperator

print(x, y, z, sep=', ') # Custom seperator


print(x, y, z, end='') # Suppress line break

print(x, y, z, end=''); print(x, y, z) # Two prints, same output line

print(x, y, z, end='...\n') # Custom line end


print(x, y, z, sep='...', end='!\n') # Multiple keywords

print(x, y, z, end='!\n', sep='...') # Order doesn't matter


print(x, y, z, sep='...', file=open('data.txt', 'w')) # Print to a file

print(x, y, z) # Back to stdout

print(open('data.txt').read()) # Display file text


text = '%s: %-.4f, %05d' % ('Result', 3.14159, 42)

print(text)

print('%s: %-.4f, %05d' % ('Result', 3.14159, 42))


import sys # Printing the hard way

sys.stdout.write('hello world\n')


import sys

temp = sys.stdout # Save for restoring later

sys.stdout = open('log.txt', 'a') # Redirect prints to a file

print('spam') # Prints go to file, not here

print(1, 2, 3)

sys.stdout.close() # Flush output to disk

sys.stdout = temp # Restore original stream

print('back here') # Prints show up here again

print(open('log.txt').read()) # Result of earlier prints


log = open('log.txt', 'a') # 3.X

print(x, y, z, file=log) # Print to a file-like object

print(a, b, c) # Print to original stdout


log = open('log.txt', 'w')

print(1, 2, 3, file=log) # for 2.X: print >> log, 1, 2, 3

print(4, 5, 6, file=log)

log.close()

print(7, 8, 9) # For 2.X: print 7, 8, 9

print(open('log.txt').read())


import sys

sys.stderr.write(('Bad!' * 8) + '\n')


X = 1; Y = 2 # Print: the easy way

print(X, Y)


import sys # Print: the hard way

sys.stdout.write(str(X) + ' ' + str(Y) + '\n')

print(X, Y, file=open('temp1', 'w')) # Redirect text to file

open('temp2', 'w').write(str(X) + ' ' + str(Y) + '\n') # Send to file manually

print(open('temp1', 'rb').read()) # Binary mode for bytes

print(open('temp2', 'rb').read())


print('spam') # 3.X print function call syntax

print('spam', 'ham', 'eggs') # These are multiple arguments


print('%s %s %s' % ('spam', 'ham', 'eggs'))

print('{0} {1} {2}'.format('spam', 'ham', 'eggs'))

print('answer: ' + str(42))






