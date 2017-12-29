"""
A. 프로그래밍이 아닌 수작업으로, C:\temp 디렉토리에 자신의 학번에 해당하는 디렉토리를 생성한 후, 임의의 파일을 3개 복사한다.
학번 디렉토리 아래에 room1 디렉토리를 만들어서 임의의 파일을 3개 복사한다.
room1밑에 room2 디렉토리를 만들어서 임의의 파일을 3개 복사한다. 자신의 학번 아래 room3 디렉토리를 만든다.
i. 여러 번 테스트하기 위해, 매번 생성하는 번거로움을 피하게 다른 디렉토리에 복사본을 만들어 놓는다.
B. 아래를 프로그래밍한다.
i. c:\temp아래의 자신의 학번 디렉토리 아래에 있는 모든 파일과 디렉토리를 삭제하라. 디렉토리인지 확인한 후,
디렉토리라면 해당 디렉토리 내에 있는 모든 파일을 삭제한 후, 해당 디렉토리를 삭제하라.
ii. 프로그램 실행 후 학번 아래에 파일과 디렉토리가 없음을 확인하라. 어떤 디렉토리 구조에서도 작동할 수 있게 프로그래밍하라.
"""

import os #os 모듈
import os.path #os.path 모듈

def recursion(path): #recursion함수 매개변수 path
    list=os.listdir(path) #path에 있는 파일과 디렉토리를 리스트로 만든다
    for i in list: #리스트 안의 요소들을 반복한다.
        path = os.path.join(path, i) #path랑 요소랑 더한다.
        if os.path.isdir(path) == True: #path가 디렉토리면
                recursion(path) #다시 recursion()을 실행한다.
                os.rmdir(path) #디렉토리를 지우고
                r = os.path.split(path) #이전 경로를
                path = r[0] #path에 저장한다.
        else: #path가 파일이면
            os.remove(path) #그 파일 지우고
            l = os.path.split(path) #그 이전 경로로 되돌아간다.
            path = l[0]

path='C:\\Temp\\학번'
recursion(path) #함수에 C:\\Temp\\힉번를 전달해준다.
print(os.listdir(path)) #프로그램 실행 후 학번 아래에 파일과 디렉토리가 없음을 확인
