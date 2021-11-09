list = [6, 1, 3, 5, 6, 3, 1]
z = []
i = 0
while i < (len(list)):
	if i in list:
		if i not in z:
			z.append(i)
	i = i+1
print(z, "product", z[0]*z[1]*z[2]*z[3])

