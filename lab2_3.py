"""
주제 : 문자열 함수
작성일 : 17. 09. 06.
추가 작성일 : 17. 09. 11.
작성자 : 201632023 이지훈
"""

# 문자열 s에 "Test your Python debugging skills!" 를 저장한다.
s = "   Test your Python debugging skills!   "

# 문자열을 모두 소문자로 출력
print("소문자 출력 :",s.lower())

# 문자열을 모두 대문자로 출력
print("대문자 출력 :",s.upper())

# 문자열에 포함된 t의 개수 출력
print("문자열에 포함된 t의 개수 출력 :",s.count("t"))

# 문자열에 포함된 T의 개수 출력
print("문자열에 포함된 T의 개수 출력 :",s.count("T"))
# print("문자열에 포함된 T의 개수 출력 :",s.upper().count("T")) <- 이런것도 된다.

"""
사용자에서 찾을 문자를 입력 받아서,
대소문자 구분 없이 해당 문자의 개수 출력
"""

a = input("어떤 문자를 찾으십니까? : ")
print("%c는 %d개 있습니다."%(a,s.lower().count(a.lower())))

# 17. 09. 11 수업

# t가 있는 위치 출력
print("t가 처음으로 있는 위치 : %d"%s.index("t"))

# x가 있는 위치 출력
print("x가 처음으로 있는 위치 : %d"%s.find("x"))

# s 앞에 빈칸 3개, 뒤에 빈칸 3개 추가해서 출력
print(s)

# s 의 왼쪽 공백 제거 후 출력
print(s.lstrip())

# s 의 오른쪽 공백 제거 후 출력
print(s.rstrip())

# s 의 양쪽 공백 제거 후 출력
print(s.strip())

# s 를 다시 출력해서 s에 영향 있는지 확인
print(s)

# s 의 양쪽 공백 제거 후 s에 저장한 후 출력(strip)
s = s.strip()
print(s)

# 문장에서 Python을 Java로 바꾸어 출력
print("문장 바꾸어 출력 : %s"%s.replace("Python","Java"))

# 문장에서 e를 i로 모두 바꾸어 출력
print("문장 바꾸어 출력 : %s"%s.replace("e","i"))

# 문장에서 e를 i로 한 번만 바꾸어 출력
print("문장 한 번만 바꾸어 출력 : %s"%s.replace("e","i",1))

# 빈 칸을 기준으로 문자열을 전부 나누기
print("문자열 나누기 : %s"%s.split(" "))

# 빈 칸을 기준으로 문자열을 3개만 떼어내기
print("문자열을 3개만 떼어내기 : %s"%s.split(" ",3))

# 문자열 길이 출력
print("문자열의 길이 : %d"%len(s))