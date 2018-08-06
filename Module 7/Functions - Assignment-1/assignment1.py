'''Calculatingpaying_debtoffinayear.'''
def paying_debtoffinayear(balance_num, annual_interestrate, monthly_paymentrate):
    '''paying_debtoffinayear function.'''
    monthly_interestrate = (annual_interestrate)/12.0
    minimum_monthlypayment = (monthly_paymentrate)*balance_num
    monthly_unpaidbalance = balance_num-minimum_monthlypayment
    updatedbalance_num = monthly_unpaidbalance+(monthly_interestrate*monthly_unpaidbalance)
    return updatedbalance_num
def main():
    '''Main Function.'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    i = 0
    while i != 12:
        data[0] = paying_debtoffinayear(data[0], data[1], data[2])
        i = i+1
    print("Remaining balance:", round(data[0], 2))
if __name__ == "__main__":
    main()
