def my_decorator(func):

    def wrapper():
        print("before whee")
        func()
        print("after whee")

    return wrapper


@my_decorator
def say_whee():
    print("whee")


say_whee()
