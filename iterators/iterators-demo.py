my_list = [2, 4, 7]

iterable_list = iter(my_list)  # passing list through iter() which returns an iterable object

print(next(iterable_list))  # 2
print(next(iterable_list))  # 4
print(next(iterable_list))  # 7
print(next(iterable_list))  # StopIteration
