class SingleModel:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name, ways) -> None:
        self.name = name
        self.ways = ways

    def __str__(self) -> str:
        return self.name


s1 = SingleModel("model1", "ways1",)

s2 = SingleModel("model2", "ways2")

print(s1)
print(s2)
