# convert distant given in feet and inches into meter and centimeter
feet = float(input("enter feets:-"))
inches = float(input("enter inches:-"))

total_inches = feet * 12 + inches

centimeter = total_inches * 2.54
meter = centimeter / 100

print("meter:-",meter)
print("centimeter:-",centimeter)
