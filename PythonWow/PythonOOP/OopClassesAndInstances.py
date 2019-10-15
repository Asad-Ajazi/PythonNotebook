# Object oriented programming in python

# attributes/methods

# employee class
# regular methods automatically take the instance (self)

class Employee:

    # adding class variables
    raise_amount = 1.05
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@gmail.com'

        # to count, if using self, would only count to 1.
        Employee.num_of_emps += 1

    def fullname(self):
        """don't forget to add self!"""
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # class variable raise_amount
        # use self to differentiate changes, or class name to change for all.

    # adding a decorator to take a class instead of instance as first argument
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


# create and set variables for an object using __init__  (the constructor)
emp_1 = Employee('John', 'Banks', 40000)
print('Number of employees: {}'.format(Employee.num_of_emps))
emp_2 = Employee('Jill', 'Hall', 35000)

# shows the memory location
print(emp_1)
print(emp_2)
print()

# printing email
print(emp_1.email)
print(emp_2.email)
print()

# printing full name using method from class.
print(emp_1.fullname())
print(emp_2.fullname())
print()

# can also run method directly from that class and pass in the instance
print('Directly from class passing in argument full name: ' + Employee.fullname(emp_1))

# using the apply raise method
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(emp_1.__dict__)
print(Employee.__dict__)
print()

print(Employee.raise_amount)
Employee.raise_amount = 1.08
print('raise from class')
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print('raise for instance emp_1')
emp_1.raise_amount = 1.2  # changed raise for emp1
# creates a raise_amount attribute to emp_1 after assignment
print(emp_1.__dict__)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()

# number of employees, add 1 each time an instance is created.
print('Number of employees: {}'.format(Employee.num_of_emps))
print()

# a class method, but does not effect the previous instance amount set
Employee.set_raise_amount(1.01)
# is the same as -- Employee.raise_amount = 1.01
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print()


# https://www.youtube.com/watch?v=rq8cL2XMM5M&t=6s