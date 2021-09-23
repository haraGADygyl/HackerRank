x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]

print([x for x in result if sum(x) != n])
