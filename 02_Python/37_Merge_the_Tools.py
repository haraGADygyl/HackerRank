def merge_the_tools(string_to_analyze, size_substring):
    result = []

    string_length = len(string_to_analyze)

    for i in range(0, string_length, size_substring):
        result.append(string_to_analyze[i:size_substring + i])

    for j in result:
        print(''.join(sorted(set(j), key=j.index)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
