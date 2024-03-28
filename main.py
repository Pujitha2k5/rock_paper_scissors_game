import random
user_choice = int(input("enter your choice :0 for rock 1 for paper 2 for scissors"))
if user_choice >= 3 and user_choice < 0:
	print("invalid number")
else:
  computer_choice =random.randint(0,2)
  print("computer_choice:")
  print(computer_choice)
  if user_choice == computer_choice:
	   print("it is a tie")
  elif user_choice == 0 and computer_choice == 2:
       print("you wins")
  elif user_choice == 2 and computer_choice == 0:
       print("you lose")
  elif user_choice > computer_choice:
	   print("you win")
  elif user_choice < computer_choice:
	   print("you lose")