def calculate_cgpa():
    total_weighted_sgpa = 0
    total_credits = 0
    
    semesters = int(input("Enter the number of semesters: "))
    
    for sem in range(1, semesters + 1):
        sgpa = float(input(f"Enter SGPA for Semester {sem}: "))
        credits = float(input(f"Enter total credits for Semester {sem}: "))
        
        total_weighted_sgpa += sgpa * credits
        total_credits += credits
        
    if total_credits == 0:
        print("Total credits cannot be zero. Check your inputs.")
        return
    
    cgpa = total_weighted_sgpa / total_credits
    print(f"\nYour CGPA across {semesters} semesters is: {cgpa:.2f}")

# Run the function
calculate_cgpa()
