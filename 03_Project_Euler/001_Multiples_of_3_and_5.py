for i in range(int(input())):
    num = int(input())

    multiples_of_3 = (num - 1) // 3
    multiples_of_5 = (num - 1) // 5
    multiples_of_15 = (num - 1) // 15

    sum_of_multiples_of_3 = (3 * (multiples_of_3 * (multiples_of_3 + 1) // 2))
    sum_of_multiples_of_5 = (5 * (multiples_of_5 * (multiples_of_5 + 1) // 2))
    sum_of_multiples_of_15 = (15 * (multiples_of_15 * (multiples_of_15 + 1) // 2))

    total = sum_of_multiples_of_3 + sum_of_multiples_of_5 - sum_of_multiples_of_15

    print(total)
