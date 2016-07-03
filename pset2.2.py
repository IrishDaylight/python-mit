currentBalance = balance
monthlyInterestRate = annualInterestRate / 12.0 #Monthly interest rate
month = 1
fixedPayment = 0

while currentBalance > 0: #Check if balance is finished being paid
    finalBalance = currentBalance #Previous final balance
    currentBalance = balance
    month = 1
    fixedPayment += 10 #increment fixed monthly payment

    while month < 13:

        monthlyInterest = monthlyInterestRate * currentBalance #Calculate monthly interest
        currentUnpaidBalance = currentBalance - fixedPayment #Calculate unpaid balance
        currentBalance = currentUnpaidBalance + (monthlyInterestRate * currentUnpaidBalance) #Calculate the balance

        month += 1

print "Lowest Payment: " + str(fixedPayment)
