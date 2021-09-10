import os

def isPrime(x):
	for div in prime_list[1:]:
		if x % div == 0:
			return False
	for d in range(2, x):
		if x % d == 0:
			return False
	return True

n = int(input('Write number: '))

prime_list = [1, 2, 3, 5, 7, 11]
k = 0
i = 12
while k < n:
	if isPrime(i):
		prime_list.append(i)
		k += 1
		os.system('cls')
		print('{}%'.format(int(100 * k / n)))
	i += 1

print('{} prime is {}'.format(k, prime_list[k-1]))
input()
