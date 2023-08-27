

def test_fun(a, b, callback=lambda x, y: x+y):

    return callback(a, b)


def add(x, y):
    print(x+y)
    return x + y


test_fun(1, 2, add)
