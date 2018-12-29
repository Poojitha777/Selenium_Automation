#WAP to count the number of lowercase character in the string

FirstString="HaRry PottER And THE sorCERerS StoNE"
count=0
for i in FirstString:
    if (i.islower()):
        count=count+1
print(count)