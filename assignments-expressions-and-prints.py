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


