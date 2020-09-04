# Tuples, Files, and Everything Else



# Tuples


print((1, 2) + (3, 4)) # Concatenation

print((1, 2) * 4) # Repitition

T = (1, 2, 3, 4) # Indexing and slicing

print(T[0], T[1:3])


x = (40) # An integer!

print(x)

y = (40,) # A tuple containing an integer

print(y)


T = ('cc', 'aa', 'dd', 'bb')

tmp = list(T) # Make a list from a tuple's items

tmp.sort() # Sort the list

print(tmp) 

T = tuple(tmp) # Make a tuple from the list's items

print(T)

print(sorted(T)) # Or use the sorted built-in, and save two steps


T = (1, 2, 3, 4, 5)

L = [x + 20 for x in T]

print(L)


T = (1, 2, 3, 2, 4, 2) # Tuple methods in 2.6, 3.0, and later

print(T.index(2)) # Offset of first appearance of 2

print(T.index(2, 2)) # Offset of appearance after offset 2

print(T.count(2)) # How many 2s are there?


T = (1, [2, 3], 4)

# T[1] = 'spam' # This fails: can't change tuple itself

T[1][0] = 'spam' # This works: can change mutables inside

print(T)


bob = ('Bob', 40.5, ['dev', 'mgr']) # Tuple record

print(bob)

print(bob[0], bob[2]) # Access by position


bob = dict(name='Bob', age=40.5, jobs=['dev', 'mgr']) # Dictionary record

print(bob)

print(bob['name'], bob['jobs']) # Access by key


print(tuple(bob.values())) # Values to tuple

print(list(bob.items())) # Items to tuple list


from collections import namedtuple # Import extension type

Rec = namedtuple('Rec', ['name', 'age', 'jobs']) # Make a generated class

bob = Rec('Bob', age=40.5, jobs=['dev', 'mgr']) # A named-tuple record

print(bob)


print(bob[0], bob[2]) # Access by position

print(bob.name, bob.jobs) # Access by attribute


O = bob._asdict() # Dictionary-like form

print(O['name'], O['jobs']) # Access by key too

print(O)


bob = Rec('Bob', 40.5, ['dev', 'mgr']) # For both tuples and named tuples

name, age, jobs = bob # Tuple assignment (Chapter 11)

print(name, jobs)

for x in bob: print(x) # Iteration context (Chapters 14, 20)


bob = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}

job, name, age = bob.values()

print(name, job) # Dict equivalent (but order may vary)

for x in bob: print(bob[x]) # Step through keys, index values

for x in bob.values(): print(x) # Step through values view


# Files


myfile = open('myfile.txt', 'w') # Open for text output: create/empty

myfile.write('hello text file\n') # Write a line of text: string

myfile.write('goodbye text file\n')

myfile.close() # Flush out buffers to disk


myfile = open('myfile.txt') # Open for text input: 'r' is default

print(myfile.readline()) # Read the lines back

print(myfile.readline())

print(myfile.readline()) # Empty string: end-of-file


print(open('myfile.txt').read()) # Read all at once into string


for line in open('myfile.txt'): # Use file iterators. not reads
    print(line, end='')


data = open('data.bin', 'rb').read() # Open binary file: rb=read binary

print(data) # byte string holds binary data

print(data[4:8]) # Act like strings

print(data[4:8][0]) # But really are small 8-bit integers

print(bin(data[4:8][0])) # Python 3.X/2.6+ bin() function


X, Y, Z = 43, 44, 45 # Native Python objects

S = 'Spam' # Must be strings to store in file

D = {'a': 1, 'b': 2}

L = [1, 2, 3]


F = open('datafile.txt', 'w') # Create output text file

F.write(S + '\n') # Terminate lines with \n

F.write('%s,%s,%s\n' % (X, Y, Z)) # Convert numbers to strings

F.write(str(L) + '$' + str(D) + '\n') # Convert and seperate with $

F.close()


chars = open('datafile.txt').read() # Raw string display

print(chars) # User-friendly display


F = open('datafile.txt') # Open again

line = F.readline() # Read one line

print(line) # Remove end-of-line


line = F.readline() # Next line from file

print(line)

parts = line.split(',') # Split (parse) on commas

print(parts)


print(int(parts[1])) # Convert from string to int

numbers = [int(P) for P in parts] # Convert all in list at once

print(numbers)


line = F.readline()

print(line)

parts = line.split('$') # Split (parse) on $

print(parts)

print(eval(parts[0]))

objects = [eval(P) for P in parts] # Do same for all in list

print(objects)


D = {'a': 1, 'b': 2}

F = open('datafile.pkl', 'wb')

import pickle

pickle.dump(D, F)

F.close() # Pickle any object to file


F = open('datafile.pkl', 'rb')

E = pickle.load(F) # Load any object from file

print(E)


print(open('datafile.pkl', 'rb').read()) # Format is prone to change!


name = dict(first='Bob', last='Smith')

rec = dict(name=name, job=['dev', 'mgr'], age=40.5)

print(rec)


import json

print(json.dumps(rec))

S = json.dumps(rec)

print(S)

O = json.loads(S)

print(O)

print(O == rec)


json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)

print(open('testjson.txt').read())

P = json.load(open('testjson.txt'))

print(P)


F = open('data.bin', 'wb') # Open binary output file

import struct

data = struct.pack('>i4sh', 7, b'spam', 8) # Make packed binary data

print(data)

F.write(data) # Write byte string

F.close()


F = open('data.bin', 'rb')

data = F.read() # Get packed binary data

print(data)

values = struct.unpack('>i4sh', data) # Convert to Python objects

print(values)


L = ['abc', [(1, 2), ([3], 3)], 5]

print(L[1])

print(L[1][1])

print(L[1][1][0])

print(L[1][1][0][0])


X = [1, 2, 3]

L = ['z', X, 'b'] # Embeds reference to X's object

D = {'x':X, 'y':2}


X[1] = 'surprise!' # Changes all three references!

print(L)

print(D)


L = [1, 2, 3]

D = {'a': 1, 'b': 2}

A = L[:] # Instead of A = L (or list(L))

B = D.copy() # Instead of B = D (ditto for sets)


A[1] = 'Ni!'

B['c'] = 'spam'

print(L, D)

print(A, B)


X = [1, 2, 3]

L = ['a', X[:], 'b'] # Embed copies of X's object

D = {'x':X[:], 'y':2}


import copy

X = copy.deepcopy(Y) # Fully copy an arbitrarily nested object Y


L1 = [1, ('a', 3)] # Same value, unique objects

L2 = [1, ('a', 3)]

print(L1 == L2, L1 is L2) # Equivalent? Same object?


S1 = 'spam'

S2 = 'spam'

print(S1 == S2, S1 is S2)


S1 = 'a longer string'

S2 = 'a longer string'

print(S1 == S2, S1 is S2)


L1 = [1, ('a', 3)]

L2 = [1, ('a', 2)]

print(L1 < L2, L1 == L2, L1 > L2) # Less, equal, greater: tuple of results


print(11 == '11') # Equality does not convert non-numbers

# print(11 >= '11') # 2.X compares by types name string: int, str

print(11 > 9.123) # Mixed numbers convert to highest type

print(str(11) >= '11', 11 >= int('11')) # Manual conversions force the issue


D1 = {'a':1, 'b':2}

D2 = {'a':1, 'b':3}

print(D1 == D2) # Dictionary equality: 2.X + 3.X

# print(D1 < D2) # Dictionary magnitude: 2.X only


print(list(D1.items()))

print(sorted(D1.items()))

print(sorted(D1.items()) < sorted(D2.items())) # Magnitude test in 3.X

print(sorted(D1.items()) > sorted(D2.items()))


L = [None] * 100

print(L)


print(bool(1))

print(bool('spam'))

print(bool({}))


L = [1, 2, 3]

M = ['X', L, 'Y'] # Embed a reference to L

print(M)

L[1] = objects # Changes M too

print(M)


L = [1, 2, 3]

M = ['X', L[:], 'Y'] # Embed a copy of L (or list(L), or L.copy())

L[1] = 0

print(L)

print(M)


L = [4, 5, 6]

X = L * 4 # Like [4, 5, 6] + [4, 5, 6] + ...

Y = [L] * 4 # [L] + [L] + ... = [L, L,...]

print(X)

print(Y)

L[1] = 0 # Impacts Y but not X

print(X)

print(Y)


L = [4, 5, 6]

Y = [list(L)] * 4 # Embed a (shared) copy of L

L[1] = 0

print(Y)


Y[0][1] = 99 # All four copies are still the same

print(Y)


L = [4, 5, 6]

Y = [list(L) for i in range(4)]

print(Y)

Y[0][1] = 99

print(Y)


L = ['grail'] # Append reference to same object

L.append(L) # Generates cycle in object: [...]

print(L)


T = (1, 2, 3)

# T[2] = 4 # Error!

T = T[:2] + (4,) # OK: (1, 2, 4)



