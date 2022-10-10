from loan_analysis import Loan
import sys
from time import sleep

def display_menu():
    print("""
    Menu
    -------------------------
    1. Start a new loan
    2. Show Payment
    3. Show Amortization Table
    4. Show Loan Summary
    5. Plot Balances
    6. Show size of payment to payoff in specific time
    7. Show effect of adding amount to each payment
    8. Change parameter
    9. Exit
    """)

def pmt(loan):
    print(loan.pmt_str)

def amort(loan):
    print(loan.table)

def summary(loan):
    loan.summary()

def plot(loan):
    loan.plot_balances()

def pay_faster(loan):
    yrs = float(input("Enter years to be debt free:"))
    result = loan.retire_debt(yrs)
    print(f"Monthly Extra: ${result[0]}:,.2f\tTotal monthly{result[1]:,.2f}")

def pay_earlier(loan):
    amt = input("Enter monthly extra: ")
    new_term = loan.pay_early(amt)
    print(f"Loan paid of in {new_term}")

def change_selection():
    print("""
    Choose which paramter to change:
    1. Interest Rate
    2. Term
    3. Amount Borrowed
    """)

action = {'2':pmt,'3':amort,'4':summary,'5':plot,'6':pay_faster,'7':pay_earlier}

def main():
    display_menu()
    while True:
        choice = input("Enter a selection from the Menu:")
        if choice == '1':
            rate = float(input('Enter interest rate:'))
            term = int(input('Enter term:'))
            pv = float(input('Enter amount borrowed:'))
            loan = Loan(rate, term, pv)
            print('Loan Initialized')
            sleep(1)
        
        elif choice in '234567':
            try:
                action[choice](loan)
                sleep(1)
            except NameError:
                print('No loan initialized')
                print('Please Initialize Loan By Choosing 1 from Menu')
                sleep(1)
            except KeyError:
                print('Please Initialize Loan By Choosing 1 from Menu')
        elif choice == '8':
            change_selection()
            change_choice = input("Enter a selection to change from the Menu:")
            if change_choice == '1':
                rate = float(input('Enter interest rate:'))
            elif change_choice=='2':
                term = int(input('Enter term:'))
            elif change_choice=='3':
                pv = float(input('Enter amount borrowed:'))
            loan = Loan(rate, term, pv)

        elif choice == '9':
            print('Bye!')
            sys.exit()
        
        else:
            print("Please make a selection")

if __name__ == "__main__":
    main()