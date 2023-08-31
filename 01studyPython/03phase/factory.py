class PersonFactory:
    def __init__(self, person_type):
        self.person_type = person_type

    def create(self, name):
        return self.person_type(name)
