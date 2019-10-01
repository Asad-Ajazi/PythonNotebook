print('Working with numerical data in python')

type_test = 5

# use type() to see the class. 3 = 'int', 3.14 = 'float'
print("The type of (the class) 5 = ", type(type_test))

# Arithmetic operators:
# Addition:       5 + 4
# Subtraction:    5 - 4
# Multiplication: 5 * 4
# Division:       5 / 4
print("Normal Division 5/4 =", 5/4)

# Floor Division: 5 // 4
# Flood division divides then goes to the closest lower whole number.
print("Floor Division 5//4 = ", 5//4)
print()

# Exponent:       5 ** 4
print("Exponent:")
print("3 ** 3 = (3x3x3)", 3**3)
print()

# Modulus:        5 % 4
# Mod give the remainder after a division
print("Modulus")
print("6 % 4 =", 6%4)
print("15 % 3 =", 15 % 3)
print()

# Odd/Even check:
print("Odd or Even Check:")
print("2 % 2 (even)=", 2 % 2)
print("3 % 2 (odd)=", 3 % 2)

# Order of Operations:
print("Order of Operations:")
print("3 * 2 + 1 =", 3*2*1)
print("3 * (2 + 1) =", 3 * (2 + 1))
print()

# Incrementing numbers
print("Incrementing Numbers:")
num = 1
print("Num =", num)
# num = num + 1
num += 1
print("+= 1 increments by 1. Num is now:", num)
num *= 10
print("*= 10 multiplies by 10, Num is now:", num)
print()

# Built in functions for numbers:
print("Built in functions:")

# abs():
print("abs() removes sign from negative numbers.")
print("abs(-5) =", abs(-5))
print()

# round(number, digits to round to) to the nearest integer value:
print("Rounding numbers to desired length:")
print("round(3.6)", round(3.6))  # 3.7
print("round(3.77, 1) =", round(3.77, 1))  # 3.78
print()



