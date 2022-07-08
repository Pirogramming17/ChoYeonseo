num = 0

while True:
  try:
    p1 = int(input("부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능): "))
  except ValueError:
    print("정수를 입력하세요: ")
  else:
    while True:
      if p1 in range(1,4):
        break
      else:
        p1 = int(input("1,2,3 중 하나를 선택하세요:"))
    break

for i in range(p1):
  num+=1
  print("playerA :", num)