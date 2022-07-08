# 9단계

import random

def brGame():
        while True:
            try:
                p=int(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능): "))
            except ValueError:
                print("정수를 입력하세요: ")
            else:
                while True:
                    if p in range(1,4):
                        break
                    else:
                        p=int(input("1,2,3 중 하나를 선택하세요:" ))
                return p
            break



num = 0
while True:
    player = brGame()
    for i in range(player):
        num += 1
        print("player :", num)
        if num >= 31:
            print("computer win!")
            break
        
    if num >= 31:
        break
    
    computer = random.randint(1,3)
    for j in range(computer):
        num+=1
        print("computer :", num)
        if num >= 31:
            print("player win!")
            break
    
    if num >= 31:
        break