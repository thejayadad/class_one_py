import random

balance = 0
num1 = random.randint(1,3)
num2 = random.randint(1,3)
num3 = random.randint(1,3)
user_deposit = int(input("How much do you wanna deposit? "))

balance += user_deposit



play = True
while play:
    print("*************WELCOME TO SLOTS**********************")
    user_wager = int(input("How much do you want to wager? "))
    if user_wager > user_deposit:
        print("Not enough money, try again")
        break
    slot = []
    if num1 == num2 & num1 == num3 & num2 == num3:
        slot.append(num1)
        slot.append(num2)
        slot.append(num3)
        print(slot)
        balance += user_wager
        print(balance)
        print("match")

    else:
        slot.append(num1)
        slot.append(num2)
        slot.append(num3)
        balance -= user_wager
        print(slot)
        print("mis-match")
        print(balance)
        if(balance <= 0):
            print("Game Over! ")
