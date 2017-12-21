"""
주제: 딕셔너리(Dictionary), set
작성일: 17. 09. 18.
작성자: 201632023 이지훈
"""

# fruits = {'a':'사과', 'b':'배','c':'복숭아','d':'딸기'} 를 정의한 후 출력
fruits = {'a':'사과', 'b':'배','c':'복숭아','d':'딸기'}
print(fruits)

# 키가 'a'인 경우의 값을 출력하라.
print(fruits['a'])

# 키가 'b'인 경우의 값을 '체리'로 수정하라.
fruits['b'] = '체리'
print(fruits)
"""
b = 'b'
fruits[b] = '체리'
print(fruits) <- 이렇게도 된다.
"""

# fruits에서 키가 'a'인 경우의 값의 길이를 출력하라
print(len(fruits['a']))

# 모든 키를 출력하라.
print(fruits.keys())

# 모든 값들을 출력하라.
print(fruits.values())

# fruits안에 'a'라는 키가 있으면 True, 없으면 False를 출력하라.
print('a' in fruits)

# fruits 의 values 중에 '복숭아' 가 있으면 True, 없으면 False를 출력하라.
print('복숭아' in fruits.values())

# 'c'라는 키를 가지는 fruit를 삭제하라.
del fruits['c']
print(fruits)
#----------------------------------------------#

# set
s = {7, 8, 9}
print(s)

# fruits를 set으로 형변환하여 출력하라
print(set(fruits))

# [3, 4, 5] (<-list)를 set으로 형변환하여 s에 저장하고 이를 출력하라.
print(set([3, 4, 5]))
print(list(s)) #<- 반대도 가능하다.

# s에서 8을 지우고 (remove) s를 출력하라
s.remove(8)
print(s)