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









