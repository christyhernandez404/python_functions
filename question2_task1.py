def list():
    items = []
    while True:
        item = input("Input an item to add it to the list:")
        items.append(item)
        check_in = input("Would you like to add more items? Y/N: ")
        if check_in != 'Y':
            print(f"This is your updated list: {items}")
            break


list()
