list1=['rani','sonam','piyali','ronu']
list2=['ram','shyam','ramu','ronu']
b=[]
i=0
while i<len(list2[i]):
    if list1 not in list2:
        b.append(list1[i])
        print(b)
    i=i+1

