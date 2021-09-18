set_length = int(input())
numbers = set(map(int, input().split()))
commands_count = int(input())

for i in range(commands_count):
    command_input = input().split()
    command = command_input[0]

    if command == 'remove':
        command_number = int(command_input[1])

        numbers.remove(command_number)

    elif command == 'discard':
        command_number = int(command_input[1])

        numbers.discard(command_number)

    else:
        numbers.pop()

print(sum(numbers))
