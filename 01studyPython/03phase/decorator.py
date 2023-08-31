from time import sleep


def sleep_decorator(say: str):
    def decorator(func):
        print(say)
        func(say)
        print(say)
    return decorator


@sleep_decorator("Hello")
def say_hello(say: str):
    print(f"base {say}")
