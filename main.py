#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D
import random
print("Welcome to Snake Water Gun:)\nRules:\n1. Enter 0 for Snake, 1 for Water and 2 for Gun!\n2. Once you lost, The Game will be over!\n")
win =0
flag =0
while(flag!=-1):
  try:
   user= int(input("Choose Your Input: "))
   print("Your Input is Snake") if user ==0 else print("Your Input is Water") if user ==1 else print("Your Input is Gun") if user ==2 else print("Invalid Input!") 
  except ValueError:
    print("Only 0,1 and 2 is Valid Input!")
    break
  computer = random.choice([0,1,2])
  print("Computer's Input is Snake") if computer ==0 else print("Computer's Input is Water") if computer ==1 else print("Computer's Input is Gun") if computer ==2 else print("Invalid Input!")
  if (user==0 and computer==1) or (user==1 and computer==2) or (user==2 and computer==0):
      win = win +1
      print(f"You have won, Your Score is {win}\n")
  elif (user==0 and computer==0) or (user==1 and computer==1) or (user==2 and computer==2):
      print(f"Match Tied, Your Score is {win}\n")
  else:
    flag=-1
    print(f"You Loss, Your Score is {win}\n")
    
  
  

print("Game Over!")