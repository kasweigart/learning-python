# Lists and Dictionaries



# Lists


print(len([1, 2, 3])) # Length

print([1, 2, 3] + [4, 5, 6]) # Concatenation

print(['Ni!'] * 4) # Repitition


print(str([1, 2]) + '34') # Same as '[1, 2]' + '34'

print([1, 2] + list('34')) # Same as [1, 2] + ['3', '4']


print(3 in [1, 2, 3]) # Membership

for x in [1, 2, 3]: # Iteration (2.X uses: print x,)
    print(x)


res = [c * 4 for c in 'SPAM'] # List comprehension

print(res)


res = []

for c in 'SPAM':
    res.append(c * 4)

print(res)


print(list(map(abs, [-1, -2, 0, 1, 2]))) # Map a function across a sequence


L = ['spam', 'Spam', 'SPAM!']

print(L[2]) # Offsets start at zero

print(L[-2]) # Negative: count from the right

print(L[1:]) # Slicing fetches sections


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[1])

print(matrix[1][1])

print(matrix[2][0])


L = ['spam', 'Spam', 'SPAM!']

L[1] = 'eggs' # Index assignment

print(L)

L[0:2] = ['eat', 'more'] # Slice assignment: delete+insert

print(L) # Replaces items 0,1


L = [1, 2, 3]

L[1:2] = [4, 5] # Replacement/insertion

print(L)

L[1:1] = [6, 7] # Insertion (replace nothing)

print(L)

L[1:2] = [] # Deletion (insert nothing)

print(L)


L = [1]

L[:0] = [2, 3, 4] # Insert all at :0, an empty slcie at front

print(L)

L[len(L):] = [5, 6, 7] # Insert all at len(L):, an empty slice at end

print(L)

L.extend([8, 9, 10]) # Insert all at end, named method

print(L)


L = ['eat', 'more', 'SPAM!']

L.append('please') # Append method call: add item at end

print(L)

L.sort() # Sort list items ('S' < 'e')

print(L)


L = ['abc', 'ABD', 'aBe']

L.sort() # Sort with mixed case

print(L)


L = ['abc', 'ABD', 'aBe']

L.sort(key=str.lower) # Normalize to lowercase

print(L)

L = ['abc', 'ABD', 'aBe']

L.sort(key=str.lower, reverse=True) # Change sort order

print(L)

