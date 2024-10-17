name = input("Please enter your name:")
section = input("Please enter your section:")

prelim = float(input("Enter your Prelim Grade:"))
if prelim < 40 or prelim > 100:
    print("Invalid input. Must be between 40 and 100")
else:
    midterm = float(input("Enter your Midterm Grade:"))
    if midterm < 40 or midterm > 100:
        print("Invalid input. Must be between 40 and 100")
        
    else:
        finalterm=float(input("Enter your Finalterm Grade:"))
        if finalterm < 40 or finalterm > 100:
            print("Invalid input. Must be between 40 and 100")
            
        else:
            FinalGrade = (prelim * 0.3333) + (midterm * 0.3333) + (finalterm * 0.3333)
            FinalGrade = round(FinalGrade)
            print("Your Final Grade is:", FinalGrade)

    if 99<= FinalGrade <=100:
        print("your GPA is 1.0")
    elif 96<= FinalGrade <=98:
        print("your GPA is 1.25")
    elif 93<= FinalGrade <=95:
        print("your GPA is 1.50") 
    elif 90<= FinalGrade <=92:
        print("your GPA is 1.75")
    elif 87<= FinalGrade <=89:
        print("your GPA is 2.00")
    elif 84<= FinalGrade <=86:
        print("your GPA is 2.25")
    elif 81<= FinalGrade <=83:
        print("your GPA is 2.50")
    elif 78<= FinalGrade <=80:
        print("your GPA is 2.75")
    elif 75<= FinalGrade <=77:
        print("your GPA is 3.00")
    elif FinalGrade <=74:
        print("your GPA is 5.00")
    else:
        print("Invalid input. Must be between 40 and 100")
    
    