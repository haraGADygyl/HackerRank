stamps_count = int(input())

unique_stamps = set()

for i in range(stamps_count):
    current_stamp = input().rstrip()

    if current_stamp not in unique_stamps:
        unique_stamps.add(current_stamp)

print(len(unique_stamps))
