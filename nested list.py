a = [1, 2, 3, [4, 5]]
i = 0
while i < len(a):
	if i <= 2:
		print(a[i])
	else:
		print(a[i][0])
		print(a[i][1])
	i += 1


