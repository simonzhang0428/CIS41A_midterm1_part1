from burger import *


class Order:
    def __init__(self):
        self._priceBtax = 0
        self._priceAtax = 0
        self._tax = 0

        self.b1 = Burger1()
        self.b2 = Burger2()
        self.b3 = Burger3()
        self.b4 = Burger4()
        self.b5 = Burger5()

        self.burgers = [self.b1, self.b2, self.b3, self.b4, self.b5]

    def displayMenu(self):
        """
        Display the menu of De Anza College food court.
        Choose from 1 to 5, 6 for exit.
        """
        print("\n----------- De Anza Food Court -----------")
        number = 1
        for i in range(len(self.burgers)):
            print("{a}. {b:15s} {c:8.2f}".format(a=number, b=self.burgers[i].get_name(), c=self.burgers[i].get_price()))
            i += 1
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
                    self.burgers[burger_choice - 1].set_quantity(number)
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

        for i in range(len(self.burgers)):
            self._priceBtax += self.burgers[i].get_price() * self.burgers[i].get_quantity()
            self._priceAtax = self._priceBtax + (self._priceBtax * self._tax)

    def printBill(self):
        """
        Display the bill on the console.
        """
        print("\nYour bill:")

        for i in range(len(self.burgers)):
            print(
                " %-20s Qty: %-10d Price: $%-10.2f Total: $%-10.2f" %
                (self.burgers[i].get_name(), self.burgers[i].get_quantity(), self.burgers[i].get_price(),
                 (self.burgers[i].get_price() * self.burgers[i].get_quantity())))

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
            for i in range(len(self.burgers)):
                fileHandleToSaveTheBill.write(" %-20s Qty: %-10d Price: $%-10.2f Total: $%-10.2f" %
                                              (self.burgers[i].get_name(), self.burgers[i].get_quantity(),
                                               self.burgers[i].get_price(),
                                               (self.burgers[i].get_price() * self.burgers[i].get_quantity())) + '\n')

            fileHandleToSaveTheBill.write("-" * 50 + '\n')
            fileHandleToSaveTheBill.write("Price before tax:" + str(round(self._priceBtax, 2)) + '\n')
            fileHandleToSaveTheBill.write("Price after tax:" + str(round(self._priceAtax, 2)) + '\n')

    def create_order(self):
        """
        Create an order
        """
        print('now add an order:')
        self.getInputs()
        self.calculate()
        self.printBill()