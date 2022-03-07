# A factorial function and the implementation for the mathematical operation choose along with its application in a statistical formula.
def factorial(number):
     total = 1
     for x in range(1,number+1):
         total*=x
     return total
 sum = 0
 for i in range(0,4):
     sum+=(factorial(5)/(factorial(i)*factorial(5-i)))*((0.1**i)*((1-0.1)**(5-i)))
 print(1-sum)

