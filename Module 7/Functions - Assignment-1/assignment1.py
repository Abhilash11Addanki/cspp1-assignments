'''Calculatingpaying_debtoffinayear.'''
def paying_debtoffinayear(balance_num, annual_interestrate, monthly_paymentrate):
    '''paying_debtoffinayear function.'''
    i = 0
    while i != 12:
        monthly_interestrate = (annual_interestrate)/12.0
        minimum_monthlypayment = (monthly_paymentrate)*balance_num
        monthly_unpaidbalance = balance_num-minimum_monthlypayment
        updatedbalance_num = monthly_unpaidbalance+(monthly_interestrate*monthly_unpaidbalance)
        balance_num = updatedbalance_num
        i += 1
    return round(balance_num, 2)
def main():
    '''Main function.'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Remaining balance:", paying_debtoffinayear(data[0], data[1], data[2]))
if __name__ == "__main__":
    main()
