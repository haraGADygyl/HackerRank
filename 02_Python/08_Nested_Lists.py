if __name__ == '__main__':

    full_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        full_list.append([name, score])

    scores = set()
    for name, score in full_list:
        scores.add(score)

    second_lowest = sorted(list(scores))[1]

    lowest_list = []
    for name, score in full_list:
        if score == second_lowest:
            lowest_list.append(name)

    lowest_list.sort()

    print('\n'.join(lowest_list))
