def my_decorators(func):
    def wrapper():
        print("will be print at the first ")
        func()
        print("will be print at the last")

    return wrapper


@my_decorators
def my_function():
    print("I will be print at the middle")

my_function()