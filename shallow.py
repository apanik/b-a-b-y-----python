import copy


list_ = [[1,2,3],["a","b","c"],[1.1,2.2,3.3]]
new_list_ = copy.copy(list_)
list_[0][1] = "new string"


print("list_ ",list_)
print("new_list_ ",new_list_)


# UNDERSTANDING
# In Shallow copy when we change in old list it's changes to the new list also 

