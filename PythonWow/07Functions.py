# Working with functions in Python 3
print("Functions in Python 3")
print()


# creating a functions, def keyword. 2 lines before/after a function definition
def hello_func():
    print('hello function.')


# use the pass keyword to keep a function empty without causing errors, fill later.
def fill_later_blank_function():
    pass


hello_func()  # calling the function
hello_func()  # and again
hello_func()  # and again
# DRY PRINCIPLE, DON'T REPEAT YOURSELF
print(hello_func)  # print without () to show memory location
print()


# return a value from a function
def return_a_string():
    return 'This string was returned from a function'


print(return_a_string())  # returned string is printed
print(return_a_string().upper())  # chaining other methods on the return type.
print()


# passing in an argument and formatting result
def return_a_greeting(greeting):
    return '{} Function.'.format(greeting)


# passing in multiple arguments, default value (name = you) if not supplied
# keyword argument (defaults/optional) must come after the required arguments
def return_a_greeting_name(greeting, name='you'):
    return '{}, {} Function.'.format(greeting, name)


print(return_a_greeting_name('Hi'))  # uses default value
print(return_a_greeting_name('Hi', 'John'))


print(return_a_greeting('Welcome (passed in argument)'))
print()


# passing arguments to a function, add two numbers
def add_two_numbers(num1, num2):
    return int(num1) + int(num2)


print('Add numbers method:', add_two_numbers('3', '2'))
print(add_two_numbers(5, 9))
print()

print('*args and **kwargs')


# *args and **kwargs (arguments and keyword arguments)
# allows for accepting arbitrary number of position/kw arguments
def student_info(*args, **kwargs):
    print(args)  # tuple
    print(kwargs)  # dictionary


# args turn to a tuple, kwargs to a dictionary
student_info('Maths', 'Science', name='Peter', age=22)
print()

# arguments using * or **
print('*args and **kwargs with list/dict passed in')
courses = ['English', 'Art']
student = {'name': 'John', 'age': 25}

# passing list/dictionary in. unpack using */** and pass in
print('--Without */**')
student_info(courses, student)
print('\n--With */** unpacking.')
student_info(*courses, **student)