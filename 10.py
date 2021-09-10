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

prime_list = []
sum_ = 0
i = 1
while i <= n:
	if isPrime(i):
		prime_list.append(i)
		sum_ += i
	i += 1

print('Sum of primes below {} is {}'.format(n, sum_))
input()