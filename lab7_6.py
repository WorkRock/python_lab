"""lab7_6
주제 :
A. 프로그래밍이 아닌 수작업으로, C:\temp 디렉토리에 자신의 학번에 해당하는 디렉토리를 생성한 후, 임의의 파일을 3개 복사한다.
학번 디렉토리 아래에 room1 디렉토리를 만들어서 임의의 파일을 3개 복사한다.
room1밑에 room2 디렉토리를 만들어서 임의의 파일을 3개 복사한다. 자신의 학번 아래 room3 디렉토리를 만든다.
i. 여러 번 테스트하기 위해, 매번 생성하는 번거로움을 피하게 다른 디렉토리에 복사본을 만들어 놓는다.
B. 아래를 프로그래밍한다.
i. c:\temp아래의 자신의 학번 디렉토리 아래에 있는 모든 파일과 디렉토리를 삭제하라. 디렉토리인지 확인한 후, 디렉토리라면 해당 디렉토리 내에 있는 모든 파일을 삭제한 후, 해당 디렉토리를 삭제하라.
ii. 프로그램 실행 후 학번 아래에 파일과 디렉토리가 없음을 확인하라. 어떤 디렉토리 구조에서도 작동할 수 있게 프로그래밍하라.
작성일 : 17. 11. 29.
작성자 : 201632023 이지훈
"""
import os

def remove(b):
    os.chdir(b)
    print(b+"경로를 옮깁니다.")

    if (len(os.listdir(b)) != 0):
        print("디렉토리 내부의 파일들을 모두 찾습니다.")
        for name in os.listdir(b):
            listFile = os.path.join(b, name)
            if (os.path.isdir(listFile) == True):
                print("발견한 디렉토리 내부 : 디렉토리 존재. 디렉토리 안으로 들어갑니다.")
                return remove(listFile)
            else:
                print("발견한 디렉토리 내부 : 파일 발견. 파일을 삭제합니다.")
                os.remove(listFile)

        return remove(b)

    else:
        print("디렉토리 내부에 파일이 없으므로 디렉토리를 삭제합니다.")
        a = b.count("\\")
        l = b.split("\\", a)
        del (l[a])
        c = ""

        if(len(l) == 1):
            return print("모두 삭제 완료.")

        else:
            print("현 디렉토리의 상위 디렉토리로 위치를 옮깁니다.")
            os.removedirs(b)
            for s in l:
                if (s == "c:"):
                    c += s
                else:
                    c += "\\" + s

            return remove(c)





    """
    if(os.path.exists(b)):
        print("디렉토리 내부의 파일들을 모두 찾습니다.")
        for name in os.listdir(b):
            listFile = os.path.join(b, name)
            if(os.path.isdir(listFile)):
                if(os.path.exists(listFile)):
                    print("발견한 디렉토리 내부 : 파일 존재. 디렉토리 안으로 들어갑니다.")
                    return remove(listFile)
                else:
                    print("발견한 디렉토리 내부 : 파일 미존재. 디렉토리를 삭제합니다.")
                    os.removedirs(listFile)
                    return remove(b)
            else:
                print("디렉토리 내부 : 디렉토리 미존재. 파일을 삭제합니다.")
                print("\'"+name+"\'"+"파일을 삭제합니다")
                os.remove(listFile)
    return remove(b)"""

s1 = "c:\\temp\\201632023"
# 디렉토리가 존재하지 않을 수 있으므로 예외처리를 해줌
try:
   remove(s1)

except FileNotFoundError: # 예외 FileNotFoundError가 발생하면 적절한 안내문과 함께 에러 안내.
    print("입력한 디렉토리가 존재하지 않습니다.")