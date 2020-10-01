# Advanced Function Topics



def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:]) # Call myself recursively

print(mysum([1,2,3,4,5]))


def mysum(L):
    print(L) # Trace recursive levels
    if not L: # L shorter at each level
        return 0
    else:
        return L[0] + mysum(L[1:])

print(mysum([1,2,3,4,5]))


def mysum(L):
    return 0 if not L else L[0] + mysum(L[1:]) # Use ternary expression

def mysum(L):
    return L[0] if len(L) == 1 else L[0] + mysum(L[1:]) # Any type, assume one

def mysum(L):
    first, *rest = L
    return first if not rest else first + mysum(rest) # Use 3.X ext seq assign


print(mysum([1])) # mysum([]) fails in last 2

print(mysum([1,2,3,4,5]))

print(mysum(('s', 'p', 'a', 'm'))) # But various types work now

print(mysum(['spam', 'eggs', 'ham']))


def mysum(L):
    if not L: return 0
    return nonempty(L) # Call a function that calls me

def nonempty(L):
    return L[0] + mysum(L[1:]) # Indirectly recursive

print(mysum([1.1,2.2,3.3,4.4]))


L = [1,2,3,4,5]

sum = 0

while L:
    sum += L[0]
    L = L[1:]

print(sum)


L = [1,2,3,4,5]

sum = 0

for x in L: sum += x

print(sum)


import sys

print(sys.getrecursionlimit()) # 1000 calls deep default

sys.setrecursionlimit(10000) # Allow deeper nesting

# print(help(sys.setrecursionlimit)) # Read more about it


def echo(message): # Name echo assigned to function object
    print(message)

echo('Direct call') # Call object through original name

x = echo # Now x references the function too

x('Indirect call') # Call object through name by adding ()


def indirect(func, arg):
    func(arg) # Call the passed-in object by adding ()

indirect(echo, 'Argument call!') # Pass the function to another function


schedule = [ (echo, 'Spam!'), (echo, 'Ham!')]

for (func, arg) in schedule:
    func(arg) # Call functions embedded in containers


def make(label): # Make a function but don't call it
    def echo(message):
        print(label + ':' + message)
    return echo

F = make('Spam') # Label in enclosing scope is required

F('Ham') # Call the function that make returned

F('Eggs!')


def func(a):
    b = 'spam'
    return b * a

print(func(8))


print(func.__name__)

print(dir(func))


print(func.__code__)

print(dir(func.__code__))

print(func.__code__.co_varnames)

print(func.__code__.co_argcount)


print(func)

func.count = 0

func.count += 1

print(func.count)


func.handles = 'Button-Press'

print(func.handles)

print(dir(func))


def f(): pass

print(dir(f))

print(len(dir(f)))

print([x for x in dir(f) if not x.startswith('__')])


def func(a, b, c):
    return a + b + c

print(func(1, 2, 3))


def func(a: 'spam', b: (1, 10), c: float) -> int:
    return a + b + c

print(func(1, 2, 3))


print(func.__annotations__)


def func(a: 'spam', b, c: 99):
    return a + b + c

print(func(1,2,3))

print(func.__annotations__)

for arg in func.__annotations__:
    print(arg, '=>', func.__annotations__[arg])


def func(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6) -> int:
    return a + b + c

print(func(1,2,3))

print(func()) # 4 + 5 + 6 (all defaults)

print(func(1, c=10)) # 1 + 5 + 10 (keywords work normally)

print(func.__annotations__)


def func(a:'spam'=4, b:(1,10)=5, c:float=6)->int:
    return a + b + c

print(func(1,2)) # 1 + 2 + 6

print(func.__annotations__)


def func(x,y,z): return x + y + z

print(func(2,3,4))


f = lambda x,y,z: x + y + z

print(f(2,3,4))


x = (lambda a='fee', b='fie', c='foe': a + b + c)

print(x('wee'))


def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x) # Title in enclosing def scope
    return action # Return a function object

act = knights()

msg = act('robin') # 'robin' passed to x

print(msg)

print(act) # act: a function, not its result


L = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4] # Inline function definition. A list of three callable functions

for f in L:
    print(f(2)) # Prints 4, 8, 16

print(L[0](3)) # Prints 9


def f1(x): return x ** 2

def f2(x): return x ** 3 # Define named functions

def f3(x): return x ** 4


L = [f1, f2, f3] # Reference by name

for f in L:
    print(f(2)) # Prints 4, 8, 16

print(L[0](3)) # Prints 9


key = 'got'

print({'already': (lambda: 2 + 2), 'got': (lambda: 2 * 4), 'one': (lambda: 2 ** 6)}[key]())


def f1(): return 2 + 2

def f2(): return 2 * 4

def f3(): return 2 ** 6

key = 'one'

print({'already': f1, 'got': f2, 'one': f3}[key]())


lower = (lambda x, y: x if x < y else y)

print(lower('bb', 'aa'))

print(lower('aa', 'bb'))


import sys

showall = lambda x: list(map(sys.stdout.write, x)) # 3.X: must use list

t = showall(['spam\n', 'toast\n', 'eggs\n']) # 3.X: can use print


showall = lambda x: [sys.stdout.write(line) for line in x]

t = showall(('bright\n', 'side\n', 'of\n', 'life\n'))


showall = lambda x: [print(line, end='') for line in x] # Same: 3.X only

showall = lambda x: print(*x, sep='', end='') # Same: 3.X only


def action(x):
    return (lambda y: x + y) # Make and return function, remember x

act = action(99)

print(act)

print(act(2)) # Call what action returned


counters = [1,2,3,4]

updated = []

for x in counters:
    updated.append(x + 10) # Add 10 to each item

print(updated)


def inc(x): return x + 10 # Function to be run

print(list(map(inc, counters))) # Collect results


print(map(lambda x: x + 3, counters)) # Function expression


def mymap(func, seq):
    res = []
    for x in seq: res.append(func(x))
    return res


print(list(map(inc, [1,2,3]))) # Built-in is an iterable

print(mymap(inc, [1,2,3])) # Ours builds a list (see generators)


print(pow(3,4)) # 3**4

print(list(map(pow, [1,2,3], [2,3,4]))) # 1**2, 2**3, 3**4


print(list(map(inc, [1,2,3,4])))

print([inc(x) for x in [1,2,3,4]]) # Use parens to generate items instead


print(list(range(-5,5))) # An iterable in 3.X

print(list(filter((lambda x: x > 0), range(-5,5)))) # An iterable in 3.X


res = []

for x in range(-5,5): # The statement equivalent
    if x > 0:
        res.append(x)

print(res)


print([x for x in range(-5,5) if x > 0]) # Use () to generate items


from functools import reduce

print(reduce((lambda x,y: x + y), [1,2,3,4])) # Import in 3.X, not in 2.X

print(reduce((lambda x,y: x * y), [1,2,3,4]))


L = [1,2,3,4]

res = L[0]

for x in L[1:]:
    res = res + x

print(res)


def myreduce(function, sequence):
    tally = sequence[0]
    for next in sequence[1:]:
        tally = function(tally, next)
    return tally

print(myreduce((lambda x,y: x + y), [1,2,3,4,5]))

print(myreduce((lambda x,y: x * y), [1,2,3,4,5]))


import operator, functools

print(functools.reduce(operator.add, [2,4,6])) # Function-based +

print(functools.reduce((lambda x,y: x + y), [2,4,6]))












