from collections import OrderedDict

item_count = int(input())

result = OrderedDict()
for i in range(item_count):
    data = input().rsplit(' ', 1)
    item_name = data[0]
    item_price = int(data[1])

    if item_name not in result:
        result[item_name] = item_price
    else:
        result[item_name] += item_price

for k, v in result.items():
    print(k, v)
