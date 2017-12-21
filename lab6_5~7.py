"""lab6_5
주제 :
1. 입력된 문장엣 숫자부분을 모두 출력하라
ex) 2017년 3월 8일 5000원
2. 입력된 문장을 ,를 기준으로 나누어 출력하라
ex) 김치, 고추장, 된장
3. 입력된 문장에서 / 를 -로 변경하라
ex) 2017/05/06
4. 입력된 문장에서 '<' 이후에 나오는 단어들을 출력하라
ex) <2015> <김일수> <성공회대학교>
작성자 : 201632023 이지훈
작성일 : 17. 11. 20.
"""

import re

#1
result = re.findall("\d+","2017년 3월 8일 5000원")
print(result)
#2
result = re.split("[,]+","김치, 고추장, 된장")
print(result)
#3
result = re.sub("/","-","2017/05/06")
print(result)
#4
result = re.split("[<]+","<2015> <김일수> <성공회대학교>")
print(result) # 제일 앞의 <에 의해 ""이 결과에 포함되어 있다 <- 틀린예시
for i in result:
    if i == "": # 제일 앞의 ""은 건너 뛴다.
        continue
    r = re.search("[>]+",i) # '>'으로 끝나는 지점을 찾는다 []는 없어도 된다.
    print(i[0:r.end()-1]) # '>' 앞까지 슬라이싱해서 출력
"""lab6_6
주제 : 예외처리 연습
작성자 : 201632023 이지훈
작성일 : 17. 11. 20.
"""

"""예외처리 예시
try:
    num = int(input("숫자를 입력 : "))
except ValueError:
    print("숫자를 입력하세요")
"""

"""
정수 입력이 들어올 때까지 반복 후 성공 시, 입력 받은 정수 출력하기
"""

while(True):
    try:
        num = int(input("숫자를 입력 : "))
        print("입력한 정수 : ",num)
        break
    except ValueError:
        print("숫자를 입력하세요")

"""
주제 : 예외처리 연습
정수 입력이 들어올 때까지 반복 후 성공 시, 입력 받은 정수 출력하기.
1.try, exception, else, finally 이용하여 정수가 제대로 입력될 때 까지 반복후
    A.정수가 아닌 값이 들어오면, "다시 입력하세요."
    B.정수가 제대로 들어오면, 입력된 정수 출력.
    C.정수가 아닌 값이 들어오든, 아닌 값이 들어오든 언제나 "try-exception 연습"을 출력.
2. 100 이하의 양의 정수만 입력 받도록 수정
    A. 0이하 또는 100초과의 정수가 입력되면, ValueError를 발생(raise)시키고
    B. "1과 100사이의 수를 입력해 주세요." 출력
작성자 : 201632023 이지훈
작성일 : 2017. 11. 22(수정)
"""

while 1: # 무한 반복
    try: # try 사용, error가 뜨면 except로 넘어감
        num=int(input("숫자를 입력하세요: ")) # 수를 입력 받음
        if(num<=0 or num>100): # 만약 num이 100이하의 양의 정수가 아니라면
            raise ValueError # ValueError 발생
    except ValueError: # ValueError 발생시
        print("1과 100사이의 수를 입력해 주세요.") # 안내문과 함께 에러 안내
    else: # 조건을 모두 충족할시
        print("입력 받은 정수: ",num) # num을 출력해주고
        break # 프로그램 종료
    finally: # 어떤 상태에 상관없이 출력
        print("try-exception 연습")

"""lab6_7
주제 :
1. divide 함수 정의
A. 두개의 매개변수 x, y를 받아서 x를 y로 나눈 값을 반환
B. ZeroDivisionError 발생시 "0으로 나눌 수 없습니다" 출력
C. 성공시 나눈 결과 출력
작성자 : 201632023 이지훈
작성일 : 2017. 11. 22
"""

def divide(x,y):
    """
    매개변수로 받은 두 정수를 나누어주는 함수
    :param x: 1번 매개변수
    :param y: 2번 매개변수
    :return: 1을 2번으로 나눈 값
    """
    try: # 에러가 떳을값을 대비해 try-except문 사용
        return x // y # 에러가 없을시 원래대로 출력
    except ZeroDivisionError: # 나누는 값이 0인 경우
        return "0으로 나눌 수 없습니다" # 알맞은 안내문과 함께 에러 안내


a = int(input("첫 번째 정수 입력 : "))
b = int(input("두 번째 정수 입력 : "))

print("나눈 결과 값 :",divide(a,b))