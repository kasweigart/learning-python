# The Documentation Interlude



import sys

print(dir(sys))


print(len(dir(sys))) # Number of names in sys

print(len([x for x in dir(sys) if not x.startswith('__')])) # Non __X names only

print(len([x for x in dir(sys) if not x[0] == '_'])) # non underscore names


print(dir([]))

print(dir(''))


print(len(dir([])), len([x for x in dir([]) if not x.startswith('__')]))

print(len(dir('')), len([x for x in dir('') if not x.startswith('__')]))


print([a for a in dir(list) if not a.startswith('__')])

print([a for a in dir(dict) if not a.startswith('__')])


def dir1(x): return [a for a in dir(x) if not a.startswith('__')] # See Part IV

print(dir1(tuple))


print(dir(str) == dir('')) # Same result, type name or literal

print(dir(list) == dir([]))


import sys

print(sys.__doc__)


print(sys.getrefcount.__doc__)


print(int.__doc__)

print(map.__doc__)


import sys

# help(sys.getrefcount)


# help(sys)


S = 'spam'

L = []

print([ord(c) for c in S])


for i in range(50):
    print('hello %d\n\a' % i)


D = dict(a=1,b=2,c=3)

for i in sorted(D.items()):
    print(i)












