def getDivList(n):
	d = 2
	div_list = [1]
	while n > 1:
		if n % d == 0 and d != 1:
			div_list.append(d)
			n = n // d
		else:
			d += 1
	return div_list

n = int(input('Write a number: '))

num_list = []
for i in range(1, n + 1):
	num_list.append(i)

for i in range(n - 1, 0, -1):
	div_list = getDivList(num_list[i])
	for j in range(1, i):
		for div in div_list:
			if num_list[j] % div == 0:
				num_list[j] = num_list[j] // div

mem = set()
mlt = 1
for el in num_list:
	mem.add(el)
	mlt *= el

print('Answer is {}'.format(mlt))
print('Dividers: {}'.format(mem))
input()
