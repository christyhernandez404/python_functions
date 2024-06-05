def list():
    items = []
    while True:
        check_in = input(
            "Would you like to add or remove items to your list or niether? add/remove/neither: ")
        if check_in == 'add':
            item = input("Input an item to add it to the list:")
            items.append(item)
        elif check_in == 'remove':
            item = input("Input an item to remove from  the list:")
            items.remove(item)
        else:
            print(f"This is your updated list: {items}")
            break


list()
