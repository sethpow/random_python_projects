class car():
    def __init__(self, make, model, year, miles=0, condition='New'):
        self.make = make
        self.model = model
        self.year = year
        self.miles = miles
        self.condition = condition

    def display_all(self, condition=True):
        if(condition):
            print(f"Make: {self.make} - Model: {self.model} - Year: {self.year} - miles: {self.miles} - Condition: {self.condition}")
        else:
            print(f"Make: {self.make} - Model: {self.model} - Year: {self.year}")


my_car = car('Toyota', 'Tundra', 2012, 100, 'Used')
my_car.display_all()