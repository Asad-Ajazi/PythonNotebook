# Working with conditional statements. if/else/elif etc.
print("Conditional Statements! \n")

# basic if statement, only runs when condition is true.
# Python uses indentations instead of brackets, 4 spaces.
if True:
    print('Conditional statement was true.')

# if False will never run.
if False:
    print("This is false so it won't be run")
print()  # this is outside the statement so will run.

# Comparisons: (return boolean values)
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=

# Object Identity:  is
# ^^(This checks if values have the same id/ are the same object in memory)

# == evaluates to true or false.
# basic if/elif/else statement.
city = 'Berlin'
if city == 'London':
    print('Welcome to London.')
elif city == 'Berlin':
    print("Welcome to Berlin")
elif city == 'Tokyo':
    print('Welcome to Tokyo')
else:
    print("You're not in the right city.")

# Python does not have a switch statement, use if's instead.
print()

# Boolean operations:
# and
# or
# not

# and: checking if user in an Admin 'and' is logged_in
print("checking if user in an Admin 'and' is logged_in")

user = 'Admin'
logged_in = False

print('Checking all conditions with "and"')
if user == 'Admin' and logged_in:
    print('Admin dashboard.')
else:
    print('Access Denied')

# or: returns true if at least one of the conditions are true.
print('\nChecking if one or more conditions are true with "or')
if user == 'Admin' or logged_in:
    print('Admin dashboard.')
else:
    print('Access Denied')

# not: changes true to false and false to true. returns the reverse result
print('\nUsing "not" to reverse bool. (if not false == true)')
# if logged in is false, then returns true and executes first statement.
if not logged_in:
    print('Please login')
else:
    print('Home Page')

print()  # spacing.

# is keyword to check for same object. not the same as ==
print('using the "is" keyword to check for the same object')

a = [1, 2, 3]
b = [1, 2, 3]

print('a:', a)
print('b:', b)

# == returns true because values are the same
print('a == b:', a == b)

# is, returns false because they are different objects in memory
print('\na id =', id(a))
print('b id =', id(b))
print('a is b:', a is b)

# changing b = a, so they reference the same object in memory.
print('\nChanging b = a.')
b = a
print('a id =', id(a))
print('b id =', id(b))
print('a is b:', a is b)
print('a == b:', a == b)
print()


# conditional values that always evaluate to false.
# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.
# ^use these to evaluate if strings, lists etc are empty

condition = None  # any false value listed above. Will result in false

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

