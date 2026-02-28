class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
def Introduce(self):
        print(f"My name is {self.name}, im {self.age} yo.")
        print(f"My color is {self.color}")
        for i in self.color:
            print(i)
my_cat = Cat("Снежок", 2, "белый")
my_cat.Introduce()
