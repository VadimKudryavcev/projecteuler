for a in range(1, 1000 - 1):
	for b in range(a, 1000 - 1):
		c = 1000 - a - b
		if a * a + b * b == c * c:
			aa, bb, cc = a, b, c
			break

print('(a, b, c) = ({}, {}, {})'.format(aa, bb, cc))
input()