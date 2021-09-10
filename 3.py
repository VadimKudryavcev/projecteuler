def simple_d(n):
	if not n in prime_list:
		for i in prime_list:
			if n % i == 0:
				d = i
		return d
	return n

prime_list = []
not_prime_set = set()

n = int(input('Write a number: '))

for i in range(1, n + 1):
	if not i in not_prime_set:
		prime_list.append(i)
	for j in range(1, i + 1):
		if i * j <= n:
			not_prime_set.add(i * j)

print('Answer is {}'.format(simple_d(n)))
input()
