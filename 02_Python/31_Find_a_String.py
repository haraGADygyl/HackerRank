import re


def count_substring(main_str, sub_str):
    pattern = r'(?=' + sub_str + ')'
    return len(re.findall(pattern, main_str))


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
