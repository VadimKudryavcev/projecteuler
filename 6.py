n = int(input('Write a number: '))

sum_of_sqr = int(n * (n + 1) * (2 * n + 1) / 6)
sqr_of_sum = int((n * (n + 1) / 2) ** 2)

print('{} - {} = {}'.format(sqr_of_sum, sum_of_sqr, sqr_of_sum - sum_of_sqr))
input()