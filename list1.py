list = [[6, 7, 8], [1, 2, 3], [4, 5, 9]]
i = 0
z = []
while i < len(list):
	j = 0
	while j < len(list):
		z.append(list[i][j])
		j = j+1
	i = i+1
print(z)

