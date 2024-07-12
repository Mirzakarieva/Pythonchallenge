# # task1
a = input("Type an a ,a is 2 digit number : ")

summ = int(a[0])+int(a[1])

print(f"The sum of a's two digits is {summ}")

# # task2

print(3*(3+3)/3-3)

# BMI Index massi tela

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight/height**2

print("Your BMT is ", round(bmi))

# task4

age = int(input("What's your current age? "))

years = 90-age
months = years*12
weeks = years*52
days = years*365

print(f"You have {days} days, {weeks} weeks, and {months} months left")

# final task

total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
amount_of_people = int(input("How many people to split the bill?"))

result = total * (1 + tip/100) / amount_of_people

print("Each person should pay: $", round(result, 2))
