def my_decorator(func):
    def wrapper():
        print("After")
        func()
        print("Before")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()