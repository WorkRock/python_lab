"""lab7_8
주제 : 3. (파일 읽기, lab7_8) fruits.txt 파일에 저장되어 있는 과일 이름들을 출력하라. 몇 줄의 과일이 저장되었든지 상관없이 출력됨을 보장하라.
작성일 : 17. 12. 04.
작성자 : 201632023 이지훈
"""

f = open("fruits.txt","r")
fruit = f.readlines()
for a in fruit:
    print(a)
f.close()