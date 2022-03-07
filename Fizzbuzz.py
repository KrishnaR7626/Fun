# Simple Fizzbuzz
n = int(input("enter how many number "))

i=1
while i<=n:
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%5==0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)
    i+=1
