try:
    f = open("score.txt", "r")  # 데이터 파일을 읽어 들인다.
    line = f.readlines() #각각의 줄을 요소로 갖는 리스트 line을 만든다.
    all = 0 #각 학생 평균의 합을 구할 변수 all
    count = 0 #학생이 몇명인지 셀 변수 count
    allk = 0 #모든 국어 점수의 합 변수 allk
    alle = 0 #모든 영어 점수의 합 변수 alle
    allm = 0 #모든 수학 점수의 합 변수 allm
    print("==== 전체 평균 ====")
    for i in line:
        count += 1 #학생이 몇명인지 센다
        list = i.split(":") #':'을 기준으로 나눈다
        korean = list[1] #리스트의 1번째 요소는 국어점수
        k = int(korean.strip()) #요소의 공백을 지운다,int형으로 변환
        allk += k #모든 국어 점수의 합
        english = list[2] #리스트의 2번쨰 요소는 영어점수
        e = int(english.strip()) #요소의 공백을 지운다,int형으로 변환
        alle += e #모든 영어 점수의 합
        math = list[3] #리스트의 3번째 요소는 수학점수
        m = int(math.strip()) #요소의 공백을 지운다,int형으로 변환
        allm += m  #모든 수학 점수의 합
        average = (k + e + m) / 3 #각 학생의 평균
        all += average #각 학생 평균의 합
    print("%.1f" % (all / count)) #전체 평균=각 학생 평균의 합/학생수

    print("==== 각 학생 평균 ====")
    for i in line:
        list = i.split(":")  # ':'을 기준으로 나눈다
        name = list[0]  # 리스트의 0번째 요소는 이름
        korean = list[1]  # 리스트의 1번째 요소는 국어점수
        k = int(korean.strip())  # 요소의 공백을 지운다,int형으로 변환
        english = list[2]  # 리스트의 2번쨰 요소는 영어점수
        e = int(english.strip())  # 요소의 공백을 지운다,int형으로 변환
        math = list[3]  # 리스트의 3번째 요소는 수학점수
        m = int(math.strip())  # 요소의 공백을 지운다,int형으로 변환
        average = (k + e + m) / 3  # 각 학생의 평균
        print(name, "%.1f" % average) #이름, 평균 출력

    print("==== 각 과목 평균 ====")
    print("국어 평균:%.1f" % (allk / count)) #국어 평균=모든 국어 점수의 합/학생수
    print("영어 평균:%.1f" % (alle / count)) #영어 평균=모든 영어 점수의 합/학생수
    print("수학 평균:%.1f" % (allm / count)) #수학 평균=모든 수학 점수의 합/학생수

except FileNotFoundError: #파일이 존재하지 않으면
    print("파일이 존재하지 않습니다.") #"파일이 존재하지 않습니다."출력
