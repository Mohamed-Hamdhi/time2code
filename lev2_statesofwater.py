# States of water problem
# -------------------------
# Subprograms
# -------------------------
# Return the state of water
def water_state(centigrade):
# Less than or equal to 0°.
    if centigrade <= 0:
        return "solid"
# Less than 100° but greater than 0°.
    elif centigrade < 100:
        return "liquid"
# 100° or above.
    else:
        return "gaseous"
# -------------------------
# Main program
# -------------------------
temperature = float(input("Enter the temperature in °C: "))
state = water_state(temperature)
print("The water is in a", state, "state.")
