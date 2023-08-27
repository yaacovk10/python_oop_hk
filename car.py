class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    def accelerate(self, speed_increase):
        self.speed += speed_increase

    def brake(self, speed_decrease):
        if self.speed >= speed_decrease:
            self.speed -= speed_decrease
        else:
            self.speed = 0

    def honk(self):
        return "Honk! Honk!"

    def get_speed(self):
        return self.speed

    def __str__(self):
        return f"{self.year} {self.color} {self.make} {self.model}"

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", 2023, "Blue")

# Using the methods and accessing attributes
print(my_car)  # Output: 2023 Blue Toyota Camry

my_car.accelerate(30)
print(my_car.get_speed())  # Output: 30

my_car.brake(10)
print(my_car.get_speed())  # Output: 20

print(my_car.honk())  # Output: Honk! Honk!
