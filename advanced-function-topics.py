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








