"""def asd():
    return "가나다라마바사하자차카타파하",123,155,214,212
a = int(input("숫자 입력 : "))
b = int(input("숫자 입력 : "))

print("두 수의 합 :",a+b)
print("두 수의 차 : %d"%(a-b))
total = a*b
print("두 수의 곱 : ",total)
print("두 수의 나눗셈 : %d"%(a//b))
"""
str = "김일수:    35: 80: 90\n"
a = str.split(": ")
s=[]
for o in a:
    s.append(o.strip())
name = s[0]
kor = s[1]
eng = s[2]
math = s[3]
aver = (s[1] + s[2] + s[3])

print(s)
