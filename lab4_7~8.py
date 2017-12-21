""" lab4_7
주제: for 반복문
작성일: 17. 09. 25.
작성자: 201632023 이지훈
"""

l = [1, 3, 5]
for i in range(1,6,2):
    print(i)
print(l)

s = "성공회대학교"

for i in s:
    print(i)

# 1에서 부터 100까지 합을 구하시오
total1 = 0
for i in range(1, 101):
    total1 += i
print("합 :",total1)

# 1에서 100까지 3의 배수의 합을 구하여 출력하시오.
total2 = 0
for i in range(3, 101, 3):
        total2 +=i
print("합 :",total2)
# for i in range(99, 0, -3): <- 이것도 된다

# 1에서 부터 100까지 합을 while을 이용하여 구하시오
total3 = 0
i=1
while i < 101:
    total3 += i
    i +=1
    if(i==50):
        break
print("합 :",total3)

# 1에서 100까지 3의 배수의 합을 while을 이용하여 출력하시오.
total4 = 0
i=1
while i <=100:
    i +=1
    if(i%3 !=0):
        continue
    total4 += i
print("합 :",total4)
""" lab4_8
주제: for 반복문
작성일: 17. 09. 25.
작성자: 201632023 이지훈
"""

# 사용자로부터 입력 받은 수의 모든 약수 구하기
a = int(input("수를 입력하세요 : "))
for i in range(1, a+1):
    if(a%i == 0):
        print(i)

# 1부터 사용자로부터 입력 받은 수까지 각각의 모든 약수 구하여 리스트 형태로 출력
for i in range(1, a+1):
    l = []
    for n in range(1,i+1):
        if(i%n == 0):
            l.append(n)
    print("%s의 약수 : "%i,l)