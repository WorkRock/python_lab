"""
주제 : data type
작성일 : 17. 09. 04
작성자 : 201632023 이지훈
"""
# float형 변수 f에 3.4 저장, 출력
f = 3.4
print("f :",f)

# int형 변수 i에 1을 저장, 출력
i = 1
print("i :",i)

# bool형 변수 b에 true를 저장, 출력
b = True
print("b :",b)

# String형 변수 s에 '1' 을 저장, 출력
s = "1"
print("s :",s)

# f와 i를 더해서 출력
print("i + f :",i+f)

# s와 i를 더해서 출력
# print("s + i : ",s+i) <- error. type전환이 되지 않음.(Can't convert 'int' object to str implicitly)

# s를 int형으로 변환하여 i와 더하여 출력
print("s + i (s변환):",int(s)+i)
# s = int(s)를 이용해도 된다. 다만 이러면 s자체가 int형으로 변환된다.

# i를 str형으로 변환하여 s와 더하여 출력
print("s + i (i변환):",s+str(i))

# 복소수 k를 정의하여 5+7i 저장, 출력 (허수 부분은 j로 표현한다)
k = 5 + 7j
print("k :",k)
print("k 의 실수부분 :",k.real)
print("k 의 허수부분 :",k.imag)
print("켤레복소수 :",k.conjugate())

# j에 28을 입력
j = 28
# i를 j로 나눈 값을 출력
print("i / j :",i/j)
i = 59
print("i / j (정수 나눗셈):",i//j) # <- 정수 나눗셈은 '//' 사용
print("i / j 나머지:",i%j)

# j의 제곱 출력
print("j의 2제곱 :",j**2)
print("j의 3제곱 :",j**3)

# j에 -29 저장 후, j의 절대값 출력
j = -29
print("j의 절대값 :",abs(j))

# b or False 출력 (참고로 b는 True로 저장했었다. 위를 보자)
print("b or false :",b or False)

# b and False 출력 (참고로 b는 True로 저장했었다. 위를 보자)
print("b and false :",b and False)

# o에 8진수 16대입, 변수 그대로 출력
o = 0o16
print("o (10진수 출력):",o)
print("o (8진수 출력): %o"%(o))

"""
x에 16진수 A5대입, 변수 그대로 출력
16진수로 출력, 10진수로 출력, 8진수로 출력
"""
x = 0xA5
print("x (그대로 출력):",x)
print("x (16진수로 출력): %x"%(x))
print("x (10진수로 출력):%d"%(x))
print("x (8진수로 출력): %o"%(x))