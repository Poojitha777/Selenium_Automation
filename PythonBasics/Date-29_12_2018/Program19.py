#WAP which displaysthe letters that are not in both the strings

FirstString = "United"
SecondString = "Kingdom"
print("The letters which are not repeated in both lists are:", set(FirstString) ^ set(SecondString))