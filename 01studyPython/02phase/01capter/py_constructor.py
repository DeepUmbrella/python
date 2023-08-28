
class Animal:
    name=None
    age=None
    kind=None
    __nick_name=None

    def __init__(self,name="",age=18,kind = "all"):
        self.age = age
        self.name = name
        self.kind = kind
        self.__nick_name = name
 
    def get_name(self):
        return self.name


    def get_nick_name(self):
        return self.__nick_name
      
    def __str__(self):
        return self.name 

    def __lt__(self,other):
        return self.age < other.age

    def __le__(self,other):
        return self.age <= other.age
    def __eq__(self,other):
        return self.kind == other.kind

dog = Animal("dog",18)
cat = Animal("cat",19)
cat_nick_name = cat.get_nick_name()
name = dog.get_name()

print(dog) 
print(dog > cat) #False
print(dog < cat) #True
print(dog >= cat)#False
print(dog <= cat)#True
print(dog == cat)

print(f"dog's name is {name} cat nick_name is {cat_nick_name}")