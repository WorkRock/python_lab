"""lab7_7_1
주제 : 현재 디렉토리 아래의 fruits.txt 파에 사용자가 입력하는 과일을 한 줄에 하나씩 3개를 추가하여 저장하라.
A. fruits.txt 파일에 저장되었는지 열어서 확인하라.
작성일 : 17. 12. 04.
작성자 : 201632023 이지훈
"""

f = open("fruits.txt","a")
for i in range(0,3):
    fruit = input("과일 입력 : ")
    f.write(fruit + "\n")
f.close()