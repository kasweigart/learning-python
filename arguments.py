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





