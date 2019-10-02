# Lists, Tuples and Sets in Python

# Create a LIST
courses = ['English', 'Maths', 'Science', 'History']
print(courses)

# len() function to see how many items are in the list.
print('Number of items in list:', len(courses))

# accessing values via index.
print('Value at index 1 =', courses[1])

# using negative (-1) to start at the end.
print('Value at index -1 (last item) =', courses[-1])

# getting a range of values from a list [0:2] (start index, end index (but not including))
print('\nRange of values:')
print('[0:2]', courses[0:2])
print('Start to index 3 [:3] =  ', courses[:3])
print('Start index to end [2:] =', courses[2:])
print('Last 2 items [:-2] =     ', courses[:-2])
print()

# List Methods.
# Append to the end of the list.
courses.append('Art')
print('Art added to end using append:', courses)

# insert value into specific index.
courses.insert(0, 'Economics')
print('Value added to index 0:', courses)
print()

# using insert on a second list adds list within list.
courses_2 = ['PE', 'Geography']
courses.insert(0, courses_2)
print('Using insert with a list:', courses)
del courses[0]  # To delete the added nested list.

# Extend to add another list to the end of a list.
courses.extend(courses_2)
print('Extend to add multiple items to end: ', courses)
print()

# removing values from list
courses.remove('Science')
print('Removing "Science" from the list:')
print(courses)

# pop to remove last value and return it
last_value = courses.pop()
print('pop() to remove last item:', courses)
print('Value removed =', last_value)
print()

# del to remove item from specific index.
del courses[0]
print('Value at index 0 removed using del:', courses)
print()

# sorting list
# reverse current list
courses.reverse()
print('Reversed List: ', courses)

# Sort in alphabetical order.
courses.sort()
print('Sorted alphabetically', courses, '\n')

nums = [5, 2, 1, 3, 4]
print('Unsorted list of numbers:         ', nums)
nums.sort()
print('Numbers sorted in ascending order:', nums)
nums.sort(reverse=True)
print('sort(reverse=True) to sort descending:', nums, '\n')

# Sorted function returns sorted version of list, original not altered.
sorted_nums = sorted(nums)
print('Sorted function on nums list:', sorted_nums, '\n')

# Min, Max, Sum
print('Number list:', nums)
print('min():', min(nums))
print('max():', max(nums))
print('sum():', sum(nums))
print()

# Finding the index of an item
print('courses list:', courses)
print('The index() of History is:', courses.index('History'))

# the 'in' operator
print('Is Art in courses list?:', 'Art' in courses)
print('Is Science in courses list?:', 'Science' in courses)
print()

# basic for loop.
print('Simple for loop:')
for course in courses:
    print(course)
print()

# using enumerate function to get index and value.
print('Using enumerate to show the index:')
for index, course in enumerate(courses):
    print('Index:', index, ', Value =', course)
print()

# using enumerate to change start value, 1 instead of 0.
print('Change starting index to 1 instead of 0:')
for index, course in enumerate(courses, start=1):
    print('Index:', index, ', Value =', course)

# Turn list into string separated by a certain value:
print()
print('Courses list:', courses)

course_str = ' - '.join(courses)
print('Joining list to string: ', course_str)
print()

# converting a string separated by certain value to a list
new_courses_list = course_str.split(' - ')
print('String converted back to a list: ')
print(new_courses_list)