"""
Generators can be implemented in a clear
and concise way as compared to their iterator class counterpart.

"""


# A simple generator function
def my_gen():
    point = "starting point..."
    # Generator function contains yield statements
    yield point

    point = "middle point..."
    # Generator function contains yield statements
    yield point

    point = "at the ending..."
    # Generator function contains yield statements
    yield point


data = my_gen()

""" printing through using 'next' method """

print(next(data))
print(next(data))
print(next(data))


for data in my_gen():
    print("[via loop] ",data)

# generator example via expression

my_gen1 = (x for x in range(1, 10))
my_gen1_sum = sum(x for x in range(1, 10))
my_gen1_max = max(x for x in range(1, 10))

print(next(my_gen1))
print(my_gen1_sum)
print(my_gen1_max)
