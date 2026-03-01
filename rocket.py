class Rocket:
    def __init__(self, name, fuel_level):
#Initial Attributes
        self.name = "Apollo"
        self.fuel_level = 80
        print(f"--- Rocket '{self.name}' has been initialized. ---")

    def refill_fuel(self, amount):
#Add specified amount of fuel to the current fuel level. Refill the fuel
        self.fuel_level += amount
        print(f"Fuel added. New level: {self.fuel_level}")

    def launch(self):
#Check the fuel level and Try to launch
        if self.fuel_level >= 10:
            self.fuel_level -= 10
            print(f"{self.name} launched successfully! 🌍 -> 🌕")
        else:
            print("Error: Not enough fuel! Please add fuel.")

#TEST

#Create a rocket instance
my_rocket = Rocket("Apollo", 5)

#Try to launch with insufficient fuel
my_rocket.launch()

#Add fuel
my_rocket.refill_fuel(5)

#Try to launch again
my_rocket.launch()