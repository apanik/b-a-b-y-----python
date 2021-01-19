def bark_3_times(func):
    def wrapper():
        func()
        func()
        func()

    return wrapper


@bark_3_times
def doggo():
    print("bark")
