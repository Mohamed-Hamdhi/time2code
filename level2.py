# Ride height program
# -------------------------
# Subprograms
# -------------------------
# Check if the child is under 90cm.
def valid_height(height):
if height < 91:
return True
else:
return False
# -------------------------
# Main program
# -------------------------
height = float(input("Enter the height of the person in cm: "))
if valid_height(height):
print("Height OK.")
else:
print("Sorry, you are too tall.")
