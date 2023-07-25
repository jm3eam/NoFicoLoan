from colorama import Back, Fore, Style, init

# Initialize colorama for colored text output
init()


def calculate_creditworthiness():
    points = 0

    # Metric 1: Loan Amount
    while True:
        print("\033[1;33;14mMin.Loan $1000 - Max.Loan $75000\033[0m")
        loan_amount = input("Loan amount: ")
        try:
            loan_amount = float(loan_amount)
            if 1000 <= loan_amount <= 75000:
                break
            else:
                print("Loan amount out of range. Enter the correct amount")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Metric 2: Income Point ratio
    monthly_income = float(input("Monthly after-tax income amount: "))
    if monthly_income > 5000:
        points += 40
    elif monthly_income > 2500:
        points += 30
    elif monthly_income > 1250:
        points += 20
    elif monthly_income > 650:
        points += 10
    else:
        points += 5
      
    # Metric 3: Length of Employment
    employment_years = int(input("Years of employment: "))
    if employment_years >= 4:
        points += 20
    elif employment_years >= 2:
        points += 10
    else:
        points += 5

     # Metric 4: Home Ownership
    homeownership = get_yes_or_no_input("Home Ownership (Yes/No): ")
    if homeownership == "yes":
        cep = float(input("Current equity in your property: "))
        if cep > 50000:
            points += 10
        elif cep > 25000:
            points += 5
        else:
            points += 2

     # Metric 5: Other Personal Income
    cmbab = float(input("Combined monthly bank account balances: "))
    if cmbab > 0.5 * loan_amount:
        points += 10
    elif cmbab > 0.25 * loan_amount:
        points += 5
    else:
        points += 2

    retirement_income = get_yes_or_no_input("Do you receive retirement income? (Yes/No): ")
    if retirement_income == "yes":
        mri = float(input("Monthly retirement income: "))
        if mri > 0.5 * loan_amount:
            points += 10
        elif mri > 0.25 * loan_amount:
            points += 5
        else:
            points += 2


    investment_income = get_yes_or_no_input("Do you receive investment income? (Yes/No): ")
    if investment_income == "yes":
        mii = float(input("Monthly investment income: "))
        if mii > 0.5 * loan_amount:
            points += 10
        elif mii > 0.25 * loan_amount:
            points += 5
        else:
            points += 2

  # Metric 6: Age of Applicant
    age = int(input("Age of Applicant: "))
    if age > 99:
        print("\033[92m")
        print("Contact your loan officer and provide code 099DOB")
        print("\033[0m")
        return None
    elif age < 18:
        print("\033[91m")
        print("Contact your loan officer and provide code U18DOB")
        print("\033[0m")
        return None
    else:
        if age >= 65:
            points += 4
        elif 50 <= age < 65:
            points += 6
        elif 35 <= age < 50:
            points += 8
        elif 25 <= age < 35:
            points += 10
        elif 18 <= age < 25:
            points += 5

    # Calculate Total Income
    total_income = monthly_income + cmbab
    if retirement_income == "yes":
      total_income += mri
    else:
      mri = 0
    if investment_income == "yes":
        total_income += mii
    else:
     mii = 0

    # Debt Risk Score Calculation
    rent_mortgage = float(input("Monthly Rent/Mortgage: "))
    car_payment_insurance = float(input("Car Payment/Insurance: "))
    monthly_cc_debt = float(input("Monthly Credit Card Debt: "))
    monthly_groceries = float(input("Monthly Groceries: "))
    monthly_student_debt = float(input("Monthly Student Debt: "))

    if rent_mortgage < 0.3 * total_income:
        points -= 0
    elif rent_mortgage < 0.4 * total_income:
        points -= 10
    elif rent_mortgage < 0.5 * total_income:
        points -= 20
    elif rent_mortgage < 0.6 * total_income:
        points -= 30
    else:
        points -= 40

    if car_payment_insurance < 0.3 * total_income:
        points -= 5
    elif car_payment_insurance < 0.4 * total_income:
        points -= 10
    elif car_payment_insurance > 0.5 * total_income:
        points -= 20

    if monthly_cc_debt > 0.5 * total_income:
        points -= 20
    elif monthly_cc_debt > 0.4 * total_income:
        points -= 10
    elif monthly_cc_debt <= 0.3 * total_income:
        points -= 5

    if monthly_groceries < 0.2 * total_income:
        points -= 0
    elif 0.2 * total_income < monthly_groceries < 0.5 * total_income:
        points -= 5
    elif monthly_groceries > 0.5 * total_income:
        points -= 10

    if monthly_student_debt < 0.2 * total_income:
        points -= 0
    elif 0.2 * total_income < monthly_student_debt < 0.5 * total_income:
        points -= 5
    elif monthly_student_debt > 0.5 * total_income:
        points -= 10

    credit_worthiness_points = points

    # Determine Loan Eligibility Score
    loan_eligibility_score = (credit_worthiness_points / 100) * 100
    return loan_eligibility_score
  
    # Determine Loan Approval Percentage
    if 5 <= loan_eligibility_score <= 10:
        approval_percentage = 35
    elif 11 <= loan_eligibility_score <= 15:
        approval_percentage = 40
    elif 16 <= loan_eligibility_score <= 20:
        approval_percentage = 45
    elif 21 <= loan_eligibility_score <= 25:
        approval_percentage = 50
    elif 26 <= loan_eligibility_score <= 30:
        approval_percentage = 55
    elif 31 <= loan_eligibility_score <= 35:
        approval_percentage = 60
    elif 36 <= loan_eligibility_score <= 40:
        approval_percentage = 65
    elif 41 <= loan_eligibility_score <= 50:
        approval_percentage = 70
    elif 51 <= loan_eligibility_score <= 60:
        approval_percentage = 80
    elif 61 <= loan_eligibility_score <= 80:
        approval_percentage = 90
    elif 81 <= loan_eligibility_score <= 100:
        approval_percentage = 100
    else:
        approval_percentage = 0

    return approval_percentage


def get_yes_or_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ("y", "yes"):
            return "yes"
        elif response in ("n", "no"):
            return "no"
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

def main():
    print(Fore.MAGENTA + Style.BRIGHT + "Credit-Worth Income vs Debt Calculator, No FICO")
    print(Style.RESET_ALL)  # Reset colorama formatting

    while True:
        approval_percentage = calculate_creditworthiness()

        if approval_percentage:
            loan_amount = float(input("Enter the loan amount: "))
            approval_amount = (approval_percentage / 100) * loan_amount

            print(Fore.GREEN + Back.WHITE + Style.BRIGHT + f"Loan Approval Percentage: {approval_percentage:.2f}%")
            print(Fore.GREEN + Back.WHITE + Style.BRIGHT + f"Congratulations! You have been approved for the amount of: ${approval_amount:.2f}")
            print(Style.RESET_ALL)  # Reset colorama formatting

        response = input("Would you like to start a new application? (Yes/No): ").strip().lower()
        if response in ("yes", "y"):
            print("\nStarting a new application...\n")
        else:
            print(Fore.BLUE + Style.BRIGHT + "Thank you for using this calculator, created by an MDC student for a Python Class")
            break


if __name__ == "__main__":
    main()
#using the code is the force of the futue