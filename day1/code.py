fuelRequired = 0
mass = 0
finalMass = 0
fuelRequiredTask2 = 0

input = open("input.txt", "r");
input2 = open("input.txt", "r");

print("----------Task 1----------")

for line in input:
    mass = int(line)
    finalMass = (mass/3) - 2
    fuelRequired = fuelRequired + finalMass

print("Fuel required is " + str(fuelRequired))

print("----------Task 2----------")

for line in input2:
    mass = int(line)
    print("initial mass = " + str(mass))
    while mass > 0:
        finalMass = (mass/3) - 2
        if finalMass < 1: finalMass = 0;
        fuelRequiredTask2 = fuelRequiredTask2 + finalMass
        mass = finalMass
        print(str(mass))

print("Tast 2 fuel required is " + str(fuelRequiredTask2))
