from collections import Counter

# Ver 1

size_of_groups = int(input())
room_numbers = [int(x) for x in input().split()]

counter = Counter(room_numbers)

for k, v in counter.items():
    if v == 1:
        print(k)
        break

# Ver 2
#
# size_of_groups = int(input())
# room_numbers = [int(x) for x in input().split()]
#
# first_set = set()
# second_set = set()
#
# for i in room_numbers:
#     if i in first_set:
#         second_set.add(i)
#     else:
#         first_set.add(i)
#
# result = first_set.difference(second_set)
#
# print(*result)
