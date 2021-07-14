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
        numb = int(input('how many products would you like to add?'))
        for x in range(numb):
            food = input('Enter a product name:')
            main_menu.courier_list.append(food)
        print(main_menu.courier_list)
        courier_menu()
    elif input2 == 3:#replace/update a product
        for i, cor in enumerate(main_menu.courier_list):
            print(i, cor)
        index = int(input('Enter:'))
        replace = input('what would you like to update this with ?')
        main_menu.courier_list[index] = replace
        print(main_menu.courier_list)
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