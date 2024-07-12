import random
# av score
student_heights = input("Input a list of student heights ").split()
length = 0
sum = 0
for height in student_heights:
    length += 1
    sum += int(height)
average = round(sum/length)
print(average)

# highest score
student_scores = input("Input a list of student scores").split()
max = 0

for score in student_scores:
    score = int(score)
    if score > max:
        max = score
print(max)

# sum of all even numbers from 0 till 100
sum = 0
for i in range(2, 101, 2):
    sum += i
print(sum)

# fizzbuzz
for n in range(0, 101):
    if n % 3 == 0 and n % 5 == 0:
        n = "FizzBuzz"
    elif n % 3 == 0:
        n = "Fizz"
    elif n % 5 == 0:
        n = "Buzz"
    print(n)


# passwords
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ["!", "#", '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password = []
for letter in range(0, nr_letters):
    rand_index = random.randint(0, len(letters)-1)
    password.append(letters[rand_index])
# better version
# password.append(random.choice(letters))

for number in range(0, nr_numbers):
    rand_index = random.randint(0, len(numbers)-1)
    password.append(numbers[rand_index])
# better version
# password.append(random.choice(numbers))

for symbol in range(0, nr_symbols):
    rand_index = random.randint(0, len(symbols)-1)
    password.append(symbols[rand_index])
# better version
# password.append(random.choice(symbol))

random.shuffle(password)
final_password = ''.join(password)

print(f"The password is: {final_password}")