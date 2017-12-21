"""lab7_1
주제 : urllib 연습
작성일 : 17. 11. 27.
작성자 : 201632023 이지훈
"""

import urllib.request

req = urllib.request
d = urllib.request.urlopen("http://sw.skhu.ac.kr/")
status = d.getheaders()
for s in status:
    print(s)

"""lab7_2
주제 :
현재 디렉토리를 출력한 후, 사용자로부터 파일을 생성할 디렉토리를 입력받고,
입력된 디렉토리로 이동한 후 해당 디렉토리 아래에 있는 모든 파일 목록을 한 줄에 하나씩 출력하라
A. 만약, 입력한 디렉토리가 존재하지 않는다면, "입력한 디렉토리가 존재하지 않습니다." 를 출력한다.
Exception으로 처리하라. 일부러 오류를 발생시켜 Exception의 이름을 파악하라.
작성일 : 17. 11. 27.
작성자 : 201632023 이지훈
"""

import os # os를 import해줌

# 현재 디렉토리위치를 찾아주는 getcwd(). 안내문과 함께 적절하게 출력
print("현재 디렉토리 위치 :",os.getcwd())

# 사용자에게 이동할 경로를 입력받음
s = input("이동하실 경로를 입력하십쇼 : ")

# 디렉토리가 존재하지 않을 수 있으므로 예외처리를 해줌
try:
    os.chdir(s) # 예외가 나올 수 있는 곳.

    # 디렉토리를 발견했다면 디렉토리 아래의 파일들을 출력해주는 listdir() 사용
    for name in os.listdir(s):
        print(name)

except FileNotFoundError: # 예외 FileNotFoundError가 발생하면 적절한 안내문과 함께 에러 안내.
    print("입력한 디렉토리가 존재하지 않습니다.")

"""lab7_3
주제 :
사용자가 입력한 디렉토리로 이동한 후, 사용자가 입력한 이름의 새 디렉토리를 생성하라. 사용자가 입력한 디렉토리 아래에 test 디렉토리를 생성하라.
사용자가 입력한 디렉토리를 포함하여 해당 디렉토리와 test 디렉토리를 삭제하라.
삭제가 끝난 후, 사용자가 입력한 입력한 디렉토리의 부모 디렉토리의 파일 목록을 출력하라.(lab7_3)
작성일 : 17. 11. 27.
작성자 : 201632023 이지훈
"""

import os

# 사용자에게 이동할 경로를 입력받음
s1 = input("이동하실 경로를 입력하십쇼 : ")

# 디렉토리가 존재하지 않을 수 있으므로 예외처리를 해줌
try:
    os.chdir(s1) # 예외가 나올 수 있는 곳.
    s2 = input("설정할 폴더의 이름을 입력하세요 : ")
    os.makedirs(s1 + "\\" + s2)
    os.makedirs(s1 + "\\" + s2 + "\\"+ "test")
    # 디렉토리를 발견했다면 디렉토리 아래의 파일들을 출력해주는 listdir() 사용
    #for name in os.listdir(s1):
     #   print(name)

except FileNotFoundError: # 예외 FileNotFoundError가 발생하면 적절한 안내문과 함께 에러 안내.
    print("입력한 디렉토리가 존재하지 않습니다.")