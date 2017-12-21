"""lab7_4
주제 : encoding 사용 없이 웹페이지 가져오기
작성일 : 17. 11. 29.
작성자 : 201632023 이지훈
"""

def input_query():
    q = str(input("검색어를 입력하세요 : "))
    return "&query = " + q

print(input_query())

"""lab7_5
주제 : encoding을 사용하여 웹페이지 가져오기
작성일 : 17. 11. 29.
작성자 : 201632023 이지훈
"""

import urllib.parse

def input_query():
    q = urllib.parse.quote_plus(input("검색어를 입력하세요 : "))
    return "&query = " + q

print(input_query())