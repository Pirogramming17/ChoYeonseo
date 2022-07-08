# 8단계



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
    player1 = brGame()
    for i in range(player1):
        num += 1
        print("player A :", num)
        if num >= 31:
            print("playerB win!")
            break
        
    if num >= 31:
        break
    
    player2 = brGame()
    for j in range(player2):
        num+=1
        print("player B :", num)
        if num >= 31:
            print("playerA win!")
            break
    
    if num >= 31:
        break