# Seasons program

# -------------------------
# Subprograms
# -------------------------
def seasons(month):
    match month:
        case "December" |"12" | "January"|"1" | "February"|"2":
            return "Winter"
        case "March"|"3" | "April"|"4" | "May"|"5":
            return "Spring"
        case "June"|"6"| "July"|"7" | "August"|"8":
            return "Summer"
        case "September"|"9" | "October"|"10" | "November"|"11":
            return "Autumn"
        case _:
            return "Error"


# -------------------------
# Main program
# -------------------------
month = input("Enter the month: ")
season = seasons(month)
print("Month", month, "is in the", season)
