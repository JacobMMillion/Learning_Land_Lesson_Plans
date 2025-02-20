# robot.py

class Robot:
    def __init__(self, name, model):
        # Initialize the robot with a name and model.
        self.name = name
        self.model = model
        self.battery_level = 100  # Battery level starts at 100%

    def move(self, direction, steps):
        # Simulate the robot moving a number of steps in a given direction.
        print(f"{self.name} moves {steps} steps to the {direction}.")

    def speak(self, message):
        # The robot speaks a message.
        print(f"{self.name} says: '{message}'")

    def charge(self):
        # Recharge the robot's battery.
        self.battery_level = 100
        print(f"{self.name} is fully charged!")

# Example usage:
if __name__ == "__main__":
    r2d2 = Robot("R2-D2", "Astromech")
    r2d2.move("forward", 5)
    r2d2.speak("Hello, human!")
    r2d2.charge()