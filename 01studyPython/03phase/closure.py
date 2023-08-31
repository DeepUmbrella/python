
# if want to change the value of a variable in closure,must use nonlocal syntax

def outer():
    logo = '***'

    def inner(text):
        nonlocal logo

        logo += text
        return logo
    return inner


outer_logo = outer()
print(outer_logo('Python'))
