class Car:

    def __init__(self, year):
        self.year = year

    def age(self):
        age = 2020 - self.year
        return age



classic = Car(1959)

print(classic.age())
