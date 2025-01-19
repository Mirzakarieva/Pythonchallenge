number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

# BMI pro ;)
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# • Under 18.5 they are underweight
# • Over 18.5 but below 25 they have a normal weight
# • Over 25 but below 30 they are overweight
# • Over 30 but below 35 they are obese
# • Above 35 they are clinically obese.

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / height ** 2

if bmi < 18.5:
    message = " underweight"
elif bmi < 25:
    message = " normal weighted"
elif bmi < 30:
    message = " overweight"
elif bmi < 35:
    message = " obese"
else:
    message = " clinically obese"
print(f"Your BMT is {round(bmi)}, you are {message}.")

# leap year
# Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February.
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
# Congratulations, you've got a job at Python Pizza.
# Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

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

# Other 2 ways for pepperoni:
# 1:
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# 2:
# if add_pepperoni == "Y":
#     bill += 3 if size != "S" else 2


if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

# Love calculator
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2-digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is x, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is y, you are alright together.
# Otherwise, the message will just be their score. e.g.:
# "Your score is z.
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is his/her name? \n")

name1 = name1.lower()
name2 = name2.lower()
L = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e = name1.count("e") + name2.count("e")

t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")

result = (t + r + u + e) * 10 + (L + o + v + e)

if result <= 10 or result >= 90:
    message = "you go together like coke and mentos."
elif 40 >= result <= 50:
    message = "you are alright together."
else:
    message = ""

print(f"Yor score is {result},", message)

# Treasure something
print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island. Your mission is to find the treasure.")
direction = input('You\'re at a crossroad,crossroad, where do you want to go? Type "left" or "right".').lower()
if direction == "left":
    action = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat.'
                   ' Type "swim" to swim across.').lower()
    if action == "wait":
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue."
                     "Which colour do you choose?").lower()
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
