from itertools import product
from string import ascii_uppercase as alphabet

registrations = {}

def gen_license_plates():

    for letters in product(alphabet, repeat=3):
        letters = "".join(letters)
        if letters == "GOV":
            continue

        for numbers in range(1000):
            yield f"{letters} {numbers:03}"


def new_registration(owner):
    if owner not in registrations:
        plate = next(license_plates)
        registrations[owner] = plate
        return plate
    return None



license_plates = gen_license_plates()

count_plates = 0
for plate in license_plates:
    print(f"Plate {plate}")
    count_plates += 1
    if count_plates >= 100:
        break



print(new_registration("Marcello Chiuminatto"))


# fast forward

for _ in range(5000):
    next(license_plates)


print(new_registration("Floki"))


for _ in range(5000):
    next(license_plates)


print(new_registration("Xoxi"))

plates_2 = gen_license_plates()


print(next(plates_2))

