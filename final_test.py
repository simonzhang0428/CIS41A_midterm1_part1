from order import Order
import csv

if __name__ == "__main__":

    # while True:
    #     order = Order()
    #     order.displayMenu()
    #     order.getInputs()
    #     order.calculate()
    #     order.printBill()
    #     order.saveToFile()
    #
    #     # help(order)
    #
    #     userInputToContinue = input("Continue for another order(Any keys= Yes, n= No)?")
    #
    #     if userInputToContinue.lower() == 'n':
    #         print("The system is shutting down!")
    #         break
    #

    print("C:Create \t R:Read \t U:Update \t D:Delete")
    choice = input("Enter your choice: ")

    order = Order()

    if choice.lower() == 'c':
        print('Now creating an order...')
        order.displayMenu()
        order.getInputs()
        order.calculate()
        order.printBill()

    elif choice.lower() == 'r':
        print("Now read the default file: sample_input.csv")

        with open("sample_input.csv") as infile:
            reader = csv.reader(infile)

            for line in reader:
                index_burger = int(line[0])
                order.burgers[index_burger-1].quantity = line[-1]

        order.calculate()
        order.printBill()


"""
----------- De Anza Food Court -----------
1. De Anza Burger      5.25
1. Bacon Cheese        5.75
1. Mushroom Swiss      5.95
1. Western Burger      5.95
1. Don Cali Burger     5.95
6. Exit
Enter 1 - 5 to choose burger, or Enter 6 to exit:two
Integer only!
Enter 1 - 5 to choose burger, or Enter 6 to exit:2
How many do you want?ten
Positive integer only! Please enter again.
How many do you want?10
Enter 1 - 5 to choose burger, or Enter 6 to exit:5
How many do you want?20
Enter 1 - 5 to choose burger, or Enter 6 to exit:6
Staff Enter 1, Student Enter 2:1

Your bill:
 De Anza Burger       Qty: 0          Price: $5.25       Total: $0.00      
 Bacon Cheese         Qty: 10         Price: $5.75       Total: $57.50     
 Mushroom Swiss       Qty: 0          Price: $5.95       Total: $0.00      
 Western Burger       Qty: 0          Price: $5.95       Total: $0.00      
 Don Cali Burger      Qty: 20         Price: $5.95       Total: $119.00    
--------------------------------------------------
Price before tax: 176.5
Price after tax: 192.38
Continue for another order(Any keys= Yes, n= No)?y

----------- De Anza Food Court -----------
1. De Anza Burger      5.25
1. Bacon Cheese        5.75
1. Mushroom Swiss      5.95
1. Western Burger      5.95
1. Don Cali Burger     5.95
6. Exit
Enter 1 - 5 to choose burger, or Enter 6 to exit:-9
Invalid input!
Enter 1 - 5 to choose burger, or Enter 6 to exit:1
How many do you want?10
Enter 1 - 5 to choose burger, or Enter 6 to exit:4
How many do you want?-9
Positive integer only!
How many do you want?20
Enter 1 - 5 to choose burger, or Enter 6 to exit:6
Staff Enter 1, Student Enter 2:2

Your bill:
 De Anza Burger       Qty: 10         Price: $5.25       Total: $52.50     
 Bacon Cheese         Qty: 0          Price: $5.75       Total: $0.00      
 Mushroom Swiss       Qty: 0          Price: $5.95       Total: $0.00      
 Western Burger       Qty: 20         Price: $5.95       Total: $119.00    
 Don Cali Burger      Qty: 0          Price: $5.95       Total: $0.00      
--------------------------------------------------
Price before tax: 171.5
Price after tax: 171.5
Continue for another order(Any keys= Yes, n= No)?n
The system is shutting down!

Process finished with exit code 0
"""
