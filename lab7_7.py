"""lab7_7
주제 : 파일 생성 -> 현재 디렉토리 아래에 fruits.txt 파일을 생성하여,
생성자가 입력하는 과일을 한 줄에 하나씩 3개를 저장하라.
->fruits.txt 파일에 저장되었는지 열어서 확인하라
작성일 : 17. 12. 04.
작성자 : 201632023 이지훈
"""

f = open("fruits.txt","w")
for i in range(0,3):
    a = input("과일 입력 : ")
    f.write(a + "\n")
f.close()