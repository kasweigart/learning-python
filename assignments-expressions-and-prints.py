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






