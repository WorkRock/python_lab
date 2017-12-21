"""
주제: 함수
작성일: 17. 10. 11.
작성자: 201632023 이지훈
"""

def sum(a,b):
    return a + b
s = sum(2,4)
print(s)

"""
주제: 두 개의 정수를 매개변수로 받아서 두 수의 차를 반환하는 subtract를 정의하여
4, 8을 매개변수로 함수를 호출한 후 출력하라.
작성일: 17. 10. 11.
작성자: 201632023 이지훈
"""

def subtract(a,b):
    return a- b

s = subtract(4,8)
print(s)

"""
주제: 두 개의 문자열을 매개변수로 받아서, ' , ' 로 연결하여
출력하는 print_string함수를 정의한다
일요일,월요일, 화요일의 리스트를 매개변수로 print_string을 호출하여 출력하라
작성일: 17. 10. 11.
작성자: 201632023 이지훈
"""

def print_string(l):
    length = len(l)
    """ 예시 정답
    length = len(l)
    s = ""
    i = 0
    for w in l:
        s += w
        i += 1
        if(i != length):
            s +=', '
    print(s)
    """
    for i in range(length):
        if(i != length- 1):
            print(l[i], end = ", ")
            continue
        print(l[i], end="")

print_string(['일요일','월요일','화요일'])

"""
def print_string(*l):
    length = len(l)
    s = ""
    i = 0
    for w in l:
        s += w
        i += 1
        if(i != length):
            s +=', '
    print(s)

print_string('일요일','월요일','화요일')
"""