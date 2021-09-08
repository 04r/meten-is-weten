maxim = []
minim = []

getal1 = input("Getal 1: ")
getal2 = input("Getal 2: ")

if getal1 > getal2:
    minim = f"{getal1}, getal 1"
    maxim = f"{getal2}, getal 2"
else:
    maxim = f"{getal2}, getal 2"
    minim = f"{getal1}, getal 1"

print(f"Max: {maxim}")
print(f"Min: {minim}")