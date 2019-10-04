# Working with Dictionaries in Python
print('Dictionaries in Python')
print()

# dictionary = {'key': 'Value', 'Key2': 'Value2'}
# Keys can be any immutable data type (strings, ints)
student = {'name': 'John', 'age': 22, 'courses': ['Maths', 'Science'], 1: 2}

print('Student dict:', student)
print('Printing name string:', student['name'])
print('Printing list of courses:', student['courses'])
print()

# using .get method to return 'none' if key doesn't exist.
print('Using the .get method to prevent key not found error.')
print('Print Name:', student.get('name'))
print('Print height:', student.get('height'))
print('Print height with custom:', student.get('height', 'Custom default value, key not found.'))
print()

# adding a new entry to the dictionary
print('Adding new entries to the dictionary:')
student['phone'] = '07123456789'
print('Phone number:', student['phone'])
# updating an existing entry
student['phone'] = '09547862134'
print('Updated phone number:', student['phone'])
print()

# using the update method to update multiple values at a time.
print('Using the update() method to update multiple values')
print('Before update:', student)
# Can change values and also add new ones.
student.update({'name': 'Dan', 'age': 34, 'is_alive': True})
print('After update:', student)
print()

# Deleting specific keys/values using del.
print('Using del to delete age from records:')
del student['age']
print(student)
print()

# Using pop to remove and return a value:
print('Using pop() to remove and return a value:')
print(student)
phone = student.pop('phone')
print(student)
print('Phone number removed was:', phone)
print()

# looping through keys/ values of a dictionary. keys/values/items
print('Number of keys in Dict:', len(student))
print('Print Keys:', student.keys())
print('Print values:', student.values())
print('Print Both:', student.items())

print()
# looping through the keys
print('printing only keys:')
for key in student:
    print(key)
print()

# items() method to loop through keys and values
print('Printing keys and values using items() method:')
for key, value in student.items():
    print(key, ':', value)
