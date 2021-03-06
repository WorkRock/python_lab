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
    os.chdir(b) # 경로를 옮겨줌
    print(b+"으로 경로를 옮깁니다.")

    if (len(os.listdir(b)) != 0): # 만약 b내부에 파일과 폴더가 한 개라도 존재할 시
        print("디렉토리 내부의 파일들을 모두 찾습니다.")
        for name in os.listdir(b): # listdir을 사용, 파일들을 검색
            listFile = os.path.join(b, name) # 검색한 파일을 경로와 합쳐 삭제가 유용하게 해줌
            if (os.path.isdir(listFile)): # 만약 발견한 것이 폴더일시
                print("\'"+name+"\'"+ "디렉토리를 발견하였습니다.")
                if (len(os.listdir(listFile)) == 0): # 그리고 발견한 폴더의 내부가 비어있을 시
                    print("\'" + name + "\'" + "디렉토리의 내부가 비어있어 삭제합니다.")
                    os.removedirs(listFile) # 폴더 삭제
                    return remove(b) # 재귀로 다시 불러줌
                else: # 폴더의 내부에 파일이 존재할 시
                    print("\'" + name + "\'" + "디렉토리의 내부에 파일이 있어 들어갑니다.")
                    return remove(listFile) # 재귀로 그 폴더안에 들어가줌

            else: # 만약 발견한 것이 파일일 시
                print("\'"+name+"\'"+"파일을 삭제합니다.")
                os.remove(listFile) # for문을 이용해 파일들 일괄 삭제

        return remove(b) # 그 후 재귀함수로 다시 불러줌

    else: # 만약 b내부에 파일과 폴더가 존재하지 않을 시
        print("디렉토리 내부에 파일이 존재하지 않습니다.")
        a = b.count("\\") # \의 갯수를 세어주고
        l = b.split("\\", a) # \를 기준으로 \의 갯수만큼 b를 나누어줍니다.
        del (l[a]) # 그 후, 가장 뒷부분의 요소를 제거하면 상위 폴더로 넘어갑니다.
        b = "" # b는 아무것도 없는 상태로 초기화 해줍니다.
        if(len(l) == 1): # 만약 'c:'밖에 남지 않은 상태라면 삭제 완료를 알려주고 프로그램을 종료합니다.
            return print("모두 삭제 완료.")
        else: # 그게 아니라면 상위 폴더로 이동해 줍니다.
            print("현 디렉토리의 상위 디렉토리로 위치를 옮깁니다.")
            for s in l:
                if (s == "c:"): # 'c:'의 앞부분에는 \가 붙지 않으므로 이렇게 처리해 줍니다.
                    b += s
                else: # c:가 아닐시 \를 붙여줍니다.
                    b += "\\" + s

            return remove(b) # 다쉬 재귀로 함수를 불러줍니다.


s1 = "c:\\temp\\201632023"
# 디렉토리가 존재하지 않을 수 있으므로 예외처리를 해줌
try:
   remove(s1)

except FileNotFoundError: # 예외 FileNotFoundError가 발생하면 적절한 안내문과 함께 에러 안내.
    print("입력한 디렉토리가 존재하지 않습니다.")