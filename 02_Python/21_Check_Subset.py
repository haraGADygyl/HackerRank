tests_count = int(input().strip())

for i in range(tests_count):
    set_a_length = int(input())
    set_a = set([int(x) for x in input().strip().split()])
    set_b_length = int(input())
    set_b = set([int(x) for x in input().strip().split()])

    if set_a.issubset(set_b):
        print('True')
    else:
        print('False')
