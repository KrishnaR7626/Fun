# Proof of a mathematical numbers trick I found, was not sure so I wrote a program to confirm its validity and it was true.
arr=[]
t=10
p=10
while t<100:

    p = 10
    while p<100:

        a=t*p
        i = [int(r) for r in str(p)]
        j = [int(n) for n in str(t)]
        b=i[1]
        c=j[0]
        d=i[0]
        e=j[1]
        x=b*c*10
        y=d*c*100
        z=b*e
        u=d*e*10
        o=x+y+z+u

        if a!=o:
            print("found it " +str(t) +"   "+str(p))
        else:
            q="a"
            arr.append(q)
        p+=1
    t+=1
print(len(arr))
