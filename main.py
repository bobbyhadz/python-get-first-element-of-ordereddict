# Get the First element of an OrderedDict in Python

from collections import OrderedDict

my_dict = OrderedDict(
    [('name', 'bobbyhadz'),
     ('age', 30),
     ('topic', 'Python')]
)

first_key = next(iter(my_dict))
print(first_key)  # 👉️ name

first_value = my_dict[first_key]
print(first_value)  # 👉️ bobbyhadz

first_pair = next(iter(my_dict.items()))
print(first_pair)  # 👉️ ('name', 'bobbyhadz')

print(list(my_dict.items())[0])  # 👉️ ('name', 'bobbyhadz')
print(list(my_dict.items())[1])  # 👉️ ('age', 30)