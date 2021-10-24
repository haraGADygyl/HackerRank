import string


def print_rangoli(size):
    letters = string.ascii_lowercase

    arr = []

    for i in range(size):
        s = '-'.join(letters[i:size])
        arr.append((s[::-1] + s[1:]).center(4 * size - 3, '-'))

    print('\n'.join(arr[:0:-1] + arr))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
