list=[1,2,3,4,5,6,7,8,9,0]
i = 0
z = []
while i < len(list):
	j = 0
	x = []
	while j < 3:
		d = i+j
		x.append(d)
		j += 1
	z.append(x)
	i += 3
print(z)
