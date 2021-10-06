from itertools import product

first_list = [int(x) for x in input().split()]
second_list = [int(x) for x in input().split()]

result = list(product(first_list, second_list))

print(' '.join(str(x) for x in result))
