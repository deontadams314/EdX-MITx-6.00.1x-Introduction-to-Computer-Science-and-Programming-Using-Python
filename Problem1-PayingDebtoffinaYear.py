def debtProb(balance, annualInterestRate, monthlyPaymentRate):
    for month in range(12):
        monthly_interest = annualInterestRate / 12
        min_monthly_pay = monthlyPaymentRate * balance
        monthly_unpaid_bal = balance - min_monthly_pay
        updated_balance = round(monthly_unpaid_bal + (monthly_interest * monthly_unpaid_bal), 2)
        #month += 1
        balance =  updated_balance
    print ("Remaining balance: " + str(balance))

debtProb(balance, annualInterestRate, monthlyPaymentRate)
