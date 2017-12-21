name = input("이름 : ")
age = int(input("숫자에 불과한 것 : "))
height = float(input("수치에 불과한 것 : "))
print("\n나의 이름은", name, "입니다")
print("나이는", age,"입니다")
print("키는", height,"입니다\n")

print("나의 이름은 %s입니다"%name)
print("나이는 %d입니다"%age)
print("키는 %.1f입니다\n"%height)

print("저는 %s 이고 현재 %d살 이며, 키는 %.1f입니다.\n"%(name,age,height))

message1 = "저는 %s 이고 현재 %d살 이며, 키는 %.1f입니다.\n" %(name,age,height)
message2 = "저는 %s 이고 현재 %d살 이며, 키는 %.1f입니다.\n"
print(message1)
print(message2%(name,age,height))

print("저는 {} 이고 현재 {}살 이며, 키는 {}입니다.\n".format(name,age,height))