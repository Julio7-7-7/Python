import random

dado = 0
while dado != 6:
    dado = random.randint(1, 6)
    print(f"Sacaste un {dado}")
print("Sacaste un 6")
