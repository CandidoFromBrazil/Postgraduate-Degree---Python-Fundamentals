class Car:
    # The Constructor: This sets up the initial "state" of each car
    def __init__(self, brand, model, year, fuel_level=100):
        self.brand = brand          # Public attribute
        self.model = model          # Public attribute
        self.year = year            # Public attribute
        self.__fuel_level = fuel_level  # Private attribute (cannot be accessed directly)

    # Instance Method: An action the car can perform
    def drive(self, distance):
        fuel_needed = distance * 0.1
        if self.__fuel_level >= fuel_needed:
            self.__fuel_level -= fuel_needed
            print(f"The {self.model} drove {distance} miles.")
        else:
            print(f"Not enough fuel to drive {distance} miles!")

    # Getter Method: Safely accessing private data
    def check_fuel(self):
        return f"Current fuel level: {self.__fuel_level}%"

    # Dunder Method: Controls how the object prints to the console
    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

# --- Using the Class ---

# 1. Create (instantiate) two different car objects
my_tesla = Car("Tesla", "Model 3", 2024)
old_truck = Car("Ford", "F-150", 1998, fuel_level=20)

# 2. Interact with the objects
print(my_tesla)            # Uses the __str__ method
my_tesla.drive(50)
print(my_tesla.check_fuel())

print("-" * 20)

print(old_truck)
old_truck.drive(300)       # This should fail due to low fuel