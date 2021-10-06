from itertools import permutations

text, number = input().split()
text = sorted(x for x in text)
number = int(number)

result = list(permutations(text, number))

for i in result:
    final_str = ''
    for j in i:
        final_str += j
    print(final_str)
