# Dictionaries

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}

print(D['food']) # Fetch value of key 'food'

D['quantity'] += 1 # Add 1 to 'quantity' value

print(D)

D = {}
D['name'] = 'Bob' # Creates key by assignment
D['job'] = 'dev'
D['age'] = 40

print(D)
print(D['name'])

bob1 = dict(name='Bob', job='dev', age=40) # Keywords
print(bob1)

bob2 = dict(zip(['name', 'job', 'age'], ['Bob','dev', 40])) # Zipping
print(bob2)

rec = {
    'name': {'first': 'Bob', 'last': 'Smith'},
    'jobs': ['dev', 'mgr'],
    'age': 40.5
}

print(rec['name']) # Nested dict
print(rec['name']['last']) # Index the nested dict

print(rec['jobs']) # Nested list
print(rec['jobs'][-1]) # Index the nested list

rec['jobs'].append('janitor') # Expand Bob's job description in place
print(rec)

D = {'a': 1, 'b': 2, 'c': 3}
D['e'] = 99 # Assigning new keys grows dicts
print(D)

# print(D['f']) Error

print('f' in D)

if not 'f' in D: # Python's sole selection statement
    print('missing')
    print('no, really...') # Statement blocks are indented

value = D.get('x', 0) # Index but with a default
print(value)

value = D['x'] if 'x' in D else 0 # if/else expression form
print(value)

D = {'a': 1, 'b': 2, 'c': 3}

Ks = list(D.keys()) # Unordered keys list
print(Ks)

Ks.sort() # Ordered keys list
print(Ks)

for key in Ks: # Itereate through sorted keys
    print(key, '=>', D[key])

for key in sorted(D):
    print(key, '=>', D[key])

for c in 'spam':
    print(c.upper())

x = 4
while x > 0:
    print('spam!' * x)
    x -= 1

squares = [x ** 2 for x in [1,2,3,4,5]]
print(squares)

squares = []
for x in [1,2,3,4,5]:
    squares.append(x ** 2)
print(squares)






