a = int(input("정수 입력 : "))

if(a%3 == 0 and a%4 == 0):
    print("3과 4의 공배수")
elif(a%3 == 0):
    print("3의 배수")
elif(a%4 == 0):
    print("4의 배수")
else:
    print("3의 배수도, 4의 배수도 아닙니다")