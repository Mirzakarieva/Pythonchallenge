number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

# BMI pro ;)


height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / height ** 2

if bmi < 18.5:
    message = " underweighted"
elif bmi < 25:
    message = " normal weighted"
elif bmi < 30:
    message = " overweighted"
elif bmi < 35:
    message = " obesed"
else:
    message = " clinically obesed"
print(f"Your BMT is {round(bmi)}, you are {message}.")

# leap year
year = int(input("Which year do you want to check? "))

if year % 400 == 0:
    result = "Leap"
elif year % 100 == 0:
    result = " not leap"
elif year % 4 == 0:
    result = "Leap"
else:
    result = "Not leap"

print(f"The year {year} is {result} year")

# Pizza


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
else:
    bill = 25
    if add_pepperoni == "Y":
        bill += 3

# the other way to pepperoni
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3


if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

# Love calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is his/her name? \n")

name1 = name1.lower()
name2 = name2.lower()
l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e = name1.count("e") + name2.count("e")

t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")

result = (t + r + u + e) * 10 + (l + o + v + e)

if result <= 10 or result >= 90:
    message = "you go together like coke and mentos."
elif result >= 40 and result <= 50:
    message = "you are alright together."
else:
    message = ""

print(f"Yor score is {result},", message)

# Treasure something
print("Welcome to Treasure Island. Your mission is to find the treasure.")
direction = input("left or right?")
if direction == "left":
    action = input("swim or wait?")
    if action == "wait":
        door = input("Which door? red, blue or yellow?")
        if door == "red":
            print("Burned by fire. Game Over.")
        elif door == "blue":
            print("Eaten by beasts. Game Over.")
        elif door == "yellow":
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")