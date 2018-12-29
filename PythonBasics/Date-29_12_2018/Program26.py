# 1) WAP to convert the 1st 2 words of the input into uppercase

FirstString="Bangalore is the silicon city"
v=FirstString.split()
count=0
for i in v:
    print(i.upper())
    count+=1
    if count>1:
        break