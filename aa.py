maxim = ""
minim = ""
equal = ""

getal1 = input("Getal 1: ")
getal2 = input("Getal 2: ")

if getal1 > getal2:
    minim = f"{getal1}, getal 1"
    maxim = f"{getal2}, getal 2"
elif getal2 > getal1:
    maxim = f"{getal2}, getal 2"
    minim = f"{getal1}, getal 1"
if getal1 == getal2:
    equal = "Yes"
    maxim = "Equal!"
    minim = "Equal!"
else:
    equal = "No"

print(f"Max: {maxim}")
print(f"Min: {minim}")
print(f"Equal? {equal}")