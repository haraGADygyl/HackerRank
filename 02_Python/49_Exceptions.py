number_of_cases = int(input())

for i in range(number_of_cases):
    first_value, second_value = input().split()

    try:
        print(int(first_value) // int(second_value))
    except BaseException as e:
        print('Error Code:', e)
