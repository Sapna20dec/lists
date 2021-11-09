list = [4, 5, 6, 7, 8, 9, 5.8, 4.9, "2"]
i = 0
b = []
sum = 0
while i < len(list):
	b.append(int(list[i]))
	sum = sum+b[i]
	i = i+1
print(sum, b)

