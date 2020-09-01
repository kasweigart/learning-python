# Nesting
M = [[1,2,3],
     [4,5,6],
     [7,8,9]]

print(M)
print(M[1]) # Get row 2
print(M[1][2]) # Get item 3 within row 2


col2 = [row[1] for row in M]

print(col2) # Get items in col 2

print([row[1] + 1 for row in M]) # Add 1 to each item in col 2


diag = [M[i][i] for i in [0,1,2]] # Collect a diagonal from matrix
print(diag)


doubles = [c * 2 for c in 'spam'] # Repeat characters in a string
print(doubles)


print(list(range(4))) # [0,1,2,3]

print(list(range(-6,7,2))) # -6 to 6 by 2

print([[x ** 2, x ** 3] for x in range(4)]) # Multiple values

print([[x, x/2, x*2] for x in range(4)]) # "If" filters

G = (sum(row) for row in M) # Create generator of row sums
print(next(G)) # Run the iteration protocol next()
print(next(G))
print(next(G))

print(list(map(sum, M))) # Map sum over items in M

print({sum(row) for row in M}) # Create a set of row sums

print({i : sum(M[i]) for i in range(3)}) # Creates key/value table of row sums

print([ord(x) for x in 'spaam']) # List of character ordinals

print({ord(x) for x in 'spaam'}) # Sets remove duplicates

print({x: ord(x) for x in 'spaam'}) # Dictionary keys are unique

print((ord(x) for x in 'spaam')) # Generator of values

