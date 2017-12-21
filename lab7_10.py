"""lab7_10
주제 : A. fruits.txt의 과일 중 하나의 offset 위치 값을 입력 받은 후,
해당 값을 같은 글자수의 다른 과일로 변경하여 저장한 후, fruits.txt 파일에 저장된 모든 과일을 출력하라.
작성일 : 17. 12. 06.
작성자 : 201632023 이지훈
"""

f = open("fruits.txt","r+")
count = len(f.readlines())
f.seek(0)
for a in range(0,count):
    print(str(a+1)+"번 offset종류 : ",f.tell())
    f.readline()

a = int(input("offset입력 : "))

f.seek(a)
fruit = f.readline()
print(fruit)

while(1):
    length = len(fruit)-1
    print("글씨의 길이 : ",length)
    s = input("변경할 과일 입력(글자 수가 같아야 합니다). : ")
    if(len(s) != length):
        print("재입력이 필요합니다")
    else:
        break
f.seek(a)
f.write(s)
print()
f.seek(0)
for a in range(0,count):
    print(f.tell())
    print(f.readline())
f.close()