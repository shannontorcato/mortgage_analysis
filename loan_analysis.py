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

loan = Loan(2.5, 30, 100000)
print(loan.pmt)