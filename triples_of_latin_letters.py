number = int(input())

for letter_1 in range(1, number + 1):
    for letter_2 in range(1, number + 1):
        for letter_3 in range(1, number + 1):
            print(f"{chr(letter_1 + 96)}{chr(letter_2 + 96)}{chr(letter_3 + 96)}")
