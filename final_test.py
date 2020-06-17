from order import Order
import csv

if __name__ == "__main__":

    order = Order()

    while True:
        print("\nC:Create \t R:Read \t U:Update \t D:Delete \t X:Exit")
        choice = input("Enter your choice: ")

        if choice.lower() == 'c':
            print('Now creating an order...')
            order.displayMenu()
            order.getInputs()
            order.calculate()
            order.printBill()

        elif choice.lower() == 'r':
            # import os
            #
            # cwd = os.getcwd()  # Get the current working directory (cwd)
            # files = os.listdir(cwd)  # Get all the files in that directory
            # print("Files in %r: %s" % (cwd, files))

            print("Now read the default file (sample_input.csv)...")
            order_read = Order()

            with open("/Users/jingping/Documents/GitHub/CIS41A_midterm1_part1/venv/sample_input.csv") as infile:
                reader = csv.reader(infile)

                for line in reader:
                    index_burger = int(line[0])
                    order_read.burgers[index_burger - 1].quantity = int(line[1])

            order_read.calculate()
            order_read.printBill()

        elif choice.lower() == 'u':
            print("\nBefore update: ")
            order.printBill()
            order.getInputs()
            order.calculate()
            print("\nAfter update: ")
            order.printBill()

        elif choice.lower() == 'd':
            print("Now deleting the order...")
            order = Order()

        elif choice.lower() == 'x':
            break

        else:
            print("Invalid choice!")

    print("\nNow save to file...")
    order.saveToFile()
    print("\nThanks for using, Have a Great Day!")


"""

C:Create 	 R:Read 	 U:Update 	 D:Delete 	 X:Exit
Enter your choice: -9
Invalid choice!

C:Create 	 R:Read 	 U:Update 	 D:Delete 	 X:Exit
Enter your choice: c
Now creating an order...

----------- De Anza Food Court -----------
1. De Anza Burger      5.25
2. Bacon Cheese        5.75
3. Mushroom Swiss      5.95
4. Western Burger      5.95
5. Don Cali Burger     5.95
6. Exit
Enter 1 - 5 to choose burger, or Enter 6 to exit:-9
Invalid input!
Enter 1 - 5 to choose burger, or Enter 6 to exit:1
How many do you want?10
Enter 1 - 5 to choose burger, or Enter 6 to exit:6
Staff Enter 1, Student Enter 2:1

Your bill:
 De Anza Burger       Qty: 10         Price: $5.25       Total: $52.50     
 Bacon Cheese         Qty: 0          Price: $5.75       Total: $0.00      
 Mushroom Swiss       Qty: 0          Price: $5.95       Total: $0.00      
 Western Burger       Qty: 0          Price: $5.95       Total: $0.00      
 Don Cali Burger      Qty: 0          Price: $5.95       Total: $0.00      
--------------------------------------------------
Price before tax: 52.5
Price after tax: 57.23

C:Create 	 R:Read 	 U:Update 	 D:Delete 	 X:Exit
Enter your choice: r
Now read the default file (sample_input.csv)...
Staff Enter 1, Student Enter 2:1

Your bill:
 De Anza Burger       Qty: 1          Price: $5.25       Total: $5.25      
 Bacon Cheese         Qty: 2          Price: $5.75       Total: $11.50     
 Mushroom Swiss       Qty: 3          Price: $5.95       Total: $17.85     
 Western Burger       Qty: 4          Price: $5.95       Total: $23.80     
 Don Cali Burger      Qty: 5          Price: $5.95       Total: $29.75     
--------------------------------------------------
Price before tax: 88.15
Price after tax: 96.08

C:Create 	 R:Read 	 U:Update 	 D:Delete 	 X:Exit
Enter your choice: u

Before update: 

Your bill:
 De Anza Burger       Qty: 10         Price: $5.25       Total: $52.50     
 Bacon Cheese         Qty: 0          Price: $5.75       Total: $0.00      
 Mushroom Swiss       Qty: 0          Price: $5.95       Total: $0.00      
 Western Burger       Qty: 0          Price: $5.95       Total: $0.00      
 Don Cali Burger      Qty: 0          Price: $5.95       Total: $0.00      
--------------------------------------------------
Price before tax: 52.5
Price after tax: 57.23
Enter 1 - 5 to choose burger, or Enter 6 to exit:2
How many do you want?10
Enter 1 - 5 to choose burger, or Enter 6 to exit:6
Staff Enter 1, Student Enter 2:1

After update: 

Your bill:
 De Anza Burger       Qty: 10         Price: $5.25       Total: $52.50     
 Bacon Cheese         Qty: 10         Price: $5.75       Total: $57.50     
 Mushroom Swiss       Qty: 0          Price: $5.95       Total: $0.00      
 Western Burger       Qty: 0          Price: $5.95       Total: $0.00      
 Don Cali Burger      Qty: 0          Price: $5.95       Total: $0.00      
--------------------------------------------------
Price before tax: 162.5
Price after tax: 177.12

C:Create 	 R:Read 	 U:Update 	 D:Delete 	 X:Exit
Enter your choice: d
Now deleting the order...

C:Create 	 R:Read 	 U:Update 	 D:Delete 	 X:Exit
Enter your choice: x

Now save to file...

Thanks for using, Have a Great Day!

Process finished with exit code 0



C:Create 	 R:Read 	 U:Update 	 D:Delete 	 X:Exit
Enter your choice: r
Now read the default file (sample_input.csv)...
Staff Enter 1, Student Enter 2:2

Your bill:
 De Anza Burger       Qty: 1          Price: $5.25       Total: $5.25      
 Bacon Cheese         Qty: 2          Price: $5.75       Total: $11.50     
 Mushroom Swiss       Qty: 3          Price: $5.95       Total: $17.85     
 Western Burger       Qty: 4          Price: $5.95       Total: $23.80     
 Don Cali Burger      Qty: 5          Price: $5.95       Total: $29.75     
--------------------------------------------------
Price before tax: 88.15
Price after tax: 88.15

C:Create 	 R:Read 	 U:Update 	 D:Delete 	 X:Exit
Enter your choice: c
Now creating an order...

----------- De Anza Food Court -----------
1. De Anza Burger      5.25
2. Bacon Cheese        5.75
3. Mushroom Swiss      5.95
4. Western Burger      5.95
5. Don Cali Burger     5.95
6. Exit
Enter 1 - 5 to choose burger, or Enter 6 to exit:1
How many do you want?10
Enter 1 - 5 to choose burger, or Enter 6 to exit:6
Staff Enter 1, Student Enter 2:1

Your bill:
 De Anza Burger       Qty: 10         Price: $5.25       Total: $52.50     
 Bacon Cheese         Qty: 0          Price: $5.75       Total: $0.00      
 Mushroom Swiss       Qty: 0          Price: $5.95       Total: $0.00      
 Western Burger       Qty: 0          Price: $5.95       Total: $0.00      
 Don Cali Burger      Qty: 0          Price: $5.95       Total: $0.00      
--------------------------------------------------
Price before tax: 52.5
Price after tax: 57.23

C:Create 	 R:Read 	 U:Update 	 D:Delete 	 X:Exit
Enter your choice: d
Now deleting the order...

C:Create 	 R:Read 	 U:Update 	 D:Delete 	 X:Exit
Enter your choice: u

Before update: 

Your bill:
 De Anza Burger       Qty: 0          Price: $5.25       Total: $0.00      
 Bacon Cheese         Qty: 0          Price: $5.75       Total: $0.00      
 Mushroom Swiss       Qty: 0          Price: $5.95       Total: $0.00      
 Western Burger       Qty: 0          Price: $5.95       Total: $0.00      
 Don Cali Burger      Qty: 0          Price: $5.95       Total: $0.00      
--------------------------------------------------
Price before tax: 0
Price after tax: 0
Enter 1 - 5 to choose burger, or Enter 6 to exit:1
How many do you want?10
Enter 1 - 5 to choose burger, or Enter 6 to exit:5
How many do you want?20
Enter 1 - 5 to choose burger, or Enter 6 to exit:6
Staff Enter 1, Student Enter 2:1

After update: 

Your bill:
 De Anza Burger       Qty: 10         Price: $5.25       Total: $52.50     
 Bacon Cheese         Qty: 0          Price: $5.75       Total: $0.00      
 Mushroom Swiss       Qty: 0          Price: $5.95       Total: $0.00      
 Western Burger       Qty: 0          Price: $5.95       Total: $0.00      
 Don Cali Burger      Qty: 20         Price: $5.95       Total: $119.00    
--------------------------------------------------
Price before tax: 171.5
Price after tax: 186.94

C:Create 	 R:Read 	 U:Update 	 D:Delete 	 X:Exit
Enter your choice: x

Now save to file...

Thanks for using, Have a Great Day!

Process finished with exit code 0
"""