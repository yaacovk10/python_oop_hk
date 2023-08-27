class Animal:
    def __init__(self, kind, age, weight, height):
        self.kind = kind
        self.age = age
        self.weight = weight
        self.height = height

    def cry(self):
        return "The animal makes a sound."

    def eat(self, food):
        return f"The animal is eating {food}."

    def sleep(self):
        return "The animal is sleeping."

# Test the Animal class
if __name__ == "__main__":
    lion = Animal("Lion", 5, 200, 1.2)
    print(f"Kind: {lion.kind}, Age: {lion.age} years, Weight: {lion.weight} kg, Height: {lion.height} meters")
    print(lion.cry())
    print(lion.eat("meat"))
    print(lion.sleep())

    elephant = Animal("Elephant", 15, 5000, 3.5)
    print(f"Kind: {elephant.kind}, Age: {elephant.age} years, Weight: {elephant.weight} kg, Height: {elephant.height} meters")
    print(elephant.cry())
    print(elephant.eat("vegetation"))
    print(elephant.sleep())
