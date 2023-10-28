# decorators.py

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


@my_decorator
def jump_five_meters():
    print("Jumped_five_meter!")


if __name__ == "__main__":
    say_hello()
