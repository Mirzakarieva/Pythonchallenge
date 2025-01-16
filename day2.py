# # task1
# Write a program that adds the digits in a 2-digit number. e.g. if the
# input was 35, then the output should be 3 + 5 = 8
two_digit_number = input("Type a 2 digit number : ")

summ = int(two_digit_number[0])+int(two_digit_number[1])

print(f"The sum of number's two digits is {summ}")

# # task2
# Change (3 * 3 + 3 / 3 - 3) so that, we get 3 as a result

print(3*(3+3)/3-3)

# BMI calculator: Index massi tela

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight/height**2

print("Your BMT is ", round(bmi))

# task4
#  Create a program using maths and f-Strings
#  that tells us how many days, weeks, months we have left if we live until 90 years old.
age = int(input("What's your current age? "))

years = 90-age
months = years*12
weeks = years*52
days = years*365

print(f"You have {days} days, {weeks} weeks, and {months} months left")

# final task
print('Welcome to the tip calculator.')
total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
amount_of_people = int(input("How many people to split the bill?"))

result = total * (1 + tip/100) / amount_of_people

print("Each person should pay: $", round(result, 2))
