import main_menu

def courier_menu():
    print('-Courier menu options- Enter 0 to return to Main Menu, Enter 1 to see Couriers, Enter 2 to create new Couriers, Enter 3 to update existing Couriers and Enter 4 to delete a Courier')
    input2 = int(input('Enter option:'))
    if input2 == 0:
        main_menu.main_menu() 
    elif input2 == 1:#print products
        print(main_menu.courier_list)
        courier_menu()
    elif input2 == 2:#make new products
        numb = int(input('how many couriers would you like to add?'))
        for x in range(numb):
            food = str(input('Enter a courier name:'))
            price = int(input('Enter a phone number:'))
            courier_input = {}
            courier_input['name'] = food
            courier_input['price'] = price
            main_menu.courier_list.append(courier_input)
        print(main_menu.courier_list)
        courier_menu()
    elif input2 == 3:#replace/update a product
        for i, value in enumerate(main_menu.courier_list):
            print(i, value)
        # GET user input for order index value
        index = int(input('Pick an product:'))#ensure input is enough
        print('Enter a value to ammend order or enter to skip to next property')
        for key in main_menu.courier_list[index]:
            print(key)
            replace = input(f'{key}:')
            if not replace:
                continue
            else:
                main_menu.courier_list[index][key] = replace
        print(main_menu.courier_list[index])
        courier_menu()
    elif input2 == 4:#delete a product
        for i, cor in enumerate(main_menu.courier_list):
            print(i, cor)
        index = int(input('Enter the number you would like to delete:'))
        main_menu.courier_list.remove(main_menu.courier_list[index])
        print(main_menu.courier_list)
        courier_menu()
    else:
        print('Option not recognised')
        courier_menu()