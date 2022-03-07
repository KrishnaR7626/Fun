# An implementation of Euler's Method for calculating values at an exact point in time, very exhaustive manually to calculate large number of steps.
import math

def xprime (x):
    xp = ((2-x)*(math.sqrt(1-x)))/2
    return xp

x1arr=[]
i=0
n=int(input("Enter n (the number of steps) "))
a=1/n
x=0
while i < n+1:
    x1arr.append(round(x,2))
    x+=a
    i+=1
h1=a
y1arr=[0]

i=0
while i<len(x1arr)-1:
    y=y1arr[i]+h1*xprime(x1arr[i])
    y1arr.append(y)
    i+=1

print("According to Euler's method and using the step size of " + str(a) + " the value of x(1) or t=1 is "+str(y1arr[len(y1arr)-1]))
