#filename=open("TextFile.txt","r")
z = 'the'
filename = input("Enter file name: ")
with open(filename) as myFile:
    for number, line in enumerate(myFile, 1):
        if z in line:
            print("found at line:",number)
