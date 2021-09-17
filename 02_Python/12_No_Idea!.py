arr_length, sets_range = [int(x) for x in input().rstrip().split()]
numbers = [int(x) for x in input().rstrip().split()]
liked_numbers = set([int(x) for x in input().rstrip().split()])
disliked_numbers = set([int(x) for x in input().rstrip().split()])

total_happiness = 0

for i in range(arr_length):

    if numbers[i] in liked_numbers:
        total_happiness += 1

    if numbers[i] in disliked_numbers:
        total_happiness -= 1

print(total_happiness)
