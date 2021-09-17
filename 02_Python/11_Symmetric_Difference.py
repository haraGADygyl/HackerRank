first_set_length = int(input())
first_set = set(input().split())
second_set_length = int(input())
second_set = set(input().split())

result = list(first_set.symmetric_difference(second_set))

for i in sorted([int(x) for x in result]):
    print(i)
