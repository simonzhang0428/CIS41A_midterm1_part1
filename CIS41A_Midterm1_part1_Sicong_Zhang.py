# CIS41A Midterm 1
# Author: Simon Zhang
# 05/21/2020
# This program display the menu, get order from user, compute bill and display it
# Focus on Software Engineering: Using Functions in a Menu-Driven Program

TAX_RATE = 0.09  # Cupertino, Santa Clara
BURGERS = ('De Anza Burger', 'Bacon Cheese', 'Mushroom Swiss',
           'Western Burger', 'Don Cali Burger')
PRICES = (5.25, 5.75, 5.95, 5.95, 5.95)

quantities = [0, 0, 0, 0, 0]
choice = 0

total_before_tax = 0
tax_amount = 0
total_after_tax = 0

dash = '-' * 40


def display_menu():
    global BURGERS, PRICES
    print(dash)
    for i in range(len(BURGERS)):
        print('{:<5d}{:<25s}{:>10.2f}'.format(i + 1, BURGERS[i], PRICES[i]))


def get_order():
    global quantities, BURGERS, choice
    print(dash)
    flag1 = True
    while flag1:  # Guardians for burger choice
        try:
            choice = int(input('Enter 1 - 5 to choose burger, or Enter 6 to exit:'))
            if not 1 <= choice <= 6:
                print('Invalid choice! Choose between 1 and 6. ')
            elif choice == 6:
                print('End of Order!')
                flag1 = False
            else:
                flag2 = True
                while flag2:  # Guardians for quantity choice
                    try:
                        number = int(input('How many do you want?'))
                        if number < 0:
                            print('Positive integer only!')
                        else:
                            quantities[choice - 1] += number
                            flag2 = False
                    except:
                        print('Positive integer only! Please enter again.')
        except:
            print('Positive Numeric integer only!')
    print(dash)


def compute_bill():
    global PRICES, quantities, total_before_tax, total_after_tax, tax_amount
    for i in range(len(quantities)):
        total_before_tax += quantities[i] * PRICES[i]

    flag3 = True  # Guardians for occupation validation
    while flag3:
        try:
            occupation = int(input('Staff Enter 1, Student Enter 2:'))
            if not (occupation == 1 or occupation == 2):
                print('Choose 1 or 2!')
            elif occupation == 1:  # Staff pay 9% tax
                tax_amount = total_before_tax * TAX_RATE
                total_after_tax = total_before_tax + tax_amount
                flag3 = False
            else:  # Student no tax
                tax_amount = 0
                total_after_tax = total_before_tax
                flag3 = False

        except:
            print('Integer only!')


def print_bill():
    global BURGERS, PRICES, quantities, total_before_tax, total_after_tax, tax_amount
    print(dash)
    for i in range(len(quantities)):
        if quantities[i] != 0:
            print('{:<20s}{:>20s}'.format('Food:', BURGERS[i]))
            print('{:<20s}{:>20d}'.format('Quantities:', quantities[i]))
            print('{:<20s}{:>20.2f}'.format('Cost:', quantities[i] * PRICES[i]))

    print('{:<20s}{:>20.2f}'.format('Total before tax:', total_before_tax))
    print('{:<20s}{:>20.2f}'.format('Tax amount:', tax_amount))
    print('{:<20s}{:>20.2f}'.format('Total after tax:', total_after_tax))
    print(dash)


def main():
    display_menu()
    get_order()
    compute_bill()
    print_bill()


main()

"""
----------------------------------------
1    De Anza Burger                 5.25
2    Bacon Cheese                   5.75
3    Mushroom Swiss                 5.95
4    Western Burger                 5.95
5    Don Cali Burger                5.95
----------------------------------------
Enter 1 - 5 to choose burger, or Enter 6 to exit:ten
Positive Numeric integer only!
Enter 1 - 5 to choose burger, or Enter 6 to exit:-9
Invalid choice! Choose between 1 and 6. 
Enter 1 - 5 to choose burger, or Enter 6 to exit:1
How many do you want?ten
Positive integer only! Please enter again.
How many do you want?10
Enter 1 - 5 to choose burger, or Enter 6 to exit:5
How many do you want?20
Enter 1 - 5 to choose burger, or Enter 6 to exit:-9
Invalid choice! Choose between 1 and 6. 
Enter 1 - 5 to choose burger, or Enter 6 to exit:6
End of Order!
----------------------------------------
Staff Enter 1, Student Enter 2:1
----------------------------------------
Food:                     De Anza Burger
Quantities:                           10
Cost:                              52.50
Food:                    Don Cali Burger
Quantities:                           20
Cost:                             119.00
Total before tax:                 171.50
Tax amount:                        15.43
Total after tax:                  186.94
----------------------------------------
"""
