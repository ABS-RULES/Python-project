import random
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
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("Your choice:\n")
print(game[your_choice])

com_choice = random.randint(0, 2)
print("\nComputer chose:\n")
print(game[com_choice])

if your_choice == 0:
    if com_choice == 0:
        print("It's a draw")
    elif com_choice == 1:
        print("You lose")
    else:
        print("You win!")

if your_choice == 1:
    if com_choice == 1:
       print("It's a draw")
    elif com_choice == 2:
       print("You lose")
    else:
       print("You win!")

if your_choice == 2:
    if com_choice == 2:
        print("It's a draw")
    elif com_choice == 0:
        print("You lose")
    else:
        print("You win!")