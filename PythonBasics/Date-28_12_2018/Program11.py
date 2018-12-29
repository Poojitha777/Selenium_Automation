f=open("TextFile.txt","r")
a = f.read()
l = a.split(" ")
print(l)
z = {i:l.count(i) for i in l}
print(z)