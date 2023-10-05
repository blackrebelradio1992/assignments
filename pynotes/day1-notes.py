# print('hello world')


# a_small_number = 4


# # how to check a var
# print(type(a_small_number))


# #normal math
# print(4 / 4.5)

# #modulo
# print(3.5 % 3)#get the remainder

# #
# print(15 % 3) #returns 0 


# # there is no ===
# # string interpolation is - f string
# name = "gdog"
# print(f"yo whats up {name}")

# # If you need to add elements, 
# # you would need to create a new tuple 
# # that includes the original elements as well as the new one.
# old_tuple = (1, 2, 3)
# new_item = 4

# new_tuple = old_tuple + (new_item,)

# #this is how functions work in Python
# def say_dude():
#     return "dude"

# print(say_dude())

# # this is how you assign a function in a dictionary
# jeff = {
#     'name': 'jeff',
#     'age': 44,
#     'job': 'influencer',
#     'action': say_dude
# }
# print(jeff['age'])

# def gimme_five():
#     return 5
# print(gimme_five() + 10)


# # if a function is defined with one parameter, it must be called with one argument
# def add_one(n):
#     return n + 1
# print(add_one(10))

# # order matters for positional arguments
# def describe_berries(n, color):
#     print(f'I have {n} {color}berries.')
# describe_berries(3, 'blue')
# describe_berries('black', 4)

# # keyword arguments can be used in any order
# def describe_berries(n=1, color="blue"):
#     print(f'I have {n} {color}berries.')
# describe_berries(color="rasp", n=3)

# # use * to define a function with an unspecified number of parameters
# def print_them_all(*args):
#     print(args)
# print_them_all('alice', 'bob', 'carol')

# # use ** to define a function with an unspecified number of keyword arguments
# def who_am_i(**kwargs):
#     for kwarg in kwargs: # we'll talk more about loops in a minute
#         print(f'My {kwarg} is {kwargs[kwarg]}.')
# who_am_i(name='dan', age=20, job='skydiving instructor')

# def can_drink_beer(age, country):
#     if age >= 21 or age >= 18 and country == 'Canada':
#         return True
#     elif country == 'Antarctica':
#         return True
#     else:
#         return False

# print(can_drink_beer(20, 'USA'))
# print(can_drink_beer(21, 'USA'))
# print(can_drink_beer(18, 'Canada'))


# ## looping over list elements
# my_list = ["a", "b", "c"]
# for x in my_list:
#     print(x)

# ## loop over a range
# for x in range(10):
#     print(x)


# for i, x in enumerate(my_list):
#     print(i, x)

# ## looping over dictionary entries
# my_dict = {
#     "donuts": "yummy!",
#     "green beans": "icky!",
# }
# for k in my_dict:
#     print(my_dict[k])

# for v in my_dict.values():
#     print(v) # same output as the previous loop




# one_to_ten = range(10)
# print(one_to_ten)

# for x in one_to_ten:
#     print(x)


first_name = 'jonathan'
first_name.capitalize() # this is a string method that converts the first character to upper case
first_name # we see that despite running the method above, my original data does not change
print(first_name.capitalize())


cool_name = 'cold'
cool_name.replace('d', 'old')
print(cool_name)

last_name = 'young'
print(last_name.replace('g', '123'))
last_name # same case here - this is a non destructive method print
print(last_name)