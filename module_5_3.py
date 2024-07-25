class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other,House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name,self.number_of_floors + value)

    def __iadd__(self, value):
        if isinstance(value, int):
            return House(self.name,self.number_of_floors + value)

    def __radd__(self, value):
        if isinstance(value, int):
            return House(self.name,self.number_of_floors + value)



h1 = House('Московский', 9)
h2 = House('Самоцветы', 15)

print(h1)
print(h2)
print(h1 == h2) #__eg__
print(h1+3) #__add__
h2 += 1 # __iadd__
print(h2)
print(12 + h1) # __radd__
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__





