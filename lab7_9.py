"""lab7_9
주제 : A. fruits.txt에 저장된 각 데이터가 파일 포인터 값(offset 값)과 데이터 값을 출력하라.
작성일 : 17. 12. 06.
작성자 : 201632023 이지훈
"""

f = open("fruits.txt","r")

for a in range(0,6):
    print(f.tell())
    print(f.readline())

f.close()