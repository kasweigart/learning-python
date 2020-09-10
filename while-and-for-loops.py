# while and for Loops



# while True:
#     print('Type Ctrl-C to stop me!')


x = 'spam'

while x: # While x is not empty
    print(x, end=' ') # In 2.X use print x,
    x = x[1:] # Strip first character off x


a=0; b=10

while a < b: # One wat to code counter loops
    print(a, end=' ')
    a += 1 # Or, a = a + 1


x = 10

while x:
    x = x-1 # Or, x -= 1
    if x % 2 != 0: continue # Odd? -- skip print
    print(x, end=' ')


x = 10

while x:
    x = x-1
    if x % 2 == 0: # Even? -- print
        print(x, end=' ')


# while True:
#     name = input('Enter name: ')
#     if name == 'stop': break
#     age = input('Enter age: ')
#     print('Hello', name, '=>', int(age) ** 2)


y = 10

x = y // 2 # For some y > 1

while x > 1:
    if y % x == 0: # Remainder
        print(y, 'has factor', x)
        break
    x -= 1 # Skip else
else:
    print(y, 'is prime') # Normal exit


for x in ['spam', 'eggs', 'ham']:
    print(x, end=' ')


sum = 0

for x in [1, 2, 3, 4]:
    sum = sum + x

print(sum)


prod = 1

for item in [1, 2, 3, 4]: prod *= item

print(prod)


S = 'lumberjack'

T = ('and', "I'm", 'okay')

for x in S: print(x, end=' ') # Iterate over a string

for x in T: print(x, end=' ') # Iterate over a tuple


T = [(1,2),(3,4),(5,6)]

for (a,b) in T: # Tuple assignment at work
    print(a,b)


D = {'a': 1, 'b': 2, 'c': 3}

for key in D:
    print(key, '=>', D[key]) # Use dict keys iterator and index


print(list(D.items()))

for (key, value) in D.items():
    print(key, '=>', value) # Iterate over both keys and values


print(T)

for both in T:
    a, b = both # Manual assignment equivalent
    print(a, b) # 2.X prints with enclosing tuple '()'


((a,b),c) = ((1,2),3) # Nested sequences work too

for ((a,b),c) in [((1,2),3), ((4,5),6)]: print(a,b,c)


for ((a,b), c) in [([1,2], 3), ['XY', 6]]: print(a,b,c)


a,b,c = (1,2,3) # Tuple assignment

print(a,b,c)

for (a,b,c) in [(1,2,3), (4,5,6)]: # Used in for loop
    print(a,b,c)


a,*b,c = (1,2,3,4) # Extended seq assignment

print(a,b,c)


for (a,*b,c) in [(1,2,3,4), (5,6,7,8)]:
    print(a,b,c)


for all in [(1,2,3,4), (5,6,7,8)]: # Manual slicing in 2.X
    a,b,c = all[0], all[1:3], all[3]
    print(a,b,c)


items = ['aaa', 111, (4,5), 2.01] # A set of objects

tests = [(4,5), 3.14] # Keys to search for

for key in tests: # For all keys
    for item in items: # For all items
        if item == key: # Check for match
            print(key, 'was found')
            break
    else:
        print(key, 'not found!')


for key in tests: # For all keys
    if key in items: # Let Python check for a match
        print(key, 'was found')
    else:
        print(key, 'not found!')


seq1 = 'spam'

seq2 = 'scam'

res = []

for x in seq1: # Scan first sequence
    if x in seq2: # Common item?
        res.append(x) # Add result to end

print(res)


print([x for x in seq1 if x in seq2]) # Let Python collect results


print(list(range(5)), list(range(2, 5)), list(range(0, 10, 2)))


print(list(range(-5, 5)))

print(list(range(5, -5, -1)))


for i in range(3):
    print(i, 'Pythons')


X = 'spam'

for item in X: print(item, end=' ') # Simple iteration


i = 0

while i < len(X): # while loop iteration
    print(X[i], end=' ')
    i += 1


print(X)

print(len(X)) # Length of string

print(list(range(len(X)))) # All legal offsets into X

for i in range(len(X)): print(X[i], end=' ') # Manual range/len iteration


for item in X: print(item, end=' ') # Use simple iteration if you can


S = 'spam'

for i in range(len(S)): # For repeat counts 0..3
    S = S[1:] + S[:1] # Move front item to end
    print(S, end=' ')


print(S)

for i in range(len(S)): # For positions 0..3
    X = S[i:] + S[:i] # Rear part + front part
    print(X, end=' ')


L = [1,2,3]

for i in range(len(L)): # Works on any sequence type
    X = L[i:] + L[:i]
    print(X, end=' ')


S = 'abcdefghijk'

print(list(range(0, len(S), 2)))

for i in range(0, len(S), 2): print(S[i], end=' ')


S = 'abcdefghijk'

for c in S[::2]: print(c, end=' ')


L = [1,2,3,4,5]

for x in L:
    x+=1 # Changes x, not L

print(L)

print(x)


L = [1,2,3,4,5]

for i in range(len(L)): # Add one to each item in L
    L[i] += 1 # Or L[i] = L[i] + 1

print(L)


i = 0

while i < len(L):
    L[i] += 1
    i += 1

print(L)


print([x + 1 for x in L])


L1 = [1,2,3,4]

L2 = [5,6,7,8]

print(zip(L1, L2))

print(list(zip(L1, L2))) # list() required in 3.X, not 2.X


for (x,y) in zip(L1, L2):
    print(x,y, '--', x+y)


T1, T2, T3, = (1,2,3), (4,5,6), (7,8,9)

print(T3)

print(list(zip(T1, T2, T3))) # Three tuples for three arguments


S1 = 'abc'

S2 = 'xyz123'

print(list(zip(S1, S2))) # Truncates at len(shortest)


print(list(map(ord, 'spam')))


res = []

for c in 'spam': res.append(ord(c))

print(res)






