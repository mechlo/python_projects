        show_help()

    # make a list to hold onto our items
    shopping_list = []

    while True:
        # ask for new items
        new_item = input("> ")

        # be able to quit the app
        if new_item == 'DONE':
            break
        elif new_item == 'HELP':
            show_help()
            continue
        elif new_item == 'SHOW':
            show_list(shopping_list)
            continue
        add_to_list(shopping_list, new_item)

    show_list(shopping_list)
