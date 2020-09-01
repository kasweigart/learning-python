# Tuples (Immutable Sequences)

T = (1,2,3,4) # 4 item tuple
print(len(T))

print(T + (5,6)) # Concatenation

print(T[0]) # Indexing, slicing, and more

print(T.index(4)) # Tuple methods: 4 appears at offset 3
print(T.count(4)) # 4 appears once

T = (2,) + T[1:] # Make a new tuple for a new value
print(T)

T = 'spam', 3.0, [11,22,33]
print(T[1])
print(T[2][1])
