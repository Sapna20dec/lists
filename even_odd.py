a = [20, 18, 17, 5, 7, 8, 9, 99, 66, 6]
i = 0
b = []
c = []
while i < len(a):
	if a[i] % 2 == 0:
		b.append(a[i])
	else:
		c.append(a[i])
	i = i+1
print("even", b, 'sum of even numbers is:', sum(b))
print("odd", c, 'sum of odd numbers is ', sum(c))

