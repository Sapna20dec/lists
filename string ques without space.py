# a = [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
# i = 0
# s = ""
# while i < len(a):
#     j = 0
#     b = ""
#     while j < len(a[i]):
#         b = a[i][j]
#         s = s+b
#         j += 1
#     i += 1
# print(s)


list = [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
i = 0
while i < len(list):
	j = 0
	while j < len(list[i]):
		print(list[i][j], end=' ')
		j = j+1
	i += 1

