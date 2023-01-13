
# Basic printing/ single vs double quote dependant on string. triple.
print("Hello World!")

single_line_message = "Variable message."

two_line_message = """Triple quotes for
multi line split, can "Mix" quotes, it's cool.?"""

multi_line_same_line = "This " \
    "stays " \
    "on one line."

print(single_line_message)
print(two_line_message)
print(multi_line_same_line)

# length of string
message = "Hello world!"
print(len(message))
print(message[11])
# ===print range of characters, leave off start or end index to go to s/e
print(message[0:5])
print(message[6:])

# casing
print(message.lower())
print(message.upper(),"asdsad")

# counting the number of occurances of a char or substring in a string.
print("this is o")
print(message.count("o"))
print(message.count("l"))
print(message.count("Hello"))

# find starting index of substring
print(message.find('world'))
print(message.find("returns -1 if doesn't exist"))

# replace, replaces old string with new. Can replace individual chars.
new_message = message.replace("world", "earth")
print(new_message)

# concatenate strings
greeting = "Hello"
name = "John"
concat_message = greeting + ', ' + name + '. Welcome!'
# -- string format placeholders
concat_message = '{0}, {1}. Welcome'.format(greeting, name)
# -- f strings alternate method in newer python to not .format.
concat_message = f'{greeting.upper()}, {name}. New method f strings Hi.'
print(concat_message)

# help for methods and descriptions on what they do.
print(dir(name))
print(help(str))
print(help(str.lower))