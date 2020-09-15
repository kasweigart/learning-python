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


R = range(5)

print(R) # Ranges are iterables in 3.X

I = iter(R) # Use iteration protocol to produce results

print(next(I))

print(next(I))

print(list(range(5))) # Or use list to collect all results at once


E = enumerate('spam') # enumerate is an iterable too

print(E)

I = iter(E)

print(next(I)) # Generate results with iteration protocol

print(next(I)) # Or use list to force generation to run

print(list(enumerate('spam')))


L = [1,2,3,4,5]

for i in range(len(L)):
    L[i] += 10

print(L)


L = [x + 10 for x in L]

print(L)

res = []

for x in L:
    res.append(x + 10)

print(res)


f = open('script2.py')

lines = f.readlines()

print(lines)


lines = [line.rstrip() for line in lines]

print(lines)


lines = [line.rstrip() for line in open('script2.py')]

print(lines)


print([line.upper() for line in open('script2.py')])

print([line.rstrip().upper() for line in open('script2.py')])

print([line.split() for line in open('script2.py')])

print([line.replace(' ', '!') for line in open('script2.py')])

print([('sys' in line, line[:5]) for line in open('script2.py')])


lines = [line.rstrip() for line in open('script2.py') if line[0] == 'p']

print(lines)


res = []

for line in open('script2.py'):
    if line[0] == 'p':
        res.append(line.rstrip())

print(res)


print([line.rstrip() for line in open('script2.py') if line.rstrip()[-1].isdigit()])


print([x + y for x in 'abc' for y in 'lmn'])


res = []

for x in 'abc':
    for y in 'lmn':
        res.append(x + y)

print(res)


for line in open('script2.py'): # Use file iterators
    print(line.upper(), end='')


uppers = [line.upper() for line in open('script2.py')]

print(uppers)


print(map(str.upper, open('script2.py'))) # map is itself an iterable in 3.X


print(list(map(str.upper, open('script2.py'))))


print(sorted(open('script2.py')))

print(list(zip(open('script2.py'), open('script2.py'))))

print(list(enumerate(open('script2.py'))))

print(list(filter(bool, open('script2.py')))) # nonempty=True

import functools, operator

print(functools.reduce(operator.add, open('script2.py')))


print(list(open('script2.py')))

print(tuple(open('script2.py')))

print('&&'.join(open('script2.py')))


a,b,c,d = open('script2.py') # Sequence assignment

print(a,d)


a, *b = open('script2.py') # 3.X extended form

print(a, b)


print('y = 2\n' in open('script2.py')) # Memebership test

print('x = 2\n' in open('script2.py'))


L = [11, 22, 33, 44] # Slice assignment

L[1:3] = open('script2.py')

print(L)


L = [11]

L.extend(open('script2.py')) # list.extend method

print(L)


L = [11]

L.append(open('script2.py')) # list.append does not iterate

print(L)

print(list(L[1]))


print(set(open('script2.py')))

print({line for line in open('script2.py')})

print({ix: line for ix, line in enumerate(open('script2.py'))})


print({line for line in open('script2.py') if line[0] == 'p'})

print({ix: line for (ix, line) in enumerate(open('script2.py')) if line[0] == 'p'})


print(list(line.upper() for line in open('script2.py'))) # See Chapter 20


print(sum([3,2,4,1,5,0])) # sum expects numbers only

print(any(['spam', '', 'ni']))

print(all(['spam', '', 'ni']))

print(max([3,2,5,1,4]))

print(min([3,2,5,1,4]))


print(max(open('script2.py'))) # Line with max/min string value

print(min(open('script2.py')))


def f(a,b,c,d): print(a,b,c,d, sep='&')

print(f(1,2,3,4))

print(f(*[1,2,3,4])) # Unpacks into arguments

print(f(*open('script2.py'))) # Iterates by lines too


X = (1,2)

Y = (3,4)

print(list(zip(X,Y))) # Zip tuples: returns an iterable

A, B = zip(*zip(X,Y)) # Unzip a zip!

print(A, B)


print(zip('abc', 'xyz')) # An iterable in Python 3.X (a list in 2.X)

print(list(zip('abc', 'xyz'))) # Force list of results in 3.X to display


Z = zip((1,2), (3,4)) # Unlike 2.X lists, cannot index, etc.

# print(Z[0]) # TypeError: 'zip' object is not subscriptable


M = map(lambda x: 2 ** x, range(3))

for i in M: print(i)

for i in M: print(i) # Unlike 2.X lists, one pass only (zip too)


R = range(10) # range returns an iterable, not a list

print(R)

I = iter(R) # Make an iterator from the range iterable

print(next(I))

print(next(I))

print(next(I))

print(list(range(10))) # To force a list if required


print(len(R)) # range also does len and indexing, but no others

print(R[0])

print(R[-1])

print(next(I)) # Continue taking from iterator, where left off

print(I.__next__()) # .next() becomes __next__(), but use new next()


M = map(abs, (-1,0,-1)) # map returns an iterable, not a list

print(M)

print(next(M)) # Use iterator manually: exhausts results

print(next(M)) # These do not support len() or indexing

print(next(M))

# print(next(M)) # StopIteration

for x in M: print(x) # map iterator is now empty: one pass only

M = map(abs, (-1,0,1)) # Make a new iterable/iterator to scan again

for x in M: print(x) # Iteration contexts auto call next()

print(list(map(abs, (-1,0,1)))) # Can force a real list if needed


Z = zip((1,2,3), (10,20,30)) # zip is the same: a one-pass iterator

print(Z)

print(list(Z))

for pair in Z: print(pair) # Exhausted after one pass

Z = zip((1,2,3), (10,20,30))

for pair in Z: print(pair) # Iterator used automatically or manually

Z = zip((1,2,3), (10,20,30)) # Manual iteration (iter() not needed)

print(next(Z))

print(next(Z))


print(filter(bool, ['spam', '', 'ni']))

print(list(filter(bool, ['spam', '', 'ni'])))


print([x for x in ['spam', '', 'ni'] if bool(x)])

print([x for x in ['spam', '', 'ni'] if x])


R = range(3) # range allows multiple iterators

# print(next(R)) # TypeError: range object is not an iterator

I1 = iter(R)

print(next(I1))

print(next(I1))

I2 = iter(R) # Two iterators on one range

print(next(I2))

print(next(I1)) # I1 is at a different spot than I2


Z = zip((1,2,3), (10,11,12))

I1 = iter(Z)

I2 = iter(Z) # Two iterators on one zip

print(next(I1))

print(next(I1))

print(next(I2)) # (3.X) I2 is at same spot as I1!


M = map(abs, (-1,0,1)) # Ditto for map (and filter)

I1 = iter(M); I2 = iter(M)

print(next(I1), next(I1), next(I2))

# print(next(I2)) # StopIteration: (3.X) Single scan is exhausted!


R = range(3) # But range allows many iterators

I1, I2 = iter(R), iter(R)

print([next(I1), next(I1), next(I1)])

print(next(I2)) # Multiple active scans, like 2.X lists


D = dict(a=1,b=2,c=3)

print(D)


K = D.keys()  # A view object in 3.X, not a list

print(K)


# print(next(K)) # TypeError: dict_keys object is not an iterator. Views are not iterators themselves


I = iter(K) # View iterables have an iterator,

print(next(I)) # which can be used manually

print(next(I)) # but does not support len(), index


for k in D.keys(): print(k, end=' ') # All iteration contexts use auto


K = D.keys()

print(list(K)) # Can still force a real list if needed

V = D.values() # Ditto for values() and items() views

print(V)

print(list(V)) # Need list() to display or index as list

# print(V[0]) # TypeError: 'dict_values' object does not support indexing

print(list(V)[0])

print(list(D.items()))

for (k, v) in D.items(): print(k, v, end=' ')


print(D) # Dicitonaries still produce an iterator

I = iter(D) # Returns next key on each iteration

print(next(I))

print(next(I))

for key in D: print(key, end=' ') # Still no need to call keys() to iterate, but keys is an iterable in #.X too!


print(D)

for k in sorted(D.keys()): print(k, D[k], end=' ')

for k in sorted(D): print(k, D[k], end=' ') # 'Best practice' key sorting








































