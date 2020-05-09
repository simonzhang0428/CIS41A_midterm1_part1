def display_menu():
    print('\n#######MENU#######')
    burgers = {'1 De Anza Burger': 5.25, '2 Bacon Cheese': 5.75, '3 Mushroom Swiss': 5.95,
               '4 Western Burger': 5.95, '5 Don Cali Burger': 5.95}
    for name, price in burgers.items():
        print(name, price)


def get_order():
    print('\n#######ORDER#######')
    choice = input('Enter 1 - 5 to choose burger, or Enter 6 to exit:')
    # if choice != 6:
    #     try:
    #         if int(choice) == 1:
    #             return
    print('End of order')


def main():
    display_menu()
    get_order()


main()
