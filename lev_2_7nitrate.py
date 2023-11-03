# Nitrate problem
# -------------------------
# Subprograms
# -------------------------
# Calculate the carbon dose
def calculate_dose(nitrate):
    if nitrate > 10:
# Nitrate is more than 10 dose 3ml.
        return 3
# Nitrate is more than 2.5 does 2.5ml
    elif nitrate > 2.5:
        return 2
# Nitrate is more than 1 dose 1ml.
    elif nitrate > 1:
        return 1
# Dose 0.5ml in all other cases.
    else:
        return 0.5
# -------------------------
# Main program
# -------------------------
nitrate = float(input("Enter the nitrate level from the test: "))
carbon_dose = calculate_dose(nitrate)
print("For", nitrate, "nitrate dose", carbon_dose, "ml of carbon.")
