# if Tests and Syntax Rules



"""
if test1: # if test
    statements1 # Associated block
elif test2: # Optional elifs
    statements2
else: # Optional else
    statements3
"""


if 1:
    print('true')


if not 1:
    print('true')
else:
    print('false')


x = 'killer rabbit'

if x == 'roger':
    print('shave and a haircut')
elif x == 'bugs':
    print("what's up doc?")
else:
    print('Run away! Run away!')


choice = 'ham'

print({'spam': 1.25, 'ham': 1.99, 'eggs': 0.99, 'bacon': 1.10}[choice]) # A dictionary-based 'switch.' Use has_key or get for default


if choice == 'spam': # The equivalent if statement
    print(1.25)
elif choice == 'ham':
    print(1.99)
elif choice == 'eggs':
    print(0.99)
elif choice == 'bacon':
    print(1.10)
else:
    print('Bad choice')


branch = {'spam': 1.25, 'ham': 1.99, 'eggs': 0.99}

print(branch.get('spam', 'Bad choice'))

print(branch.get('bacon', 'Bad choice'))


choice = 'bacon'

if choice in branch:
    print(branch[choice])
else:
    print('Bad choice')


try:
    print(branch[choice])
except KeyError:
    print('Bad choice')


