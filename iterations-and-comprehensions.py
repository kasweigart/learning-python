# Iterations and Comprehensions



for x in [1,2,3,4]: print(x**2,end=' ') # In 2.X: print x**2

for x in (1,2,3,4):print(x**3,end=' ')

for x in 'spam':print(x*2,end=' ')


print(open('script2.py').read())


f = open('script2.py') # Read a four-line script in this directory

print(f.readline()) # readline loads one line at a time

print(f.readline())

print(f.readline())

print(f.readline()) # Last lines may have a \n or not

print(f.readline()) # Returns an empty string at end-of-file


f = open('script2.py') # __next__ loads one line on each call too

print(f.__next__()) # But raises an exception at end-of-file

print(f.__next__()) # Use f.next() in 2.X, or next(f) in 2.x or 3.X

print(f.__next__())

print(f.__next__())

# print(f.__next__()) # StopIteration exception


for line in open('script2.py'): # Use file iterators to read by lines
    print(line.upper(), end='')


for line in open('script2.py').readlines():
    print(line.upper(), end='')


f = open('script2.py')

while True:
    line = f.readline()
    if not line: break
    print(line.upper(), end='')


f= open('script2.py')

print(f.__next__()) # Call iteration method directly

print(f.__next__())

f = open('script2.py')

print(next(f)) # The next(f) built-in calls f.__next__() in 3.X

print(next(f)) # next(f) => [3.X: f.__next__()], [2.X: f.next()]


L = [1,2,3]

I = iter(L) # Obtain an iterator object from an iterable

print(I.__next__()) # Call iterator's next to advance to next item

print(I.__next__()) # Or use I.next() in 2.X, next(I) in either line

print(I.__next__())

# print(I.__next__()) # StopIteration Exception


f = open('script2.py')

print(iter(f) is f)

print(iter(f) is f.__iter__())

print(f.__next__())


L = [1,2,3]

print(iter(L) is L)

# print(L.__next__()) # AttributeError: 'list' object has no attribute '__next__'

I = iter(L)

print(I.__next__())

print(next(I)) # Same as I.__next__()


L=[1,2,3]

for X in L: # Automatic iteration
    print(X**2, end=' ') # Obtains iter, calls __next__, catches exceptions


I = iter(L) # Manual iteration: what for loops usually do

while True:
    try: # try statement catches exceptions
        X = next(I) # Or call I.__next__ in 3.X
    except StopIteration:
        break
    print(X**2, end=' ')


D = {'a': 1, 'b': 2, 'c': 3}

for key in D.keys():
    print(key, D[key])


I = iter(D)

print(next(I))

print(next(I))

print(next(I))

# print(next(I)) # StopIteration Exception


for key in D:
    print(key, D[key])


import os

P = os.popen('dir')

print(P.__next__())

print(P.__next__())

# print(next(P)) # TypeError: '_wrap_close' object is not an iterator


P = os.popen('dir')

I = iter(P)

print(next(I))

print(I.__next__())







