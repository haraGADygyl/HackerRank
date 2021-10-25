from itertools import combinations_with_replacement

message, number = input().split()
number = int(number)

sorted_message = sorted(message)
combinations = list(combinations_with_replacement(sorted_message, number))

for i in combinations:
    print(*i, sep='')
