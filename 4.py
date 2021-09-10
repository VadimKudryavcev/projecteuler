def isPalindrome(n):
	string = str(n)
	new_string = ''
	for i in string:
		new_string = i + new_string
	return new_string == string

for i in range(1000, 100, -1):
	for j in range(1000, 100, -1):
		if isPalindrome(i * j):
			ans = i * j
			break

print('Answer is {} * {} = {}'.format(i, j, ans))
input()

