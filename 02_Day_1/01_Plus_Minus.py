def plus_minus(arr):
    zeros = 0
    positives = 0
    negatives = 0

    for i in range(len(arr)):

        if arr[i] == 0:
            zeros += 1
        elif arr[i] > 0:
            positives += 1
        else:
            negatives += 1
    print(f'{positives / n:.6f}\n{negatives / n:.6f}\n'
          f'{zeros / n:.6f}')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plus_minus(arr)
