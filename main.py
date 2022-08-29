def main():
    print("this is a monthly loan calculator")
    print("")

    princeable = float(input("the loan amount: "))
    apr = float (input("what is the amnual interest rate?: "))
    amount_of_years = int (input("what is the years: "))
    montly_interest_rate = apr / 1200
    amount_of_months = amount_of_years * 12
    montly_payment = princeable * montly_interest_rate / (1- (1 + montly_interest_rate) ** (- amount_of_months))

    print("the monthly payment for this loan is: " )
    print (montly_payment)


main()


