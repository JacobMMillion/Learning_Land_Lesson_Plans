# car.py

class Car:


    def __init__(self, make, model, year):
        # This method is called when a new Car object is created.
        # It sets up the car's make, model, and year.
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0  # Start with the car not moving

    def accelerate(self, increase):
        # Increase the car's speed by a certain amount.
        self.speed = self.speed + increase
        print(f"The {self.model} is now going {self.speed} mph!")

    def brake(self, decrease):
        self.speed = self.speed - decrease
        print(f"The {self.model} slowed down to {self.speed} mph.")

    def honk(self):
        # Make the car honk.
        print("Beep beep!")
        
# Example usage:
if __name__ == "__main__":

    # my car
    my_car = Car("Toyota", "Corolla", 2022)

    # your car
    your_car = Car("Porche", "9-11", 2000)

    # honk
    my_car.honk()
    your_car.honk()

    # speed up
    your_car.accelerate(100)
    my_car.accelerate(40)

    # slow down
    your_car.brake(20)
    my_car.brake(10)