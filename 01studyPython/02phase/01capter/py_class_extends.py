
# use python extends class 

from py_constructor import Animal 

class Friend:
    friend_name=None

    def __init__ (self):
        self.friend_name = "red dog"


class Dog(Animal,Friend):
    master=None
    sonund="wang wang wang !"
       
    def __init__(self,master):
        self.master = master


keke_dog = Dog("jiajia")


print(f"kekedog  master {keke_dog.master} , age is {keke_dog.age}, he's friends is {keke_dog.friend_name}")