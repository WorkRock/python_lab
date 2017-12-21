"""
주제: 리스트(list)
작성일: 17. 09. 13
작성자: 201632023 이지훈
"""
# l에 [2, 4, 6, 8, 10]을 저장한 후 출력한다.
l = [2, 4, 6, 8, 10]
print(l)
# 0번째 요소값 출력한다
print(l[0])
# 3번째 요소값을 -8로 변경한다.
l[3] = -8
print(l[3])
# l에 12를 뒤에 붙여 추가한 후, l을 출력한다
l.append(12)
print(l)
# l의 1의 위치에 -3을 삽입한 후, l을 출력한다.
l.insert(1,-3)
print(l)
# append(return X)는 뒤에 삽입, insert(반환값은 없다)는 원하는 위치에 삽입 가능.
# l의 1번째 요소를 삭제한 후, l을 출력한다.
#del.l[1]
print(l)
# l에 있는 -8값을 제거한 후, l을 출력한다.
l.remove(-8)
print(l)
# remove = 값을 지움(반환값은 없다). del = 위치의 값을 지움.
# l을 정렬하여 출력한다.
l.sort()
print(l)
# l을 역순으로 출력한다.
l.reverse()
print(l)
# sort = 정렬(반환값은 없다), reverse = 말그대로 역순.
# l에서 4 값의 위치를 출력한다
print(l[4])
# l의 길이를 출력한다.
print(len(l))
# l에 [1, 2, [3, 'John', 4], 'Hi']를 저장한다.
l = [1, 2, [3, 'John', 4], 'Hi']
# l의 3번째 요소를 출력
print(l[3])
# l의 2번째 요소를 출력
print(l[2])
# l의 2번째 요소의 1번째 요소 출력
print(l[2][1])
# l의 2번째 요소의 1번째 요소의 앞의 세글자만 출력
print(l[2][1][:3])
print(l)
print(l.extend([4, 1, 3, 6 ,4]))
print(l)
print(l.pop(1))
print(l)
print(l.pop())
print(l)