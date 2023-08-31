from threading import Thread


def wrapper(cls):
    print("___wrapper")
    cls.thread_count = 3
    return cls


@wrapper
class ThreadPool:
    def __new__(cls, *arg, **keywords):
        print(cls.thread_count, "___new")
        return super().__new__(cls)


def start_new_thread(daemon=False):
    def wrapper(func):
        print("___wrapper")

        def inner(*args, **kwargs):
            thread = Thread(target=func, args=args)
            thread.daemon = daemon
            thread.start()
        return inner
    return wrapper
