main_set_length = int(input())
main_set = set([int(x) for x in input().split()])
secondary_sets_count = int(input())

for i in range(secondary_sets_count):
    commands = input().split()

    command = commands[0]
    secondary_set_length = int(commands[1])
    secondary_set = set([int(x) for x in input().split()])

    if command == 'update':
        main_set.update(secondary_set)

    elif command == 'intersection_update':
        main_set.intersection_update(secondary_set)

    elif command == 'difference_update':
        main_set.difference_update(secondary_set)

    elif command == 'symmetric_difference_update':
        main_set.symmetric_difference_update(secondary_set)

print(sum(main_set))
