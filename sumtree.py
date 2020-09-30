def sumtree(L):
    tot = 0
    for x in L: # For each item at this level
        if not isinstance(x, list):
            tot += x # Add numbers directly
        else:
            tot += sumtree(x) # Recur for sublists
    return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]] # Arbitrary nesting

print(sumtree(L)) # Prints 36


# Pathological cases
print(sumtree([1, [2, [3, [4, [5]]]]])) # Prints 15 (right-heavy)

print(sumtree([[[[[1], 2], 3], 4], 5])) # Prints 15 (left-heavy)


def sumtree(L): # Breadth-first, explicit queue
    tot = 0
    items = list(L) # Start with copy of top level
    while items:
        front = items.pop(0) # Fetch/delete front item
        if not isinstance(front, list):
            tot += front # Add numbers directly
        else:
            items.extend(front) # <== Append all in nested list
    return tot


def sumtree(L): # Depth-first, explicit stack
    tot = 0
    items = list(L) # Start wtih copy of top level
    while items:
        front = items.pop(0) # Fetch/delete front item
        if not isinstance(front, list):
            tot += front # Add numbers directly
        else:
            items[:0] = front # <== Prepend all in nested list
    return tot


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





