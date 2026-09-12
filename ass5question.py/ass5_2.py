# 2. enter number of students from user. for those many students accept marks of 5
# subjects marks from user and calculate percentage . display all percentage and 
# average percentage of students.

students = int(input("enter number of students:"))

total_percentage = 0

for i in range(1, students + 1):
    print("\nenter marks of students ", i)

    total = 0

    for j in range(1,6):
        marks = int(input(f"enter marks of subjects {j}:"))
        total += marks

        percentage = total / 5
        print("percentage of students", i, "=", percentage, "%")

        total_percentage += percentage

        average = total_percentage / students

        print("\naverage percentage of all students =", average, "%")