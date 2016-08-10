#Problem Set 1
#Name: Nick McGettigan
#Collaborators: None
#Time Spent: 1:10



#Gather inputs
initialBalance = float(raw_input("Initial Balance: $"))
annualInterestRate = float(raw_input("Annual interest rate in decimals: "))

#setup variables
minMonthlyPayment = 0
interestRate = annualInterestRate / 12
balance = initialBalance

#begin search for monthly payments large enough to pay off balance in 12 months
while balance > 0:
    balance = initialBalance
    currMonth = 0    
    minMonthlyPayment += 10
#calculate if current monthlypayment is enough
    while currMonth < 12 and balance > 0:

        currMonth += 1 # keep track of current month

        #add interest and subtract payment from balance
        balance *= (1.0 + interestRate)
        balance -= minMonthlyPayment
        
        
balance = round(balance, 2)
print 'RESULT'
print 'Monthly payment to pay off debt in 1 year:', minMonthlyPayment
print 'Months taken', currMonth
print 'Balance', balance





                           
