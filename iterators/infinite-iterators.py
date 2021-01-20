n = 1

iterable_obj = iter(int, 1)

print(next(iterable_obj))  # 0
print(next(iterable_obj))  # 0
print(next(iterable_obj))  # 0
print(next(iterable_obj))  # 0

# int() method when parameter not passed always return 0.
# so it never becomes equal to 1 so it's became infinite.
