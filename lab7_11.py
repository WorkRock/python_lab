"""lab7_11
주제 :
A. 수작업으로 과제제출 시스템에서 예제 사진 파일을 프로그램이 작동할 디렉토리에 저장한다.
B. 사용자로부터 복사할 디렉토리를 입력받아, 예제 사진 파일을 사용자가 입력한 디렉토리에 복사하는 프로그램을 작성하여 실행한다.
C. 수작업으로 사용자가 입력한 디렉토리에 사진 파일에 복사되었는지 확인한다.
작성일 : 17. 12. 06.
작성자 : 201632023 이지훈
"""
import os
k_image = open("C:\\Users\\user\\Desktop\\python\\DSC_0104.JPG","rb")
while(1):
    try:
        s = input("복사를 원하시는 디렉토리를 입력하세요 : ")
        a = os.path.join(s, "DSC_0104.JPG")
        k_image_2 = open(a, "wb")
        k_image_2.write(k_image.read())
        print("\'"+s+"\'"+ "위치에 파일이 복사되었습니다.")
        break
    except FileNotFoundError:  # 예외 FileNotFoundError가 발생하면 적절한 안내문과 함께 에러 안내.
        print("입력한 디렉토리가 존재하지 않습니다.")
k_image.close()
k_image_2.close()