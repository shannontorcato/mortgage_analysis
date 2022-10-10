import datetime as dt
from dateutils import month_start, relativedelta
import matplotlib.pyplot as plt
import numpy_financial as npf
import pandas as pd

class Loan:
    def __init__(self, rate, term, loan_amount, start=dt.date.today().isoformat()):
        self.rate = rate/1200
        self.periods = term*12
        self.loan_amount = loan_amount
        self.start = month_start(dt.date.fromisoformat(start)) + dt.timedelta(31)
        self.pmt = npf.pmt(self.rate, self.periods, -self.loan_amount)
        self.pmt_str = f"${self.pmt:,.2f}"
        self.table = self.loan_table()
    
    def loan_table(self):
        periods = [self.start + relativedelta(months=x) for x in range(self.periods)]
        interest = [npf.ipmt(self.rate, month, self.periods, -self.loan_amount)
                    for month in range(1, self.periods + 1)]
        principal = [npf.ppmt(self.rate, month, self.periods, -self.loan_amount)
                    for month in range(1, self.periods + 1)]
        table = pd.DataFrame({'Payment':self.pmt,
                              'Interest':interest,
                              'Principal': principal}, index=pd.to_datetime(periods))
        table['Balance'] = self.loan_amount - table['Principal'].cumsum()
        return table.round(2)
    
    def plot_balances(self):
        amort = self.table
        plt.plot(amort.Balance, label='Balance')
        plt.plot(amort.Interest.cumsum(), label='Interest')
        plt.grid(axis='y', alpha = .5)
        plt.legend(loc = 8)
        plt.show()
    
    def summary(self):
        amort = self.table
        print("Summary")
        print('-'*30)
        print(f'Payment: {self.pmt_str:>21}')
        print(f'{"Payoff Date:":19} {amort.index.date[-1]}')
        print(f'Total Interest:{amort.Interest.cumsum()[-1]:15,.2f}')

    def extra_pmt(self, extra_amt):
        return (npf.nper(self.rate, self.pmt+extra_amt, -self.loan_amount)/12).round(2)
    
    def retire_debt(self, years_to_payoff):
        extra_pmt = 1
        while npf.nper(self.rate, self.pmt+extra_pmt, -self.loan_amount)/12 > years_to_payoff:
            extra_pmt+=1
        return extra_pmt, self.pmt.round(2)+extra_pmt

loan = Loan(5.88, 20, 360000)
print(loan.table)
#loan.plot_balances()
#print(loan.retire_debt(10))
loan.summary()