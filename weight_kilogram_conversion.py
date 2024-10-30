weight = float(input("Please enter your weight: "))
unit_of_weight = input("Is this in pounds or kilograms?: ").lower()

if unit_of_weight == "pounds":
  weight = weight / 2.205
  unit_of_weight = "kilograms"
  print(f"Your weight is {round(weight, 2)} {unit_of_weight}.")

elif unit_of_weight == "kilograms":
  weight = weight * 2.205
  unit_of_weight = "pounds"
  print(f"Your weight is {round(weight, 2)} {unit_of_weight}.")

else:
  print("Error: Invalid unit of weight.")