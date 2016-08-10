#Problem Set 1
#Name: Nick McGettigan
#Collaborators: None
#Time Spent: 0:30

outstandingBalance = float(raw_input("Outstanding Balance: $"))
annualInterestRate = float(raw_input("Annual Interest Rate (as a decimal): "))
monthlyInterestRate = float(annualInterestRate / 12)
minMonthlyPaymentRate = float(raw_input("Minimum Monthly Payment Rate (as a decimal): "))
totalPaid = 0


for i in range(1,13):

    print 'Month:', i
    minMonthlyPayment = minMonthlyPaymentRate * outstandingBalance
    interestPaid = monthlyInterestRate * outstandingBalance
    principalPaid = minMonthlyPayment - interestPaid
    outstandingBalance = outstandingBalance - principalPaid
    totalPaid = totalPaid + minMonthlyPayment
    print 'Minimum Monthly Payment: $' + format((round(minMonthlyPayment, 2)), '.2f')
    print 'Principle Paid: $' + format((round(principalPaid, 2)), '.2f')
    print 'Remaining Balance: $' + format((round(outstandingBalance, 2)), '.2f')
    if i == 12:
        print 'RESULT'
        print 'Total Amount Paid: $' + format((round(totalPaid, 2)), '.2f')
        print 'Remaining Balance: $' + format((round(outstandingBalance,2)), '.2f')
        
