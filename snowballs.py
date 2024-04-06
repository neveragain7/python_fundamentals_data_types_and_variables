import sys

number_of_snowballs = int(input())
max_snow = ""
max_time = ""
max_quality = ""
max_value = -sys.maxsize

for snowball in range(1, number_of_snowballs + 1):
    snow = int(input())
    time = int(input())
    quality = int(input())
    value = int((snow / time) ** quality)
    if value > max_value:
        max_snow = snow
        max_time = time
        max_quality = quality
        max_value = value

print(f"{max_snow} : {max_time} = {max_value} ({max_quality})")
