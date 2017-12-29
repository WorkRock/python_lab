"""lab4_13
주제:
1. 사용자로부터 단어를 입력받는다.
2. 입력받은 단어를 출력한다.
3. 해당 단어에 포함된 알파벳을 알파벳 순서로 출력한다.
4. 해당 단어의 길이를 출력한다.
작성일: 17. 10. 01.
작성자: 201632023 이지훈
"""
"""
a = input("단어 입력 : ")
print("입력 하신 단어 : ",a)
l = []
size = len(a)
for i in range(0,size):
    l.append(a[i])

l.sort()
b = ""
for i in range(0,size):
    b += l[i]
print('정렬 : ',b)
print('길이 : ',size)
"""

s = input("input : ")
count = 0
for i in range(0,len(s)):
    a = s[i:i+3]
    if(a == 'bob'):
        count += 1
print(count)