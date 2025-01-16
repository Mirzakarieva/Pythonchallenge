print("Day 1 - String Manipulation")
print("String Concatenation is done with the '+' sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

urname = input("Enter your name: ")

print(len(urname))


# Final exrecise

a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a:", a)
print("b:", b)


# Final project
print('Welcome to the band name Generator!')
city = input("What is the name of you city?\n")
pet = input("What is the name of a pet?\n")

brand_name = city + " " + pet
print(f"The name of your band could be {brand_name}")
