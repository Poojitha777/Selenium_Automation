# filename=open("TextFile.txt","r")
# a=filename.read()
filename = input("Enter file name: ")
with open(filename, 'r') as NewfileName:
    for line in NewfileName:
        l = line.title()
        print(l)






