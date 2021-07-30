import main_menu

def orders():
    print("-Orders menu options- Enter 0 to return to Main Menu, Enter 1 to see Orders, Enter 2 to create new Orders, Enter 3 to update an existing Order's Status, Enter 4 to update an existing Order and 5 to delete an Order")
    input2 = int(input('Enter option:'))
    if input2 == 0:
        main_menu.main_menu() 
    elif input2 == 1:#print orders
        # for i in main_menu.orders_list:
        #     print(i)
        print(main_menu.orders_list)
        orders()
    elif input2 == 2:#make new orders
        name = str(input('Please enter your name?'))
        address = str(input('Please enter your address?'))
        phone = int(input('Please enter your phone number?'))
        print('Pick a courier')
        for i, cor in enumerate(main_menu.courier_list):
            print(i, cor)
        index = int(input('Pick courier:'))#change so u cant enter more than the number of couriers
        order = {}
        order['name'] = name
        order['address'] = address
        order['phone'] = phone
        order['courier'] = index
        order['Order status'] = 'Preparing'
        order['items'] = []
        print('Product stock')
        print(main_menu.products_list)
        select_products = int(input('How many products would you like to add?'))
        for prod in range(select_products):
            print('Product IDs')
            for i, value in enumerate(main_menu.products_list):
                print(i, value)
            add_product = input('Choose a product ID to add:')
            order['items'].append(add_product)
        main_menu.orders_list.append(order)
        orders()
    elif input2 == 3:#update an order status
        for i, value in enumerate(main_menu.orders_list):
            print(i, value)
        index = int(input('Pick an order:'))#ensure input is enough
        print(main_menu.orders_list[index]['Order status'])
        for i, value in enumerate(main_menu.order_status):
                print(i, value)
        index2 = int(input('Pick a Status:'))
        main_menu.orders_list[index]['Order status'] = main_menu.order_status[index2]
        print(main_menu.orders_list[index]['Order status'])
        orders()
    elif input2 == 4:#update existing order
        # PRINT orders list with its index values
        print('Orders')
        for i, value in enumerate(main_menu.orders_list):
            print(i, value)
        # GET user input for order index value
        index = int(input('Pick an order:'))#ensure input is enough if i just press enter it fails
        print('Enter a value to ammend order or enter to skip to next property')
        for key in main_menu.orders_list[index]:
            if key == 'items':
                print('Select new items')
                print('Product stock')
                print(main_menu.products_list)
                select_products = input('Enter number of products to add or enter to skip')
                new_list = []
                if not select_products:
                    continue
                else:
                    select_products = int(select_products)
                    for prod in range(select_products):
                        print('Product IDs')
                        for i, value in enumerate(main_menu.products_list):
                            print(i, value)
                        add_product = input('Choose a product ID to add:')
                        new_list.append(add_product)
                    main_menu.orders_list[index]['items'] = new_list
            elif key == 'Order status':
                print('Select a Order status or press enter to skip')
                for i, value in enumerate(main_menu.order_status):
                    print(i, value)
                index2 = input('Pick an Order Status:')
                if not index2:
                        continue
                else:
                    index2 = int(index2)
                    main_menu.orders_list[index]['Order status'] = main_menu.order_status[index2]
            elif key == 'courier':
                print('Pick a courier or Enter to skip')
                for i, cor in enumerate(main_menu.courier_list):
                    print(i, cor)
                index3 = input('Pick courier:')
                if not index3:
                        continue
                else:
                    index3 = int(index3)
                    main_menu.orders_list[index]['courier'] = index3
            else:
                replace = input(f'{key}:')
                if not replace:
                    continue
                else:
                    main_menu.orders_list[index][key] = replace
        print(main_menu.orders_list[index])
        orders()
    elif input2 == 5:#delete order
        for i, value in enumerate(main_menu.orders_list):
            print(i, value)
        index = int(input('Enter the number you would like to delete:'))
        main_menu.orders_list.remove(main_menu.orders_list[index])
        print(main_menu.orders_list)
        orders()
    else:
        print('option not recognised')
        orders()