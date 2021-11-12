from collections import Counter

shoes_count = int(input())
shoes = [int(x) for x in input().split()]
customers = int(input())

counter = Counter(shoes)

profit = 0

for i in range(customers):
    order_data = input().split()
    shoe_size_order = int(order_data[0])
    shoe_price_order = int(order_data[1])

    if counter[shoe_size_order] > 0:
        counter[shoe_size_order] -= 1
        profit += shoe_price_order

print(profit)
