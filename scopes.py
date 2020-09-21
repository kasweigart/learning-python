# Scopes



X = 99 # Global (module) scope X

def func():
    X = 88 # Local (function) scope X: a different variable


# Global scope

X = 99 # X and func assigned in module: global

def func(Y): # Y and Z assigned in function: locals
    # Local scope
    Z = X + Y # X is a global
    return Z

func(1) # func in module: result=100


import builtins

print(dir(builtins))


print(zip) # The normal way


import builtins # The hard way: for customizations

print(builtins.zip)


print(zip is builtins.zip) # Same object, different lookups


def hider():
    open = 'spam' # Local variable, hides built-in here
    ...
    # open('data.txt') # Error: this no longer opens a file in this scope!


# open = 99 # Assign in global scope, hides built-in here too


print(len(dir(builtins)), len([x for x in dir(builtins) if not x.startswith('__')]))


X = 88 # Global X

def func(): # Local X: hides global, but we want this here
    X = 99

func()

print(X) # Prints 88: unchanged


X = 88 # Global X

def func():
    global X
    X = 99 # Global X: outside def

func()

print(X) # Prints 99


y,z = 1,2 # Global variables in module

def all_global():
    global x # Declare globals assigned
    x = y+z # No need to declare y,z: LEGB rule


X = 99 # Global scope name: not used

def f1():
    X = 88 # Encolsing def local
    def f2():
        print(X) # Reference made in nested def
    f2()

f1() # Prints 88; enclosing def local


def f1():
    X = 88
    def f2():
        print(X) # Remembers X in enclosing def scope
    return f2 # Return f2 but don't call it
    
action = f1() # Make, return function

print(action()) # Call it now: prints 88


def maker(N):
    def action(X): # Make and return action
        return X ** N # action retains N from enclosing scope
    return action


f = maker(2) # Pass 2 to argument N

print(f)


print(f(3)) # Pass 3 to X, N remembers 2: 3 ** 2

print(f(4)) # 4 ** 2


g = maker(3) # g remembers 3, f remembers 2

print(g(4)) # 4 ** 3

print(f(4)) # 4 ** 2


def maker(N):
    return lambda X: X ** N # lambda functions retain state too

h = maker(3)

print(h(4)) # 4 ** 3 again


def f1():
    X = 88
    def f2(X=X): # Remember enclosing scope X with defaults
        print(X)
    f2()

f1() # Prints 88


def f1():
    x = 88 # Pass x along instead of nesting
    f2(x) # Forward reference OK

def f2(x):
    print(x) # # Flat is still often better than nested!

f1()


def func():
    x = 4
    action = (lambda n: x ** n) # x remembered from enclosing def
    return action

x = func()

print(x(2)) # Prints 16, 4**2


def func():
    x=4
    action=(lambda n,x=x: x ** n) # Pass x in manually
    return action


def makeActions():
    acts = []
    for i in range(5): # Tries to remember each i
        acts.append(lambda x: i ** x) # But all remember the same last i!
    return acts

acts = makeActions()

print(acts[0])


print(acts[0](2)) # All are 4**2, 4=value of last i

print(acts[1](2)) # This should be 1**2 (1)

print(acts[2](2)) # This should be 2**2 (4)

print(acts[4](2)) # Only this should be 4**2 (16)


def makeActions():
    acts=[]
    for i in range(5): # Use defaults instead
        acts.append(lambda x,i=i: i**x) # Remember current i
    return acts

acts = makeActions()

print(acts[0](2)) # 0**2

print(acts[1](2)) # 1**2

print(acts[2](2)) # 2**2

print(acts[4](2)) # 4**2


def f1():
    x=99
    def f2():
        def f3():
            print(x) # Found in f1's local scope!
        f3()
    f2()

f1()


# def func():
#     nonlocal name1, name2 # OK here

# nonlocal X # nonlocal declaration not allowed at module level


def tester(start):
    state = start # Referencing nonlocals works normally
    def nested(label):
        print(label, state) # Remembers state in enclosing scope
    return nested

F = tester(0)

F('spam')

F('ham')


def tester(start):
    state = start # Each call gets its own state
    def nested(label):
        nonlocal state # Remembers state in enclosing scope
        print(label, state)
        state += 1 # Allowed to change it if nonlocal
    return nested

F = tester(0) 

F('spam') # Increments state on each call

F('ham')

F('eggs')


G = tester(42) # Make a new tester that starts at 42

G('spam')

G('eggs') # My state information updated to 43

F('bacon') # But F's is where it left off: at 3


# def tester(start):
#     def nested(label):
#         nonlocal state # Nonlocals must already exist in enclosing def!
#         state = 0
#         print(label, state)
#     return nested

# SyntaxError: no binding for nonlocal 'state' found


def tester(start):
    def nested(label):
        global state # Globals don't have to exist yet when declared
        state = 0 # This creates the name in the module now
        print(label, state)
    return nested

F = tester(0)

F('abc')

print(state)


# spam = 99

# def tester():
#     def nested():
#         nonlocal spam # Must be in a def, not the module!
#         print('Current=', spam)
#         spam+=1
#     return nested

# SyntaxError: no binding for nonlocal 'spam' found


def tester(start):
    state = start # Each call gets its own state
    def nested(label):
        nonlocal state # Remembers state in enclosing scope
        print(label, state)
        state += 1
    return nested

F = tester(0)

F('spam') # State visible within closure only

# F.state # AttributeError: 'function' object has no attribute 'state'


def tester(start):
    global state # Move it out to the module to change it
    state = start # global allows changes in module scope
    def nested(label):
        global state
        print(label, state)
        state += 1
    return nested

F = tester(0)

F('spam') # Each call increments shared global state

F('eggs')


G = tester(42) # Resets state's single copy in global scope

G('toast')

G('bacon')

G('ham') # But my counter has been overwritten!


class tester: # Class-based alternative (see Part VI)
    def __init__(self, start): # On object construction
        self.state = start # save state explicitly in new object
    def nested(self, label):
        print(label, self.state) # Referenec state explicitly
        self.state += 1 # Changes are always allowed

F = tester(0) # Create instance, invoke __init__

F.nested('spam') # F is passed to self

F.nested('ham')


G = tester(42) # Each instance gets new copy of state

G.nested('toast') # Changing one does not impact others

G.nested('bacon')

F.nested('eggs') # F's state is where it left off

print(F.state) # State may be accessed outside class


class tester:
    def __init__(self, start):
        self.state = start
    def __call__(self, label): # Intercept direct instance calls
        print(label, self.state) # So .nested() not required
        self.state += 1

H = tester(99)

H('juice') # Invokes __call__

H('pancakes')


def tester(start):
    def nested(label):
        print(label, nested.state) # nested is in enclosing scope
        nested.state += 1 # Change attr, not nested itself
    nested.state = start # Initial state after func defined
    return nested

F = tester(0)

F('spam') # F is a 'nested' with state attached

F('ham')

print(F.state)


G = tester(42) # G has own state, doesn't overwrite F's

G('eggs')

F('ham')

print(F.state) # State is accessible and per-call

print(G.state)

print(F is G) # Different function objects


def tester(start):
    def nested(label):
        print(label, state[0]) # Leverage in-place mutable change
        state[0] += 1 # Extra syntax, deep magic?
    state = [start]
    return nested


































