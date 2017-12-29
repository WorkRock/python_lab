"""Beauty_Soup
주제 :
책의 p. 275~282를 참고하여, 자신의 컴퓨터에 Beauiful Soup 4.3을 설치하여, p.282의 프로그램이 작동한 결과 화면을 capture하여 과제제출 양식(표지)에 따라 제출하라. (표지+캡쳐화면)
PyCharm에서 작동한다면, p.282의 마지막 명령문은 print(bs.find("title")로 명시해야 한다.
  문자열.split, 문자열.strip(앞뒤 필요 없는 문자 제거. 매개변수가 없으면 white space 제거)
작성일 : 17. 11. 29.
작성자 : 201632023 이지훈
"""

html = """
<html>
    <head>
        <title> test web </title>
    </head>
    <body>
        <p align = "center"> text contents </p>
        <img src = "c:\Python34\Koala.jpg" width = "500" height = "300">
    </body>
</html>
"""
from bs4 import BeautifulSoup
bs = BeautifulSoup(html)
print(bs.prettify())
bs.find("title")