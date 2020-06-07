from midterm2 import Order

if __name__ == "__main__":

    while True:
        order = Order()
        order.displayMenu()
        order.getInputs()
        order.calculate()
        order.printBill()
        order.saveToFile()

        # help(order)

        userInputToContinue = input("Continue for another order(Any keys= Yes, n= No)?")

        if userInputToContinue.lower() == 'n':
            print("The system is shutting down!")
            break
