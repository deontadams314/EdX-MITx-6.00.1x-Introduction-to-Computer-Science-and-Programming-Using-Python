def debtPay(balance,annualInterestRate,monthlyPaymentRate):
	month = 0
	while month < 12:

		interest_monthly = annualInterestRate / 12 
		minimum_payment = monthlyPaymentRate * balance
		unpaid_balance = balance - minimum_payment
		new_balance = round(((unpaid_balance) + (interest_monthly * unpaid_balance)), 2)
		
		month += 1
		print("Month " + str(month) + " remaining balance: " + str(new_balance))
		balance = new_balance

	return balance
