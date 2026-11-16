def check_eligibility(name, age, indian_citizen):

    if age >= 18 and indian_citizen == "yes":
        print(name, "is eligible to vote.")
        return True

    elif age < 18:
        print(name, "is not eligible to vote.")
        print("Reason: Age is below 18.")
        print("Years left to become eligible:", 18 - age)
        return False
    
    elif indian_citizen == "no":
        print(name, "is not eligible to vote.")
        print("Reason: Not an Indian citizen.")
        return False



while True:
    name = input("Enter your name: ").strip()

    while name == "":
        print("Name cannot be empty.")
        name = input("Enter your name: ").strip()



    while True:
        try:
            age = int(input("Enter your age: "))
            if age >= 0 and age <= 120:
                break
            else:
                print("Invalid age. Age must be between 0 and 120.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


    while True:
        indian_citizen = input("Are you an Indian citizen? (yes/no): ").strip().lower()

        if indian_citizen == "yes" or indian_citizen == "no":
            break
        else:
            print("Invalid input. Please enter yes or no.")



    result = check_eligibility(name, age, indian_citizen)
    

    total_voters = 0
    eligible_voters = 0
    ineligible_voters = 0

    total_voters += 1

    if result == True:
        eligible_voters += 1

    else:
        ineligible_voters += 1

    while True:
        check = input("Do you want to check another voter? (yes/no): ").strip().lower()
    
        if check == "yes" or check == "no":
            break
        else:
            print("Please enter yes or no.")
    
        if check == "no":
            break

    
    print("Total voters checked:", total_voters)
    print("Eligible voters:", eligible_voters)
    print("Ineligible voters:", ineligible_voters)
