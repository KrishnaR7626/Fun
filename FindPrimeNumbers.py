# An inefficient way I could think of to find prime numbers.
i = int(input("enter max "))
t=1
while t<i:
    m=1
    c=0
    while m<i:
        if t%m==0:
            c+=1
        m+=1
    if c<=2:
        print(t)
    t+=1
