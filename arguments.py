# Arguments



def f(a): # a is assigned to (references) the passed object
    a = 99 # Changes local variable a only


b = 88

f(b) # a and b both reference same 88 initially

print(b) # b is not changed


def changer(a, b): # Arguments assigned references to objects
    a = 2 # Changes local name's value only
    b[0] = 'spam' # Changes shared object in place

X = 1

L = [1, 2] # Caller:

changer(X, L) # Pass immutable and mutable objects

print(X, L) # X is unchanged, L is different!


X = 1

a = X # They share the same object

a = 2 # Resets 'a' only, 'X' is still 1

print(X)


L = [1, 2]

b = L # They share the same object

b[0] = 'spam' # In-place change: 'L' sees the change too

print(L)


def multiple(x, y):
    x = 2 # Changes local names only
    y = [3, 4]
    return x, y # Return multiple new vlues in a tuple

X = 1

L = [1, 2]

X, L = multiple(X, L) # Assign results to caller's names

print(X, L)


def f(T): (a, (b, c)) = T


def f(a, b, c): print(a, b, c)

f(1, 2, 3)


f(c=3, b=2, a=1)


f(1, c=3, b=2) # a gets 1 by position, b and c passed by name


def f(a, b=2, c=3): print(a, b, c) # a required, b and c optional


f(1) # Use defaults

f(a=1)


f(1, c=6) # Choose defaults


def f(*args): print(args)


f()

f(1)

f(1,2,3,4)


def f(**args): print(args)

f()

f(a=1,b=2)


def f(a, *pargs, **kargs): print(a, pargs, kargs)

f(1, 2, 3, x=1, y=2)


def func(a,b,c,d): print(a,b,c,d)

args = (1,2)

args += (3,4) # Same as func(1,2,3,4)

func(*args)


args = {'a': 1, 'b': 2, 'c': 3}

args['d'] = 4

func(**args) # Same as func(a=1, b=2, c=3, d=4)


func(*(1,2), **{'d': 4, 'c': 3}) # Same as func(1,2,d=4,c=3)

func(1, *(2,3), **{'d': 4}) # Same as func(1,2,3,d=4)

func(1, c=3, *(2,), **{'d': 4}) # Same as func(1,2,c=3,d=4)

func(1, *(2,3), d=4) # Same as func(1,2,3,d=4)

func(1, *(2,), c=3, **{'d': 4}) # Same as func(1,2,c=3,d=4)


def kwonly(a, *b, c):
    print(a,b,c)

kwonly(1,2,c=3)

kwonly(a=1, c=3)

# kwonly(1,2,3) # TypeError: kwonly() missing 1 required keyword-only argument: 'c'


def kwonly(a,*,b,c):
    print(a,b,c)

kwonly(1,c=3,b=2)

kwonly(c=3,b=2,a=1)

# kwonly(1,2,3) # TypeError: kwonly() takes 1 positional argument but 3 were given

# kwonly(1) # kwonly() missing 2 required keyword-only arguments: 'b' and 'c'


def kwonly(a, *, b='spam', c='ham'):
    print(a,b,c)

kwonly(1)

kwonly(1, c=3)

kwonly(a=1)

kwonly(c=3, b=2, a=1)

# kwonly(1,2) # TypeError: kwonly() takes 1 positional argument but 2 were given


def kwonly(a, *, b, c='spam'):
    print(a,b,c)

kwonly(1, b='eggs')

# kwonly(1, c='eggs') # TypeError: kwonly() missing 1 required keyword-only argument: 'b'

# kwonly(1,2) # TypeError: kwonly() takes 1 positional argument but 2 were given


def kwonly(a, *, b=1, c, d=2):
    print(a,b,c,d)

kwonly(3, c=4)

kwonly(3, c=4, b=5)

# kwonly(3) # TypeError: kwonly() missing 1 required keyword-only argument: 'c'

# kwonly(1,2,3) # TypeError: kwonly() takes 1 positional argument but 3 were given


def kwonly(a, *, b=1, c, d=2):
    print(a,b,c,d)

kwonly(3, c=4)

kwonly(3, c=4, b=5)

# kwonly(3) # TypeError: kwonly() missing 1 required keyword-only argument: 'c'

# kwonly(1,2,3) # TypeError: kwonly() takes 1 positional argument but 3 were given


# def kwonly(a, **pargs, b, c): # SyntaxError: invalid syntax

# def kwonly(a, **, b, c): # SyntaxError: invalid syntax


# def(a, *b, **d, c=6): print(a,b,c,d) # Keyword-only before **!

def f(a, *b, c=6, **d): print(a,b,c,d) # Collect args in header

f(1, 2, 3, x=4, y=5) # Default used

f(1, 2, 3, x=4, y=5, c=7) # Override default

f(1, 2, 3, c=7, x=4, y=5) # Anywhere in keywords


def f(a, c=6, *b, **d): print(a,b,c,d) # c is not keyword-only here!

f(1, 2, 3, x=4)


def f(a, *b, c=6, **d): print(a,b,c,d) # KW-only between * and **

f(1, *(2,3), **dict(x=4,y=5)) # Unpack args at call

# f(1, *(2,3), **dict(x=4,y=5), c=7) # SyntaxError: invalid syntax - Keywords before **args!

f(1, *(2,3), c=7, **dict(x=4, y=5)) # Override default

f(1, c=7, *(2,3), **dict(x=4, y=5)) # After or before *

f(1, *(2,3), **dict(x=4, y=5, c=7)) # Keyword-only in **


def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res


def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first


def min3(*args):
    tmp = list(args) # Or, in Python 2,4+: return sorted(args)[0]
    tmp.sort()
    return tmp[0]


print(min1(3,4,1,2))
print(min2('bb','aa'))
print(min3([2,2],[1,1],[3,3]))


def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res


def lessthan(x, y): return x < y # See also: lambda, eval
def grtrthan(x, y): return x > y

print(minmax(lessthan, 4,2,1,5,6,3)) # Self-test code
print(minmax(grtrthan, 4,2,1,5,6,3))


from inter2 import intersect, union

s1, s2, s3 = 'SPAM', 'SCAM', 'SLAM'

print(intersect(s1, s2), union(s1, s2)) # Two operands

print(intersect([1,2,3],(1,4))) # Mixed types

print(intersect(s1,s2,s3)) # Three operands

print(union(s1,s2,s3))


def tester(func, items, trace=True):
    for i in range(len(items)):
        items = items[1:] + items[:1]
        if trace: print(items)
        print(sorted(func(*items)))

tester(intersect, ('a', 'abcdefg', 'abdst', 'albmcnd'))

tester(union, ('a', 'abcdefg', 'adbst', 'albmcnd'), False)

tester(intersect, ('ba', 'abcdefg', 'abdst', 'albmcnd'), False)


intersect([1,2,1,3], (1,1,4))

union([1,2,1,3], (1,1,4))

tester(intersect, ('ababa', 'abcdefg', 'aaab',), False)






















