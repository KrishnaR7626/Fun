# Implementation of the statistical concept of expected value, can be used to calculate expected values for large sample sizes.

def factorial(number):
    total = 1
    for x in range(1,number+1):
        total*=x
    return total
a = [0,1,2]
sum = 0
for x in a:
    temp = (factorial(5) / (factorial(x)*factorial(5-x)))*(0.2**x)*((1-0.2)**(5-x))
    sum+=temp
    print(temp)
print(sum)
