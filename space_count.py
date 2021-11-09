l = "i am sapna"
i = 0
a = []
count = 0
while i < len(l):
	if l[i] == " ":
		r = ('space'+str(count))
		count += 1
		a.append(r)
	else:
		a.append(l[i])
	i = i+1
print(a)


# a = 'sapna nyol'
# i = 0
# b = []
# while i < len(a):
# 	if a[i] in 'P':
# 		b.append(p)
# 	else:
# 		b.append(a[i])
# 	i = i+1
# print(b)


    
