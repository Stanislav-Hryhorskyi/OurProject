"""
A program that prints the same characters
that are in both strings
"""

# Variant 1 (using methods of sets)
string_1 = input('Enter the first string: ')
string_2 = input('Enter the second string: ')
new_list = sorted(list(set(string_1).intersection(set(string_2))))
print(f'List of characters (in ascending order) that are in both strings: {new_list}')

# Variant 2 (using methods of lists)
string_1 = input('Enter the first string: ')
string_2 = input('Enter the second string: ')
new_list = list()
for char_1 in string_1:
    for char_2 in string_2:
        if char_1 == char_2 and not new_list.count(char_1):
            new_list.append(char_1)
print(f'List of characters (in ascending order) that are in both strings: {sorted(new_list)}')


