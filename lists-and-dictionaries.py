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


L = ['abc', 'ABD', 'aBe']

print(sorted(L, key=str.lower, reverse=True)) # Sorting built-in


L = ['abc', 'ABD', 'aBe']

print(sorted([x.lower() for x in L], reverse=True)) # Pretransform items: differs!


L = [1, 2]

L.extend([3, 4, 5]) # Add many items at end (like in-place +)

print(L)

L.pop() # Delete and return last item (by default: -1)

print(L)

L.reverse() # In-place reversal method

print(L)

print(list(reversed(L))) # Reversal built-in with a result (iterator)


L = ['spam', 'eggs', 'ham']

print(L.index('eggs')) # Index OF an object (search/find)

L.insert(1, 'toast') # Insert at position

print(L)

L.remove('eggs') # Delete by value

print(L)

print(L.pop(1)) # Delete by position

print(L)

print(L.count('spam')) # Number of occurances


L = ['spam', 'eggs', 'ham', 'toast']

del L[0] # Delete one item

print(L)


del L[1:] # Delete an entire section

print(L) # Same as L[1:] = []


L = ['Already', 'got', 'one']

L[1:] = []

print(L)


L[0]= []

print(L)



# Dictionaries


D = {'spam': 2, 'ham': 1, 'eggs': 3} # Make a dictionary

print(D['spam']) # Fetch a value by key

print(D) # Order is 'scrambled'


print(len(D)) # Number of entries in dictionary

print('ham' in D) # Key membership test alternative

print(list(D.keys())) # Create a new list of D's keys


print(D)

D['ham'] = ['grill', 'bake', 'fry'] # Change entry (value=list)

print(D)

del D['eggs'] # Delete entry

print(D)

D['brunch'] = 'Bacon' # Add new entry

print(D)


D = {'spam': 2, 'ham': 1, 'eggs': 3}

print(list(D.values()))

print(list(D.items()))


print(D.get('spam')) # A key that is there

print(D.get('toast')) # A key that is missing

print(D.get('toast', 88))


print(D)

D2 = {'toast': 4, 'muffin': 5}

D.update(D2)

print(D)


# Pop a dictionary by key

print(D)

print(D.pop('muffin'))

print(D.pop('toast')) # Delete and return from a key

print(D)


# Pop a list by position

L = ['aa', 'bb', 'cc', 'dd']

print(L.pop()) # Delete and return from the end

print(L)

print(L.pop(1)) # Delete from a specific position

print(L)


table = {'1975': 'Holy Grail', '1979': 'Life of Brian', '1983': 'The Meaning of Life'} # Key: Value

year = '1983'

movie = table[year] # dictionary[Key] => Value

print(movie)


for year in table: # Same as: for year in table.keys()
    print(year + '\t' + table[year])


table = {'Holy Grail': '1975', 'Life of Brain': '1979', 'The Meaning of Life': '1983'} # Key=>Value (title=>year)

print(table['Holy Grail'])

print(list(table.items()))

print([title for (title, year) in table.items() if year == '1975'])


K = 'Holy Grail'

print(table[K]) # Key=>Value (normal usage)


V = '1975'

print([key for (key, value) in table.items() if value == V]) # Value=>Key

print([key for key in table.keys() if table[key] == V]) # Ditto


L = []

# L[99] = 'spam' # IndexError: list assignment index out of range


D = {}

D[99] = 'spam'

print(D[99])

print(D)


table = {1975: 'Holy Grail', 1979: 'Life of Brian', 1983: 'The Meaning of Life'} # Keys are integers, not strings

print(table[1975])

print(list(table.items()))


Matrix = {}

Matrix[(2, 3, 4)] = 88

Matrix[(7, 8, 9)] = 99

X = 2; Y = 3; Z = 4 # ; seperates statements: see Chapter 10

print(Matrix[X, Y, Z])

print(Matrix)

# print(Matrix[(2, 3, 6)]) # Not physically stored


if (2, 3, 6) in Matrix: # Check for key before fetch
    print(Matrix[(2, 3, 6)]) # See Chapters 10 and 12 for if/else
else:
    print(0)


try:
    print(Matrix[(2, 3, 6)]) # Try to index
except KeyError: # Catch and recover
    print(0) # See Chapters 10 and 34 for try/except


print(Matrix.get((2, 3, 4), 0)) # Exists: fetch and return

print(Matrix.get((2, 3, 6), 0)) # Doesn't exist: use default arg


rec = {}

rec['name'] = 'Bob'

rec['age'] = 40.5

rec['job'] = 'developer/manager'

print(rec['name'])


rec = {'name': 'Bob', 'jobs': ['developer', 'manager'], 'web': 'www.bobs.org/~Bob', 'home': {'state': 'Overworked', 'zip': 12345}}

print(rec['name'])

print(rec['jobs'])

print(rec['jobs'][1])

print(rec['home']['zip'])


db = []

db.append(rec) # A list 'database'

print(db[0]['jobs'])


db = {}

db['bob'] = rec # A dictionary 'database'

print(db['bob']['jobs'])


{'name': 'Bob', 'age': 40} # Traditional literal expression

D = {} # Assign by keys dynamically

D['name'] = 'Bob'

D['age'] = 40

dict(name='Bob', age=40) # dict keyword argument form

dict([('name', 'Bob'), ('age', 40)]) # dict key/value tuples form


# dict(zip(keyslist, valueslist)) # Zipped key/value tuples form (ahead)


print(dict.fromkeys(['a', 'b'], 0))


L = ['Bob', 40.5, ['dev', 'mgr']] # List-based 'record'

print(L[0])

print(L[1]) # Positions/numbers for fields

print(L[2][1])


D = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}

print(D['name'])

print(D['age']) # Dictionary-based 'record'

print(D['jobs'][1]) # Names mean more than numbers


D = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])

print(D['name'])

D['jobs'].remove('mgr')

print(D)


D = {}

D['state1'] = True # A visited-state dictionary

print('state1' in D)

S = set()

S.add('state1') # Same but with sets

print('state1' in S)

print(D)
















