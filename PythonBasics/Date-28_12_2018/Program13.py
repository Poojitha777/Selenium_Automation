for number in range(1,1000+1):
   if number > 1:
       #Divide every number by 2,3,5 if divisible then it is prime number
       for i in range(2,6):
           if (number % i) == 0:
               break
       else:
           print(number,"is a prime number!")

