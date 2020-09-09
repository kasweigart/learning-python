# while and for Loops



# while True:
#     print('Type Ctrl-C to stop me!')


x = 'spam'

while x: # While x is not empty
    print(x, end=' ') # In 2.X use print x,
    x = x[1:] # Strip first character off x


a=0; b=10

while a < b: # One wat to code counter loops
    print(a, end=' ')
    a += 1 # Or, a = a + 1


x = 10

while x:
    x = x-1 # Or, x -= 1
    if x % 2 != 0: continue # Odd? -- skip print
    print(x, end=' ')


x = 10

while x:
    x = x-1
    if x % 2 == 0: # Even? -- print
        print(x, end=' ')


# while True:
#     name = input('Enter name: ')
#     if name == 'stop': break
#     age = input('Enter age: ')
#     print('Hello', name, '=>', int(age) ** 2)


y = 10

x = y // 2 # For some y > 1

while x > 1:
    if y % x == 0: # Remainder
        print(y, 'has factor', x)
        break
    x -= 1 # Skip else
else:
    print(y, 'is prime') # Normal exit


