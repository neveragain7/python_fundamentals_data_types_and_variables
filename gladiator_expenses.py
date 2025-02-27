lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
shield_counter = 0
expenses = 0

for fights in range(1, lost_fights_count + 1):
    if fights % 2 == 0:
        expenses += helmet_price
    if fights % 3 == 0:
        expenses += sword_price
    if fights % 2 == 0 and fights % 3 == 0:
        expenses += shield_price
        shield_counter += 1
        if shield_counter % 2 == 0:
            expenses += armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
