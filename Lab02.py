# Part 1

name = "M.N. Orban"
age = 23
height = 76
Favorite_color = "Lilac"

print(name)
print(age, height)

print(f"hello: {name}, {age} is my age!")
print(f"hello: {name}, I am {age}")

print(f"""
Name: {name}
Height: {height}
Favorite color: {Favorite_color}
Age: {age}
""")


import math
# from math import pi
# then just reference pi (personal note about syntax)

radius = 5
area = math.pi * radius**2
circle_variable = round(area, 1)
print(circle_variable)

# part 2

p2 = round(math.sqrt(age), 1)
print(p2)

print((math.sin(height)),(math.cos(height)))


# part 3

print(age + 5)
print(height - 4)
print(age * height)
print(height / 2)
print(age // 3)
print(age**2)

# part 4

Fahrenheit = float(input("Enter Temperature in Fahrenheit"))
Celsius = (Fahrenheit - 32) * 5/9.
Degree_symbol ="°"
print("Temperature is equal to", round(Celsius, 1), Degree_symbol, "Celsius")

# It's a secret
import webbrowser
url = "https://youtu.be/hlTisI_HSgw?si=qkcssfViOTdljEbs"
webbrowser.open(url)