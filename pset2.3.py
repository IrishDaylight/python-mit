currentBalance = balance
monthlyInterestRate = annualInterestRate / 12.0 #Monthly interest rate
month = 1
loMonthlyPayment = balance / 12
hiMonthlyPayment = (balance * (1 + monthlyInterestRate)**12) / 12.0
oldPayment = hiMonthlyPayment #Set previous payment value

payment = (loMonthlyPayment + hiMonthlyPayment) / 2.0

while abs(oldPayment - payment) > 0.01: #Check if balance is finished being paid
    currentBalance = balance
    month = 1

    while month < 13:

        monthlyInterest = monthlyInterestRate * currentBalance #Calculate monthly interest
        currentUnpaidBalance = currentBalance - payment #Calculate unpaid balance
        currentBalance = currentUnpaidBalance + (monthlyInterestRate * currentUnpaidBalance) #Calculate the balance

        month += 1

    oldPayment = payment #Set old payment value

    #Check which half of the range the payment would be in
    if currentBalance < 0:
        hiMonthlyPayment = payment
    else:
        loMonthlyPayment = payment

    #Calculate payment
    payment = (loMonthlyPayment + hiMonthlyPayment) / 2.0

print "Lowest Payment: " + str(round(payment, 2))
