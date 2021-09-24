def split_and_join(text):
    return '-'.join(text.strip().split())


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
