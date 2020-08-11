# The Dynamic Typing Interlude



L1 = [2,3,4] # A mutable object
L2 = L1 # Make a reference to the same object
L1[0] = 24 # An in-place change
print(L1) # L1 is differemt
print(L2) # But so is L2!


L1 = [2,3,4]
L2 = L1[:] # Make a copy of L1 (or list(L1), copy.copy(L1), etc.)
L1[0] = 24
print(L1)
print(L2) # L2 is not changed


L = [1,2,3]
M = L # M and L reference the same object
print(L == M) # Same values
print(L is M) # Same objects


L = [1,2,3]
M = [1,2,3] # M and L reference different objects
print(L == M) # Same values
print(L is M) # Different objects


X = 42
Y = 42 # Should be two different objects
print(X == Y)
print(X is Y) # Same object anyhow: caching at work!


import sys
print(sys.getrefcount(1)) # 163 pointers to this shared piece of memory


