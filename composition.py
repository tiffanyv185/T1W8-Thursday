class Engine:
    def __init__(self, horsepower, type):
        self.horsepower = horsepower
        self.type = type
    
    def start(self):
        return f"Engine with {self.horsepower} horsepower started"
    
class Wheel:
    def __init__(self,size):
        self.size = size
    
    def roll(self):
        return f"Wheel of size {self.size} is rolling."
    
    
class Car:
    def __init__(self, brand, model, engine, wheels):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.wheeks = wheels

    def start(self):
        return self.engine.start()
    
    def drive(self):
        wheel_actions = [wheel.roll() for wheel in self.wheels]
        return f"[self.brand] {self.model} is driving" + join(wheel_actions)
    

    # Creating an engine instance
engine = Engine(350, 'V8')

    # creating wheel instances
wheels = [Wheel('18 inch') for _ in range(4)]

    # creating a car instance using engine and wheel instances
car = Car('Ford', 'Mustang', engine, wheels)

    # use car object
print(car.start())