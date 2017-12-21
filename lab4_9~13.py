"""lab4_9
주제: 구구단 출력
작성일: 17. 09. 27.
작성자: 201632023 이지훈
"""

for i in range(2,10):
    print("\n%d단"%i)
    for j in range(1,9):
        print("%d x %d = %d"%(i,j,i*j))


"""lab4_10
주제: 밑변이 5개의 *로 구성된 직각 삼각형 출력
거꾸로 된 직각 삼각형 출력
작성일: 17. 09. 27.
작성자: 201632023 이지훈
"""
# 직각 삼각형
ver = "*"
for i in range(1,6):
    print(ver)
    ver += "*"

print("\n")

# 거꾸로 된 직각삼각형
rever = "*"

for i in range(1,6):
    print(rever*(6-i))

""" lab4_11
주제: 사용자가 입력한 영문자를 한 개씩 지워가며 출력
작성일: 17. 09. 27.
작성자: 201632023 이지훈
"""

a = input("문자열을 입력해 주세요. : ")
size = len(a)
b = " "
for i in range(0,size):
    print(b*i + a[i:size])

"""lab4_12
주제: 사용자로부터 5개의 숫자를 입력받아, 이를 리스트에 저장한 후 합과 평균을 구하여 출력한다.
작성일: 17. 09. 27.
작성자: 201632023 이지훈
"""

l = []
total = 0.0
aver = 0.0
a = 0.0
for i in range(0,5):
   a = float(input("정수 입력 : "))
   l.append(a)
   total += a

aver = total/5
print("합 : %.2f 평균 : %.2f"%(total,aver))

"""lab4_13
주제:
1. 사용자로부터 단어를 입력받는다.
2. 입력받은 단어를 출력한다.
3. 해당 단어에 포함된 알파벳을 알파벳 순서로 출력한다.
4. 해당 단어의 길이를 출력한다.
작성일: 17. 09. 27.
작성자: 201632023 이지훈
"""

a = input("단어 입력 : ")
print("입력 하신 단어 : ",a)
l = []

for i in range(0,len(a)):
    l.append(a[i])

l.sort()
print('정렬 : ',l)
print('길이 : ',len(l))