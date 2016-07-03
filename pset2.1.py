#Calculate credit car balance

month = 1
monthIntRate = 0.0
minMonthPaymentRate = 0.0
monthUnpaidBal = 0.0
monthUpdatedBal = 0.0
monthOldBal = balance
totalPayment = 0.0

while month < 13:
    #Monthly interest rate
    monthIntRate = annualInterestRate / 12.0
    #Minimum monthly payment
    minMonthPaymentRate = monthlyPaymentRate * monthOldBal
    #Monthly unpaid balance
    monthUnpaidBal = monthOldBal - minMonthPaymentRate
    #Updated balance each month
    monthUpdatedBal = monthUnpaidBal + monthIntRate * monthUnpaidBal

    #Print orders
    print "Month: " + str(month)
    print "Minimum monthly payment: " + str(round(minMonthPaymentRate, 2))
    print "Remaining balance: " + str(round(monthUpdatedBal, 2))

    #Next month
    month += 1
    #Set current balance
    monthOldBal = monthUpdatedBal
    #Add to total payment
    totalPayment += minMonthPaymentRate

print "Total paid: " + str(round(totalPayment, 2)) #Print total payment
print "Remaining balance: " + str(round(monthUpdatedBal, 2)) #Remaining balance
