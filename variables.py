# Variables
# Container for values, values can be of different types like string, int, float and boolean

# Strings
first_name = "Goofy"
fav_food = "cheese"

print(f"Hey, I want to introduce you {first_name}")
print(f"His favorite food is {fav_food}")

# Integers
age = 39
qty_friends = 1
print(f"Also his age is {age} years old")
print(f"He has {qty_friends} best friend!")

# Float
height = 6.1
fav_number = 3.43253456
print(f"His height is around {height} ft")
print(f"His fav number is", f"{fav_number:.3f}") # :.number controls precision of float
print(f"However, he also like when his fav number looks like {round(fav_number, 1)}") # round function also helps to do the same

# Boolean
true = True
false = False
likes_programming = True
for_sale = False
print(f"I'm printing something that's {true}")
print(f"I'm printing something that's {false}")
print(f"Goofy also likes to build programs: {likes_programming}")

if for_sale:
    print("The product you purchased has a discounted price")
else:
    print("The product you purchased has NOT a discounted price")