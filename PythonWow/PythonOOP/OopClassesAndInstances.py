# Object oriented programming in python

# attributes/methods

# employee class


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@gmail.com'

    def fullname(self):
        """don't forget to add self!"""
        return f'{self.first} {self.last}'


# create and set variables for an object using __init__  (the constructor)
emp_1 = Employee('John', 'Banks', 40000)
emp_2 = Employee('Jill', 'Hall', 35000)

print(emp_1)
print(emp_2)
print()
# the old bad way
# emp_1.first = 'John'
# emp_1.last = 'Banks'
# emp_1.email = 'JohnBanks@gmail.com'
# emp_1.pay = 40000

# emp_2.first = 'Jill'
# emp_2.last = 'Hall'
# emp_2.email = 'JillHall@gmail.com'
# emp_2.pay = 35000

print(emp_1.email)
print(emp_2.email)
print()

# printing full name using method from class.
print(emp_1.fullname())
print(emp_2.fullname())

# can also run method directly from that class and pass in the instance
print('Directly from class passing in argument full name: ' + Employee.fullname(emp_1))