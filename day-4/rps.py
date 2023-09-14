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

#Write your code below this line 👇

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if(choice == 0):
    print(rock)
elif(choice == 1):
    print(paper)
else:
    print(scissors)

comp = random.randint(0,2)
if(comp == 0):
    print(f"Computer chose: {rock}")
    if(choice == 2):
        print("You Lose.")
    else:
        print("You Win!")
elif(comp == 1):
    print(f"Computer chose: {paper}")
    if(choice == 0):
        print("You Lose.")
    else:
        print("You Win!")
else:
    print(f"Computer chose: {scissors}")
    if(choice == 1):
        print("You Lose.")
    else:
        print("You Win!")
