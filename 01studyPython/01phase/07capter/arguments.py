# * return multiple value


def return_multiple_value():
    return 1, 2


x, y = return_multiple_value()

print(x, y)


def key_words_args_function(name: str, age: int, **kwargs):
    print(name, age, kwargs)


key_words_args_function(age=18, name="Tom", gender="male", height=180)


def default_args_function(name: str, age: int = 18, *args):
    print(name, age, args)


default_args_function("S", "19", "sdafasfa", "f666", "7777")
