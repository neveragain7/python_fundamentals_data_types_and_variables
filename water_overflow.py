number_of_lines = int(input())
capacity = 255
total_liters = 0
full_capacity_reached = False
for line in range(1, number_of_lines + 1):
    liters = int(input())
    if total_liters + liters > capacity:
        full_capacity_reached = True
    else:
        total_liters += liters

if full_capacity_reached:
    print("Insufficient capacity!")

print(total_liters)
