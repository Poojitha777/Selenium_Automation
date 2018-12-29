filename = input("Enter file name: ")
lines = 0
with open(filename, 'r') as f:
    for line in f:
        lines = lines + 1
print("The total number of lines present in the file:",lines)
