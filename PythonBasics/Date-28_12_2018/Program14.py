filename=open("TextFile.txt","r")
a = filename.read()
for line in reversed(list(open("TextFile.txt"))):
    print(line.rstrip())