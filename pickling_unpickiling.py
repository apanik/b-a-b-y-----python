import pickle

class exampleClass():
      string_ = "Example String"
      list_ = [1,2,3]
      dict_ = {"name":"anik","age":25}

# creating object of ecampleClass
my_object = exampleClass()

# pickling myobject to binary string presentation
pickled_objects = pickle.dumps(my_object)
# after pickling my_object should be like this /n : #
# b'\x80\x04\x95 \x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x0cexampleClass\x94\x93\x94)\x81\x94.'

# now unpickling that object for getting back to original state
unpickled_objects = pickle.loads(pickled_objects)


processed_string = unpickled_objects.string_
processed_list = unpickled_objects.list_
processed_dict = unpickled_objects.dict_


print(f"String is {processed_string} , list is {processed_list} , dictionary is {processed_dict}")
# output String is Example String , list is [1, 2, 3] , dictionary is {'name': 'anik', 'age': 25}
