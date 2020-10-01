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
















