import os
a = int(input("정수 입력 : "))

if(a%3 == 0 and a%4 == 0):
    print("3과 4의 공배수")
elif(a%3 == 0):
    print("3의 배수")
elif(a%4 == 0):
    print("4의 배수")
else:
    print("3의 배수도, 4의 배수도 아닙니다")


b = "c:\\temp\\201632023\\room1\\room2"
print(b)
a = b.count("\\")
l = b.split("\\",a)
del(l[a])
b = ""
for s in l:
    if(s == "c:"):
        b += s
    else:
        b += "\\"+s

print(b)
print(os.listdir("c:\\temp\\201632023\\"))
if(len(os.listdir("c:\\temp\\201632023\\room1\\room2")) == 0):
    print("없어!")
else:
    print("있어!")