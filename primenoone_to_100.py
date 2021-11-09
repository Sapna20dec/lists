i=1
a=[]
while i<=100:
    j=2
    sum=0
    while j<=i//2:
        if i%j==0:
            sum=sum+1
            break
        j=j+1
    if sum==0 and i!=1:
        a.append(i)
    i=i+1
print(a)