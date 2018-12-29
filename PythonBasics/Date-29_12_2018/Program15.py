#WAP to count the number of vowels present in a string using set

MyName="Poojitha Lakshminarayana"
x=set("aeiouAEIOU")
count=0
for i in MyName:
    if i in x:
        count=count+1
print("The number of vowels present: ",count)