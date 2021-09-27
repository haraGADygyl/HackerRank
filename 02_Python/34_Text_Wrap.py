import textwrap


def wrap(text, m_width):
    arr = textwrap.wrap(text, width=m_width)

    return '\n'.join(arr)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
