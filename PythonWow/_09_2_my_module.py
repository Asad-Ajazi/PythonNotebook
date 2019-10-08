# test module to be used to import into another file
print('imported my_module...')

test = 'Test String'


def find_index(to_search, target):
    """Finds the index of a value in a sequence"""
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
