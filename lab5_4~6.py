"""
주제: 이름, 학번, 학과를 매개변수로 받아서 이를 출력하는 함수 print_me 함수를 정의한다.
이때, 학과가 매개변수로 넘어오지 않으면 "소프트웨어공학과"를 디폴트 값으로 한다.
작성자: 201632023 이지훈
작성일: 17. 10. 16.
"""

def print_me(name,code,major = "소프트웨어공학과\n"):
    """
    매개변수를 받아 출력한다
    :param name: 이름
    :param code: 학번
    :param major: 학과
    :return: 없음
    """
    print("이름",name)
    print("학번",code)
    print("학과",major)

print_me("이지훈","201632023","소프\n")
print_me("이지훈","201632023")

"""
주제: type 함수 사용
작성자: 201632023 이지훈
작성일: 17. 10. 16.
"""

def value_type(s):
    print("값은 "+str(s)+", 타입은 "+str(type(s)))


a = 5
b = "이지훈"
c = 3.14
d = True

print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))

value_type(a)
value_type(b)
value_type(c)
value_type(d)

if(type(a) == int):
    value_type(a)

"""
주제:
1. 리스트로 넘어오는 숫자들 중에서 가장 작은 값을 반환하는 min 함수 정의
2. 리스트로 넘어오는 숫자들 중에서 가장 큰 값을 반환하는 max 함수를 정의
3. l 변수에 [4,7,9,11,-5]를 저장한 후, 함수를 호출하여 최소, 최대값을 출력
작성자: 201632023 이지훈
작성일: 17. 10. 16.
"""

def min(l):
    """
    최솟값을 리턴해주는 함수
    :param l: 숫자들의 리스트
    :return: 최솟값
    """
    s = l[0]
    for i in l:
        if(s>=i):
            s = i

    return s

def max(l):
    """
    최댓값을 리턴해주는 함수
    :param l: 숫자들의 리스트
    :return: 최댓값
    """
    s = l[0]
    for i in l:
        if(s<=i):
            s = i

    return s



l = [4,7,9,11,-5]
print("최솟값 : "+str(min(l)))
print("최댓값 : " + str(max(l)))