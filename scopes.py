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




















