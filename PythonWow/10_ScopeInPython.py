"""
LEGB
Local, Enclosing, Global, Built in.
"""
# basic scoping is similar to all other languages.
# global scope.
x = 'global x'


def global_test():
    y = 'local y'
    print(y)
    # can print global variables from within functions
    print(x + ' inside the test function')


global_test()


# print(y), will fail because its scope is inside the function


def global_to_local_test():
    """The local variable takes priority over the global in the function scope"""
    x = 'local x'
    print(x)
    # global variable is not overwritten
    print(x + ' inside the test function')


global_to_local_test()
print(x)
print()


# a = 'global a'
# declaring the global can be done within a function, is not required outside
# but is preferred


def change_global_variable():
    global a  # can be declared here, but only if using 'global'
    # avoid using global much
    a = 'changing the global a to this.'
    print(a, ' /this is inside the function')


change_global_variable()
print(a)
print()


def using_func(z):
    """passed in argument is local to the function scope"""
    print(z)


using_func('local z')
print()

# built in scope
import builtins
# shows all the builtins
print(dir(builtins))

# min returns the smallest value of an iterable
m = min([2, 9, 4, 7, 3, 11])
print(m)


def min():
    print('overwritten min function, be careful not to do this')


min()
# below code fails because min has been overwritten and accepts no arguments.
# m = min([2, 9, 4, 7, 3, 11])
# print(m)
print()


# enclosing scope. for nested functions
# inner scopes will take priority for themselves, inner can use outer, but not nested
def outer():
    b = 'outer b'

    def inner():
        b = 'inner b'
        print(b)

    inner()
    print(b)


outer()
print()

c = 'global c'


# global for inner variables. (nonlocal)
def outer():
    c = 'outer c'

    def inner():
        nonlocal c
        c = 'inner c'
        print(c)

    # changes outer c from within inner c
    inner()
    print(c)


outer()
print(c)