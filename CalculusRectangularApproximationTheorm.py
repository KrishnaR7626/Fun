# implements a theorem in calculus which uses rectangles to approximate area under a curve, as the number of rectangles increases calculations can get annoying, so this implementation was created.
n = input("enter number of rectangles ")
n = int(n)
deltax = (2-1)/n
x = 1
e = 2.718
y=1/x
func = e**y
summ = 0
i = 1
fac = 1/n
deltax = deltax/2

summ = summ + func
while i<n:
    x = x+fac
    summ = summ + 2*func
    i+=1
x=2
summ = summ + func
answer = (deltax*summ)
print(answer)
