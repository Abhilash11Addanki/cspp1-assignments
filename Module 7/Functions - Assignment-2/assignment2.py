'''paying_debtoffinayear.'''
def paying_debtoffinayear(balance_num, annual_interestrate):
    '''Function.'''
    minimum_fixedmonthlypayment = 10
    while True:
        b_1 = balance_num
        ar_1 = annual_interestrate
        i = 0
        while i != 12:
            monthly_interestrate = ar_1/12.0
            monthly_unpaidbalance = b_1-minimum_fixedmonthlypayment
            b_1 = monthly_unpaidbalance+(monthly_interestrate*monthly_unpaidbalance)
            i += 1
        if b_1 <= 0.05:
            print("Lowest Payment:", minimum_fixedmonthlypayment)
            break
        minimum_fixedmonthlypayment += 10
def main():
    '''Main Function.'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    paying_debtoffinayear(data[0], data[1])
if __name__ == "__main__":
    main()
