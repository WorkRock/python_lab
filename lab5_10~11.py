"""
주제 : 좌표 클래스 정의
작성일 : 17. 10. 30.
작성자 : 201632023 이지훈
"""

class Coordinate:
    """
    좌표를 표현하는 클래스 정의
    """
    def __init__(self, a, b):
        """
        좌표를 초기화
        :param a: x좌표의 값
        :param b: y좌표의 값
        """
        self.x = a
        self.y = b

    def prnt(self):
        """
        출력하는 메소드
        :return: 없음
        """
        print("좌표<"+str(self.x)+", "+str(self.y)+">")

    def distance(self,other):
        """
        좌표의 거리값을 계산해 주는 메소드
        :param other: 다른 점의 좌표
        :return: self와 다른 점의 거리
        """
        distance = (self.x-other.x)**2 + (self.y - other.y)**2
        return distance**0.5

    def __str__(self):
        """

        :return: 문자열
        """
        return "좌표<"+str(self.x)+", "+str(self.y)+">"


c1 = Coordinate(2,3)
c2 = Coordinate(3,1)

print(c1)
print(c2)

print("두 좌표의 거리 값 : %.2f"%c1.distance(c2))
print("두 좌표의 거리 값 : %.2f"%c2.distance(c1))

#print("두 좌표의 거리 값 : %.2f"%coordinate.distance(c1,c2))
"""
주제 : 분수
작성일 : 17. 11. 01.
작성자 : 201632023 이지훈
"""

class fraction:
    def __init__(self,numer,denom):
        """
        분수 초기화
        :param numer: 분모
        :param denom: 분자
        """
        self.numer = numer
        self.denom = denom

    def prnt(self):
        """
        출력하는 메소드
        :return: 없음
        """

    def __str__(self):
        """
        :return: 문자열
        """
        return "출력 : "+str(self.denom)+"/"+str(self.numer)

    def __add__(self,other):
        """
        두 분수의 분자를 더해주는 메소드
        :param other: 더할 분수
        :return: 두 분자의 합
        """
        a = self.numer * other.denom
        b = self.denom * other.numer
        c = self.numer * other.numer
        s = fraction(c,a+b)
        return s

    def __sub__(self, other):
        """
        두 분수의 분자를 더해주는 메소드
        :param other: 더할 분수
        :return: 두 분자의 합
        """
        a = self.numer * other.denom
        b = self.denom * other.numer
        c = self.numer * other.numer
        s = fraction(c, a - b)
        return s

c1 = fraction(4,3)
c2 = fraction(7,2)

#print(c1.add(c2))
#print(c1.minus(c2))
print(c1+c2)
print(c1 - c2)