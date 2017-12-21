"""
주제 :
작성자 : 201632023 이지훈
작성일 : 17. 10. 23.
"""

def product(a,b):
    """
    더하기를 이용하여 곱하기 하는 함수
    :param a: 정수
    :param b: 정수
    :return: a+b의 값을 반환
    """
    if(b==1):
        return a
    return a+product(a,b-1)

print(product(5,4))
print(product(7,5))
print(product(10,7))

"""
주제 : factorial을 계산하는 함수 정의(recursion 이용)
작성일 : 17. 10. 23.
작성자 : 201632023 이지훈
"""

def product(a):
    """
    팩토리얼을 구하는 함수
    :param a: 팩토리얼을 구하는 정수
    :return: a+b의 값을 반환
    """
    if(a==1):
        return a
    return a*product(a-1)

c = int(input("팩토리얼 할 정수 입력 : "))
print("팩토리얼 결과 : ",product(c))

"""
주제 : 매개변수로 넘어오는 x번째 피보나치 수를 반환하는 fibo를 정의하라(0번째부터 시작한다고 가정한다)
작성일 : 17. 10. 23.
작성자 : 201632023 이지훈
"""

"""
1. 일반 함수로 정의한다.
2. Recursion을 이용하여 다시 정의한다.
3. 0번째부터 10번째까지의 피보나치 수를 출력한다.
"""

def fibo(a):
    s = 0
    n = 0
    for i in range(0,a):
        if(i == 0):
            n == i
        s += n + i



print(fibo(10))