height = float(input("your height = "))
weight = float(input("your weight = "))

body_mass_index = weight / ((height / 100) * (height / 100))

if body_mass_index < 16:
    print("severely underweight")
elif 16 < body_mass_index <= 18.5:
    print("underweight")
elif 18.5 < body_mass_index <= 25:
    print("normal")
elif 25 < body_mass_index <= 30:
    print("overweight")
else:
    print("obese")
print(input("press alt + f4 to exit"))