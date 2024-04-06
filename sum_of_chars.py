number = int(input())
order_sum = 0
total_sum = 0
for times in range(1, number + 1):
    letter = input()
    order_sum = (ord(letter))
    total_sum += order_sum

print(f"The sum equals: {total_sum}")
