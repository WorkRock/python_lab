"""
주제 :
01. intSet 클래스는 정수들의 집합이다. 정수들을 관리하는 리스트 selfvals를 애트리뷰트로 가진다
02. 새로운 정수 e를 추가하는 insert 메소드 이미 있다면 추가하지 않음.
03. e가 정수집합에 포함되어 있는지 확인하는 member메소드인 involve(True, False 반환)
04. e를 제거하는 remove메소드. 단, e가 해당 집합에 없다면 '적당한 오류 메세지 출력'
05. 집합 형식의 문자열로 변환시켜주는 __str__메소드. 단, 정수들은 정렬되어 반환되어야 한다.
06. intSet을 저장하는 변수 s를 정의
07. s에 5, 3, 7을 삽입
08. s를 정렬하여 출력
09. s에 8이 있는지 결과 출력
10. s에 3이 있는지 결과 출력
11. s에서 3 제거
12. s에서 4 제거
13. s를 정렬하여 출력
작성일 : 17. 11. 06.
작성자 : 201632023 이지훈
"""


class intSet:
    def __init__(self,*e):
        self.vals = list(e)

    def insert(self, e):
        if (self.involve(e) == True):
            return print("이미 존재하는 정수 입니다.")
        self.vals.append(e)
        return print("삽입 완료 : " + str(e))

    def involve(self, e):
        if(e in self.vals):
            return True

        return False

    def remove(self, e):
        if (self.involve(e) == True):
            self.vals.remove(e)
            return "삭제 완료"
        else:
            return "삭제하려는 정수가 존재하지 않습니다. : " + str(e)

    def __str__(self):
        self.vals.sort()
        return "현재 만들어진 집합 : " + str(self.vals)

s = intSet(5,3,7)
s.insert(6)
s.insert(3)
s.insert(7)
print(s)
print(s.involve(8))
print(s.involve(3))
print(s.remove(3))
print(s.remove(4))
print(s)