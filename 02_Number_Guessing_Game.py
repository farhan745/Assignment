import random as computer_choice_number
count = 0
while True:
  choice_your_num = int(input("Enter your guess: "))
  computer_num = computer_choice_number.randint(1,100)
  if computer_num==choice_your_num:
    count+=1
    print(f"Congratulations! You've guessed the number in {count} attempts.")
    break
  elif computer_num>choice_your_num:
    print("Too low!")
    count+=1
  else:
    print("Too high!")
    count+=1
  
