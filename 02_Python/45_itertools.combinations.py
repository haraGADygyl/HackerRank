from itertools import combinations

text, number = input().split()
text = sorted(list(text))
number = int(number)

result = []
for i in range(1, number + 1):
    word = list(combinations(text, i))
    result.extend(word)

for j in result:
    print(*j, sep='')
