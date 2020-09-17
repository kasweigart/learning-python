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






