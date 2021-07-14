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
            food = input('Enter a product name:')
            main_menu.products_list.append(food)
        print(main_menu.products_list)
        products_menu()
    elif input2 == 3:#replace/update a product
        for i, product in enumerate(main_menu.products_list):
            print(i, product)
        index = int(input('Enter:'))
        replace = input('what would you like to update this with ?')
        main_menu.products_list[index] = replace
        print(main_menu.products_list)
        products_menu()
    elif input2 == 4:#delete a product
        for i, product in enumerate(main_menu.products_list):
            print(i, product)
        index = int(input('Enter the number you would like to delete:'))
        main_menu.products_list.remove(main_menu.products_list[index])
        print(main_menu.products_list)
        products_menu()
    else:
        print('option not recognised')
        products_menu()