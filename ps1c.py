#Problem Set 1
#Name: Nick McGettigan
#Collaborators: None
#Time Spent: 11:20



#Gather inputs
initialBalance = float(raw_input("Initial Balance: $"))
annualInterestRate = float(raw_input("Annual interest rate in decimals: "))

#setup variables
balance = initialBalance
high = (balance * (1.0 + (annualInterestRate/12) )** 12) / 12
low = balance / 12



while True:    
    minMonthlyPayment = (high + low) / 2.0
    balance = initialBalance
    for month in range(1,13):
        interest = balance * annualInterestRate / 12.0
        balance += interest - minMonthlyPayment
        if balance <= 0:
            break

    if high-low < 0.001: #found solution
        print 'RESULT'
        print 'Monthly payment to pay off debt in 1 year:', round(minMonthlyPayment,2)
        print 'Months taken', month
        balance = initialBalance
        minMonthlyPayment = round(minMonthlyPayment,2) + 0.01
        for month in range (1,13):
            interest = balance * annualInterestRate / 12.0
            balance +=interest - minMonthlyPayment
        print 'Balance', round(balance,2)
        break
        
    elif balance > 0: #Not paid enough, increase low to current min and recompute
        low = minMonthlyPayment
        
    elif balance < 0: #paid too much, increase high amount to current min and recompute
        high = minMonthlyPayment
    


























