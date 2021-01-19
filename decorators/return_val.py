def bark_3_times(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


@bark_3_times
def doggo(name):
    print("output will show below")
    return f"{name} is barking"


barks_ = doggo("Laika")

print(barks_)
