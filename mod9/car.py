class Car:
    def __init__(self, register_num, top_speed):
        self.register_num = register_num
        self.top_speed = top_speed
        self.speed = 0
        self.mileage = 0

    
    def accelerate(self, change):
        self.speed += change
        if self.speed > self.top_speed:
            self.speed = self.top_speed
        elif self.speed < 0:
            self.speed = 0


    def trip(self, hours):
        self.mileage += self.speed * hours


    def __str__(self):
        return f"{self.register_num} - Huippunopeus: {self.top_speed} km/h - Ajettu: {self.mileage} km"



car = Car("ABC-123", 142)
print(car)


car.accelerate(30)
car.accelerate(50)
car.accelerate(70)
print("Kiihdytyksen jälkeen nopeus: ", car.speed, "km/h")

car.accelerate(-200)
print("Häräjarrutuksen jälkeen nopeus: ", car.speed, "km/h")
