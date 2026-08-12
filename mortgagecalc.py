rate = input("Enter your APR: ")
loan = input("Enter your loan amount: ")
term = input("Enter your term length (in yrs): ")

try:
    r = float(rate) / (100. * 12.)
    P = float(loan)
    Y = float(term)

    # total number of payments
    n = Y * 12

    #M = P ( ( r(1+r)n ) / (1+r) n - 1 )
    M = P * ( (r *(1 + r) ** n) / ((1 + r) ** n - 1))

    payment = round(M, 2)
    print("Your monthly payment is: $" + str(payment))

    B = P # B is the Remaining loan balance
    for payment_num in range(int(n)):
        # Monthly Interest
        I = B * r

        # Monthly Principal
        Principal_Paid = M - I

        #Set B to new Loan Balance
        B -= Principal_Paid # Same as B = B - Principal_Paid

        print("Month", str(payment_num + 1), ":", "I = $" + str(round(I, 2)), 
              "Principal_Paid = $" + str(Principal_Paid))
except Exception as e:
    print("Error occured:", e)
    raise e