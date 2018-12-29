filename = input("Enter file name: ")
with open(filename, 'r') as NewFile:
    for line in NewFile:
        words = line.split()
        for i in words:
            for z in i:
                if (z.isdigit()):
                    print(z)