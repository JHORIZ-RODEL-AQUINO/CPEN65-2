from math import pi


class Circle:
    def __init__(self, value=0.0):  # default value = 0, default given = radius
        self._value = value


class Radius(Circle):
    def __init__(self, value):
        super().__init__(value)
        self._name = "radius"

    def area(self):
        return round(pi * self._value**2, 2)

    def display_area(self):
        print(f"A circle with a {self._name} of {self._value} has an area of {self.area()}")


class Diameter(Radius):
    def __init__(self, value):
        super().__init__(value)
        self._name = "diameter"

    def area(self):
        return round(pi * self._value**2 / 4, 2)


class Perimeter(Radius):
    def __init__(self, value):
        super().__init__(value)
        self._name = "perimeter"

    def area(self):
        return round(self._value**2 / pi / 4, 2)


while True:
    print("""
Calculate the area of a circle given by:
a) Radius
b) Diameter
c) Perimeter

type 'exit' to exit
""")
    choice = input("Choice: ").lower()

    if choice == "a":
        x = float(input("Enter the value of radius: "))
        Radius(x).display_area()

    elif choice == "b":
        x = float(input("Enter the value of diameter: "))
        Diameter(x).display_area()

    elif choice == "c":
        x = float(input("Enter the value of perimeter: "))
        Perimeter(x).display_area()

    elif choice == "exit":
        break

    else:
        print("Please choose from a, b, and c only")
