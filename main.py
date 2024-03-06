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

Manos=[rock,paper,scissors]
flag=0

index_ususario=int(input("What do you chosse 0 Rock ,1 paper ,2 Scissors:  "))
if (index_ususario>=3 or  index_ususario<0):
  print("Youuu loseeee ")
  flag=1

if flag!=1:
  print("TU: ")
  print(Manos[index_ususario])
  random_num=random.randint(0,2)


  print("Pc: ")
  print(Manos[random_num]);
  print("\n\n")



  if index_ususario==random_num:
    print("TIED\n\n")
  elif index_ususario==0 and random_num==2:
    print("Youu winn")
  elif index_ususario==2 and random_num==0:
    print("You loseee ")
  elif random_num>index_ususario:
    print("You loseee ")
  elif index_ususario>random_num:
    print("Youu winn")

