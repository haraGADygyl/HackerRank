set_a = set([int(x) for x in input().strip().split()])
sets_to_compare = int(input())

result = []

for i in range(sets_to_compare):

    set_b = set([int(x) for x in input().strip().split()])

    if set_a.issuperset(set_b):
        result.append(1)
    else:
        result.append(0)

print('True' if all(result) else 'False')
