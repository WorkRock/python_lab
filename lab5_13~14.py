"""lab5_13
주제 :
1. student 클래스를 정의한다. 다음 학생에게 줄, 학번을 클래스 변수 tag로 정의한다.
2. __init__() 함수를 정의한다. 이름, 학년을 매개변수로 받는다.
3. s1의 학번에 student.tag 값을 학번으로 부여한다. student.tag 값을 하나 늘린다.
4. s1의 이름에 자신의 이름을 저장한다.
5. s1의 학년에 자신의 학년을 저장한다.
6. s2출력
7. student 클래스에 학년을 올리는 upgrade()라는 메소드를 정의한다. self를 매개변수로 받는다.
몇 학년을 올릴지를 매개변수로 받는다. 1년 올리는 것이 디폴트이다.
4학년이 초과하는 경우, 오류 메세지 출력
작성일 : 17. 11. 08.
작성자 : 201632023 이지훈
"""

class student:
    tag = 201632023 # 클래스 변수

    def __init__(self,n,g):
        """
        학생을 정의및 초기화 해주는 메소드
        """
        self.name = n
        self.grade = g
        self.code = student.tag
        student.tag +=1

    def print(self):
        """
        print메소드
        :return: 출력문
        """
        return #"학번 : " + str(self.code) + ", 이름 : " + self.name + ", 학년 : " + str(self.grade)

    def __str__(self):
        """
        __str__메소드
        :return: 출력문
        """
        return "학번 : " + str(self.code) + ", 이름 : " + self.name + ", 학년 : " + str(self.grade)

    def upgrade(self, a=1): # default 매개변수
        """
        학년을 올리는 메소드
        :param a: 올려줄 학년
        :return: 학년 값
                  에러문구
        """
        if(self.grade+a <= 4 and self.grade+a >= 1):
            self.grade += a
            return self.grade
        else:
            return print("4학년을 넘어갑니다.")

s1 = student("이지훈",2)
s2 = student("포친키",1)
print(s1)
print(s2)

s1.upgrade()
print(s1)

"""lab5_14
주제 :
1. person 클래스를 정의한다. 이름과 나이를 data attribute로 가지고 있다
2. 이름과 나이를 매개변수로 받는 생성자가 있다.
3. 나이를 1살 더하는 getOlder 메소드가 있다.
4. 문자열 반환, 프린트 메소드
5. 사람을 계승하는 학생 클래스 정의. 학년, 학번을 data attribete로 가지고 있다
6. 이름 나이 학년 학번을 받는 생성자가 있다. 생성자 내에서 사람의 생성자를 호출한다.
7. 학년을 진급하는 upgrade() 메소드가 있다.
7. 문자열 반환 메소드
작성일 : 17. 11. 08.
작성자 : 201632023 이지훈
"""

class person():
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def getOlder(self, a = 1):
        self.age += a

    def print(self):
        return "이름 : " + self.name + ", 나이 : " + str(self.age)

    def __str__(self):
        return "이름 : " + self.name + ", 나이 : " + str(self.age)


    def __eq__(self, other):
        if(self.name == other.name):
            return True
        else:
            return False


class student(person):
    def __init__(self, n, a, g, c):
        person.__init__(self, n, a)
        self.name = n
        self.age = a
        self.grade = g
        self.code = c

    def upgrade(self, a=1): # default 매개변수
        """
        학년을 올리는 메소드
        :param a: 올려줄 학년
        :return: 학년 값
                  에러문구
        """
        if(self.grade+a <= 4 and self.grade+a >= 1):
            self.grade += a
            return self.grade
        else:
            return print("4학년을 넘어갑니다.")

    def __str__(self):
        """
        __str__메소드
        :return: 출력문
        """
        return "학번 : " + str(self.code) + ", 이름 : " + self.name + ", 학년 : " + str(self.grade) + ", 나이 : " + str(self.age)

p1 = person("어머니",45)
p2 = person("어머니",46)
p3 = person("어머니Yee",46)

print(p1)
print(p2)
print(p3)
print(p1 == p2) # 메소드를 안묶으면 True가 나온다. 재정의 했기 때문
print(p1 == p3)

s1 = student("3뚝3갑",33,3,333)
print(s1)