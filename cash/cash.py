from cs50 import get_float

# Ask user for a positive owed value
while True:
    n = get_float("How much is owed? ")
    if n > 0:
        break

# Turn dollars into number of cents
cents = int(n * 100 + 0.1)

# Calculate the number of quarters owed
q = cents // 25
cents = cents - q * 25

# Calculate the number of dimes owed
d = cents // 10
cents = cents - d * 10

# Calculate the number of nickels owed
ni = cents // 5
cents = cents - ni * 5

# Calculate the number of pennies owed
p = cents

# Print the total number of coins returned
print(q + d + ni + p)
