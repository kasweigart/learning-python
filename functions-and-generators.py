# Part IV: Functions and Generators




#Function Basics



# if test:
#     def func(): # Define func this way
#         ...
# else:
#     def func(): # Or else this way
#         ...
# ...
# func() # Call the version selected and built


# def func(): ... # Create function object

# func() # Call object

# func.attr = value # Attach attributes


def times(x,y): # Create and assign function
    return x * y


print(times(2,4)) # Arguments in parentheses


x = times(3.14, 4) # Save the result object

print(x)


print(times('Ni',4)) # Functions are 'typeless'


def intersect(seq1,seq2):
    res=[] # Start empty
    for x in seq1: # Scan seq1
        if x in seq2: # Common item?
            res.append(x) # Add to end
    return res


s1 = 'SPAM'

s2 = 'SCAM'

print(intersect(s1,s2)) # Strings


print([x for x in s1 if x in s2])


x = intersect([1,2,3], (1,4)) # Mixed types

print(x)






