def bark_3_times(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@bark_3_times
def doggo(name):
    print(name, " is barking")


doggo("Laika")