# Using Loops and iteration in Python (for/while)

nums = [1, 2, 3, 4, 5]

# simple for loop
print('Basic for loop over list of ints')
for num in nums:
    print(num)

print()
# break statement breaks out of the for loop.
print('Using a "break statement" to break out of the loop when a condition is met.')
for num in nums:
    if num == 3:
        print(f'Found the secret number')
        break
    print(num)

print()

# continue statement to skip current iteration of a loop
print('Using a "continue" statement to skip to the next iteration if a condition is met.')
for num in nums:
    if num == 3:
        print(f'Found the secret number')
        continue
    print(num)

print()

# Nested loops: outer, then all inner, then next outer and all inner, repeat.
print('Nested loops: prints first value in first loop, then all in second, then repeats')
for num in nums:
    for letter in 'ABC':
        print(f'{num}-{letter}')

print()

# range() function to iterate certain number of times. doesn't include last value
# 0 based index
print('for using range() function to iterate x times.')
for i in range(10):
    print(i)

print('for using range(starting index, times to iterate)')
# range(start index, number of times to loop), 1-11 to print 1-10
for i in range(1, 10):
    print(i)

print()

# While loops to iterate while condition is true.
# can also use break/continue to break out/skip loop early.
print('Using a while loop to iterate while condition remains true.')

x = 0
while x < 5:
    if x == 3:
        print('break statement hit.')
        break
    print(x)
    x += 1

print()

# can use "while True" to have infinite loop and wait for input to react.
# press "ctrl + c" to end an infinite loop in most OS's.

# while True:
    # print(x)
    # x += 1
