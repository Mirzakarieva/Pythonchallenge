import random

result = random.randint(0, 1)

if result == 1:
    print("Heads")
else:
    print("Tails")

row1 = ["*", "*", "*"]
row2 = ["*", "*", "*"]
row3 = ["*", "*", "*"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

coordinate = int(input("Where do you want to put the treasure?"))
a = coordinate//10-1
b = coordinate % 10-1
map[b][a] = "x"
print(f"{row1}\n{row2}\n{row3}")


names_string = input("Give me everybody's names, separated by a comma and space. ")
names = names_string.split(", ")

end = len(names)-1
random_index = random.randint(0, end)
random_chel = names[random_index]
print(f"{random_chel} is going to buy the meal today!")


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
         _______)
         ________)
        ________)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
         _______)
         ________)
      (____)
---.__(___)
'''
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("You typed an invalid number, you lose!")

computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == 2 and computer_choice == 0:
    print("You loose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice > computer_choice:
    print("You win!")
elif user_choice < computer_choice:
    print("You loose!")
else:
    print("draw")
