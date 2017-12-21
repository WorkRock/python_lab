import re
import os
import os.path

r = re.compile("a.f")
print(r.search("pizza"))
print(r.search("af"))
print(r.search("azaf"))
print("\n")

r = re.compile("ba?f")
print(r.search("bf"))
print(r.search("baf"))
print(r.search("basf"))
print("\n")

r = re.compile("ba*f")
print(r.search("bf"))
print(r.search("baf"))
print(r.search("baaf"))
print(r.search("basf"))
print("\n")

r = re.compile("ba+f")
print(r.search("bf"))
print(r.search("baf"))
print(r.search("baaf"))
print(r.search("basf"))
print("\n")

r = re.compile("^b")
print(r.search("bf"))
print(r.search("baf"))
print(r.search("baaf"))
print(r.search("basd"))
print("\n")

r = re.compile("f$")
print(r.search("bf"))
print(r.search("baf"))
print(r.search("baaf"))
print(r.search("basd"))
print("\n")

r = re.compile("[^bf]")
print(r.search("bf"))
print(r.search("baf"))
print(r.search("baaf"))
print(r.search("bsaf"))
print("\n")

r = re.compile("[b-f]")
print(r.search("bf"))
print(r.search("baf"))
print(r.search("baaf"))
print(r.search("ssss"))
print("\n")

print(re.search("\d+","가나다1은234를찾는다."))
print(re.match("\d+","가나다1은234를찾는다."))
print(re.match("\d+","2가나다1은234를찾는다."))
print(re.findall("\d+","가나다1은234를찾는다."))
print(re.split("\d+","가나다1은234를찾는다."))
print(re.sub("-","5","가나다1-은-234-를찾-는다."))
print("\n")

print(os.getcwd())
#print(os.listdir())
#for i in os.listdir():
#    print(i)
os.chdir("c:\\")
print(os.getcwd())
#os.mkdir("test")
#os.chdir("c:\\test")
#print(os.getcwd())
#os.chdir("c:\\")
#os.rmdir("c:\\test")
#os.makedirs("c:\\test\\test1\\test2")
#os.chdir("c:\\test")
#for i in os.listdir():
#    print(i)
#os.chdir("c:\\")
#os.removedirs("test\\test1\\test2")

print(os.path.isdir("test"))
print(os.path.isfile("test"))
print(os.path.exists("test"))
a = os.path.split("c:\\test")
print(a)
print(os.path.join(a[0],a[1]))
print(os.path.dirname("c:\\test"))
