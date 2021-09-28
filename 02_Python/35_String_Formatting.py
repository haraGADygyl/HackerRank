def print_formatted(number):
    binary_value_number = len((bin(number).lstrip('0b')))  # 4

    for i in range(1, number + 1):
        print((binary_value_number - len(str(i))) * " " + str(i),
              (binary_value_number - len(oct(i).lstrip('0o'))) * " " + str(oct(i).lstrip('0o')),
              (binary_value_number - len(hex(i).lstrip('0x'))) * " " + str(hex(i).lstrip('0x').upper()),
              (binary_value_number - len(bin(i).lstrip('0b'))) * " " + str(bin(i).lstrip('0b'))
              )


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
