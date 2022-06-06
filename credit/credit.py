from cs50 import get_string

# Prompt user for card number
while True:
    n = get_string("Card number: ")
    if int(n) > 0:
        break

n_copy = n[::-1]
primary_sum = 0
secondary_sum = 0
primary_num = n_copy[0::2]
secondary_num = n_copy[1::2]

# Loop over odd digits
for num in primary_num:
    primary_sum += int(num)

# Loop over even digits
for num in secondary_num:
    new_num = int(num) * 2

    if new_num > 9:
        new_num = new_num // 10 + new_num % 10

    secondary_sum += new_num

total = secondary_sum + primary_sum

if total % 10 == 0:

    if len(n) == 15 and n[0:2] in ["34", "37"]:
        print("AMEX")
    elif len(n) == 16 and 51 <= int(n[0:2]) <= 55:
        print("MASTERCARD")
    elif len(n) in [13, 16] and n[0] == "4":
        print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")