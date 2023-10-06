# Largest number program
# -------------------------
# Subprograms
# -------------------------
# Check which of the three numbers is the largest.
def largest(number1, number2, number3):
# All three are the same.
if (number1 == number2) and (number1 == number3):
return 1
# One is the largest.
elif (number1 > number2) and (number1 > number3):
  return 1
# Two is the largest.
elif (number2 > number1) and (number2 > number3):
return 2
# Three must be the largest otherwise.
else:
return 3
# -------------------------
# Main program
# -------------------------
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
print("The largest is number:", largest(number1, number2, number3))
