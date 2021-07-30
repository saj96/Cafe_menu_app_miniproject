import main_menu

def products_menu():
    print('-Product menu options- Enter 0 to return to Main Menu, Enter 1 to see Products, Enter 2 to create new Products, Enter 3 to update existing products and Enter 4 to delete a product')
    input2 = int(input('Enter option:'))
    if input2 == 0:
        main_menu.main_menu() 
    elif input2 == 1:#print products
        print(main_menu.products_list)
        products_menu()
    elif input2 == 2:#make new products
        numb = int(input('how many products would you like to add?'))
        for x in range(numb):
            food = str(input('Enter a product name:'))
            price = float(input('Enter a price:'))
            product_input = {}
            product_input['name'] = food
            product_input['price'] = price
            main_menu.products_list.append(product_input)
        print(main_menu.products_list)
        products_menu()
    elif input2 == 3:#replace/update a product
        for i, value in enumerate(main_menu.products_list):
            print(i, value)
        # GET user input for order index value
        index = int(input('Pick an product:'))#ensure input is enough
        print('Enter a value to ammend order or enter to skip to next property')
        for key in main_menu.products_list[index]:
            print(key)
            replace = input(f'{key}:')
            if not replace:
                continue
            else:
                main_menu.products_list[index][key] = replace
        print(main_menu.products_list[index])
        products_menu()
    elif input2 == 4:#delete a product
        for i, product in enumerate(main_menu.products_list):
            print(i, product)
        index = int(input('Enter the number you would like to delete:'))#make sure after each delete it saves and you can delete many e.g. in one command if i delete and come back to delete again without going to main then it doesnt save deleted
        main_menu.products_list.remove(main_menu.products_list[index])
        print(main_menu.products_list)
        products_menu()
    else:
        print('option not recognised')
        products_menu()