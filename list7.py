p=[[1,2,3,],[6,7,8],[4,5,6]]
i=0
while i<(len(p)):
    sum=0
    j=0
    while j<len(p[i]):
        a=p[j][i]
        sum=sum+a
        j=j+1
    print(sum,end=" ")
    i=i+1



