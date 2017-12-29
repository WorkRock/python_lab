import re

r = re.compile("[ab]")
print(r.search("pizza"))
print(r.match("pizza"))


#1
result = re.findall("\d+","2017년 3월 8일 5000원")
print(result)
#2
result = re.split("[,]+","김치, 고추장, 된장")
print(result)
#3
result = re.sub("/","-","2017/05/06")
print(result)
#4
result = re.split("[<]+","<2015> <김일수> <성공회대학교>")
print(result) # 제일 앞의 <에 의해 ""이 결과에 포함되어 있다 <- 틀린예시
for i in result:
    if i == "": # 제일 앞의 ""은 건너 뛴다.
        continue
    r = re.search("[>]+",i) # '>'으로 끝나는 지점을 찾는다 []는 없어도 된다.
    print(r.end()-1)
    print(i[0:r.end()-1]) # '>' 앞까지 슬라이싱해서 출력