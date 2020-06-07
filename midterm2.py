# CIS41A Midterm 2
# Author: Simon Zhang
# 06/01/2020
# This program display the menu, get order from user, compute bill and display it
# use two dictionary to store data, in the manner of object-oriented programming


class Order:
    """Order class, contain five methods including:
    displayMenu, getInputs, calculate, printBill, saveToFile.
    """

    def __init__(self):
        self._priceBtax = 0
        self._priceAtax = 0
        self._tax = 0

        self._priceDict = {"De Anza Burger": 5.25, "Bacon Cheese": 5.75,
                           "Mushroom Swiss": 5.95, "Western Burger": 5.95,
                           "Don Cali Burger": 5.95}

        self._orderDict = {"De Anza Burger": 0, "Bacon Cheese": 0,
                           "Mushroom Swiss": 0, "Western Burger": 0,
                           "Don Cali Burger": 0}

    def displayMenu(self):
        """
        Display the menu of De Anza College food court.
        Choose from 1 to 5, 6 for exit.
        """
        print("\n----------- De Anza Food Court -----------")
        number = 1
        for key in self._priceDict:
            print("{a}. {b:15s} {c:8.2f}".format(a=number, b=key, c=self._priceDict[key]))
            number += 1
        print("6. Exit")

    def getInputs(self):
        """
        Get the burger choice and quantity from user.
        """
        flag1 = True
        while flag1:  # Guardians for burger choice
            try:
                burger_choice = int(input('Enter 1 - 5 to choose burger, or Enter 6 to exit:'))
                if burger_choice < 1 or burger_choice > 6:
                    print('Invalid input!')
                elif burger_choice == 6:
                    flag1 = False
                else:
                    flag2 = True
                    while flag2:  # Guardians for quantity number
                        try:
                            number = int(input('How many do you want?'))
                            if number <= 0:
                                print('Positive integer only!')
                            else:
                                flag2 = False
                        except:
                            print('Positive integer only! Please enter again.')

                    # Now we have valid burger_choice and quantity
                    if burger_choice == 1:
                        self._orderDict["De Anza Burger"] += number
                    elif burger_choice == 2:
                        self._orderDict["Bacon Cheese"] += number
                    elif burger_choice == 3:
                        self._orderDict["Mushroom Swiss"] += number
                    elif burger_choice == 4:
                        self._orderDict["Western Burger"] += number
                    else:
                        self._orderDict["Don Cali Burger"] += number
            except:
                print('Integer only!')

    def calculate(self):
        """
        Calculate the pay, use the two dictionaries above.
        when hours > 40, give 1.5 bonus after 40 hours.
        Student pay no tax, Staff pay 9% tax rate.
        """
        job = int(input('Staff Enter 1, Student Enter 2:'))
        if job == 1:
            self._tax = 0.09

        for key in self._priceDict:
            self._priceBtax += self._orderDict[key] * self._priceDict[key]
            self._priceAtax = self._priceBtax + (self._priceBtax * self._tax)

    def printBill(self):
        """
        Display the bill on the console.
        """
        print("\nYour bill:")

        for key in self._orderDict:
            print(
                " %-20s Qty: %-10d Price: $%-10.2f Total: $%-10.2f" %
                (key, self._orderDict[key], self._priceDict[key], (self._orderDict[key] * self._priceDict[key])))

        print("-" * 50)
        print("Price before tax:", round(self._priceBtax, 2))
        print("Price after tax:", round(self._priceAtax, 2))

    def saveToFile(self):
        """
        use time and datetime module to get the output file name
        """
        import time
        import datetime
        timeStamp = time.time()
        orderTimeStamp = datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H-%M-%S')
        orderTimeStamp = orderTimeStamp + '.txt'

        with open(orderTimeStamp, 'w') as fileHandleToSaveTheBill:
            fileHandleToSaveTheBill.write("Your bill:\n")
            for key in self._orderDict:
                fileHandleToSaveTheBill.write(" %-20s Qty: %-10d Price: $%-10.2f Total: $%-10.2f" %
                                              (key, self._orderDict[key], self._priceDict[key],
                                               (self._orderDict[key] * self._priceDict[key])) + '\n')

            fileHandleToSaveTheBill.write("-" * 50 + '\n')
            fileHandleToSaveTheBill.write("Price before tax:" + str(self._priceBtax) + '\n')
            fileHandleToSaveTheBill.write("Price after tax:" + str(self._priceAtax) + '\n')


"""
----------- De Anza Food Court -----------
1. De Anza Burger      5.25
2. Bacon Cheese        5.75
3. Mushroom Swiss      5.95
4. Western Burger      5.95
5. Don Cali Burger     5.95
6. Exit
Enter 1 - 5 to choose burger, or Enter 6 to exit:ten
Integer only!
Enter 1 - 5 to choose burger, or Enter 6 to exit:6
Staff Enter 1, Student Enter 2:1

Your bill:
 De Anza Burger       Qty: 0          Price: $5.25       Total: $0.00      
 Bacon Cheese         Qty: 0          Price: $5.75       Total: $0.00      
 Mushroom Swiss       Qty: 0          Price: $5.95       Total: $0.00      
 Western Burger       Qty: 0          Price: $5.95       Total: $0.00      
 Don Cali Burger      Qty: 0          Price: $5.95       Total: $0.00      
--------------------------------------------------
Price before tax: 0.0
Price after tax: 0.0
Continue for another order(Any keys= Yes, n= No)?y

----------- De Anza Food Court -----------
1. De Anza Burger      5.25
2. Bacon Cheese        5.75
3. Mushroom Swiss      5.95
4. Western Burger      5.95
5. Don Cali Burger     5.95
6. Exit
Enter 1 - 5 to choose burger, or Enter 6 to exit:1
How many do you want?-9
Positive integer only!
How many do you want?10
Enter 1 - 5 to choose burger, or Enter 6 to exit:5
How many do you want?20
Enter 1 - 5 to choose burger, or Enter 6 to exit:6
Staff Enter 1, Student Enter 2:2

Your bill:
 De Anza Burger       Qty: 10         Price: $5.25       Total: $52.50     
 Bacon Cheese         Qty: 0          Price: $5.75       Total: $0.00      
 Mushroom Swiss       Qty: 0          Price: $5.95       Total: $0.00      
 Western Burger       Qty: 0          Price: $5.95       Total: $0.00      
 Don Cali Burger      Qty: 20         Price: $5.95       Total: $119.00    
--------------------------------------------------
Price before tax: 171.5
Price after tax: 171.5
Continue for another order(Any keys= Yes, n= No)?n
The system is shutting down!

Process finished with exit code 0

"""
