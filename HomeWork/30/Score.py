"""Score
주제 :
score.txt 파일에 이름, 국어점수, 영어점수, 수학 점수를 :으로 구분하여 10개 이상 저장한다.
A. 예:
김일수: 35: 80: 90
김이수: 67: 77: 99
B. 데이터를 파일에서 읽어 들여서 전체 평균, 각 학생의 평균 점수, 각 과목당 평균 점수를 출력하라.
D. 만약 현재 디렉토리에 score.txt 파일이 없다면, “파일이 존재하지 않습니다”라는 문구를 출력하고 프로그램을 종료한다.
E. 참고할 메쏘드
  문자열.split, 문자열.strip(앞뒤 필요 없는 문자 제거. 매개변수가 없으면 white space 제거)
작성일 : 17. 12. 10.
작성자 : 201632023 이지훈
"""
def inputScore():
    """
    점수와 이름을 입력받고, 이름, 점수를 리턴해준다.
    :return: 이름, 각각의 점수들
    """
    name = input("이름 입력 : ")
    while(1):
        try: # int형에 str형이 들어올시 예외처리
            kor = int(input("국어 점수 입력 : "))
            if(kor < 0 or kor > 100): # 점수가 0보다 작고 100보다 클 시 반복문 재호출
                print("점수 재입력이 필요합니다. 점수를 처음부터 다시 입력해 주세요.")
                continue
            eng = int(input("영어 점수 입력 : "))
            if (eng < 0 or eng > 100):
                print("점수 재입력이 필요합니다. 점수를 처음부터 다시 입력해 주세요.")
                continue
            math = int(input("수학 점수 입력 : "))
            if (math < 0 or math > 100):
                print("점수 재입력이 필요합니다. 점수를 처음부터 다시 입력해 주세요.")
                continue
        except ValueError: # 예외처리
            print("오직 숫자만을 입력해 주십쇼.(0~100사이)")
            continue

        break

    return name,kor,eng,math

def personalAver(str):
    """
    문자열을 매개변수로 받아 분리 후 다시 리턴해준다.
    :param str: 매개변수로 받는 문자열.
    :return: 이름, 각 점수들, 개인의 평균
    """
    a = str.split(": ") # 문자열을 ': ' 을 기준으로 나누어줌
    s = [] # 문자열을 저장할 배열
    for o in a:
        s.append(o.strip()) # 각각 원소의 공백을 제거한 후 배열에 저장
    name = s[0]
    kor = s[1]
    eng = s[2]
    math = s[3]
    aver = (int(s[1]) + int(s[2]) + int(s[3]))/3 # 평균값
    return name, kor, eng, math, aver # 이름, 각 점수들, 평균 리턴

try: # 파일이 존재하지 않을시 예외처리
    arr = [] # 각각의 점수와 이름들을 저장할 배열 arr
    allAver = 0 # 전체의 평균을 나타낼 allAver
    f = open("score.txt", "r+") # 읽기,쓰기 모드로 오픈
    size = int(input("몇 명의 정보를 입력하시겠습니까? : "))
    for i in range(0,size):
        s = inputScore()
        upload = s[0] + ": " + str(s[1]) + ": " + str(s[2]) + ": " + str(s[3]) + "\n"
        f.write(upload)
        arr.append(personalAver(upload)) # score에 저장했던 문자열을 매개변수로 넘겨줌
        allAver += arr[i][4] # 전체 평균에 각각의 평균을 더해줌

    print("==== 전체 평균 ====")
    print("%.2f"%(allAver/size))
    print("==== 각 학생 평균 ===")
    for i in range(0,size):
        print(arr[i][0] + ": " + str(arr[i][4]))
    print("==== 각 과목 평균 ====")
    korAver = 0
    engAver = 0
    mathAver = 0
    for i in range(0, size):
        korAver += int(arr[i][1])
        engAver += int(arr[i][2])
        mathAver += int(arr[i][3])

    print("국어 평균 : %.2f"%(korAver/size))
    print("영어 평균 : %.2f"%(engAver/size))
    print("수학 평균 : %.2f"%(mathAver/size))


except FileNotFoundError: # 에러문구와 함께 프로그램 종료
    print("\'score.txt\'파일이 존재하지 않습니다.")