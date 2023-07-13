import random
print("Hello!!!, let Roll the dice 😉")
print("Good luck!!!")
def dice_roll():
    print("Hello!!!, let Roll the dice 😉")
    print("Good luck!!!")
    dice1= random.randint(1,6)
    print("dice1:", dice1)
    dice2= random.randint(1,6)
    print("dice1:", dice2)
    return dice1 + dice2
while True:
     
     ans = input("Roll dice(yes/no)? ")
     if ans.lower()== 'yes':
        print("total:", dice_roll())
     elif ans.lower() =='no':
        print('Thank you for playing')
        break 
