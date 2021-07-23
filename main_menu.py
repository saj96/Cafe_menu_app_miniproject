#menu
#when it goes to main menu and it reads lines again and appends it to the products list it appends
products_list = []
courier_list = []
orders_list = [{'name': 'sajeevan', 'address': 'bur road ', 'phone': 6789998212, 'courier': 3, 'Order status': 'Preparing'}, {'name': 'nicki ', 'address': 'trinidad', 'phone': 928321, 'courier': 2, 'Order status': 'Preparing'}, {'name': 'doja ', 'address': 'la ', 'phone': 1116623843, 'courier': 0, 'Order status': 'Preparing'}, {'name': 'erykah', 'address': 'space', 'phone': 98347234, 'courier': 1, 'Order status': 'Preparing'}]
order_status = ['Preparing', 'Cooking', 'Out for delivery', 'Delivered', 'Cancelled']
#read and make products list #didn't use with as that will erase the list as a global variable
products_file = None

try:
    products_file = open('products.txt', 'r')
    lines = products_file.readlines()
    for line in lines:
        line = line.strip()
        products_list.append(line)
except Exception as e:
    print('Products.txt could not be opened' + str(e))
finally:
    products_file.close()

#read and make courier_list 
courier_file = None
try:
    courier_file = open('courier.txt', 'r')
    lines = courier_file.readlines()
    for line in lines:
        line = line.strip()
        courier_list.append(line)
except Exception as e:
    print('courier.txt could not be opened' + str(e))
finally:
    courier_file.close()
    
def main_menu():
    #print main menu options
    print('-Main menu options- Enter 0 to Exit, Enter 1 for the Products Menu, Enter 2 for Courier Menu, Enter 3 for Orders')

    input1 = int(input('Enter option:'))
    if input1 == 0:
        #save products into text
        try:
            products_file = open('products.txt', 'w')
            for product in products_list:
                products_file.write("%s\n" % product)
        except Exception as e:
            print('error occured:' + str(e))
        finally:
            products_file.close()
        #save couriers into text
        try:
            courier_file = open('courier.txt', 'w')
            courier_file.write('')
            for courier in courier_list:
                courier_file.write(courier + '\n')
        except Exception as e:
            print('error occured:' + str(e))       
        finally:
            courier_file.close()
        #exit
        exit 
        
    elif input1 == 1:
        from products_menu import products_menu
        products_menu()
    elif input1 == 2:
        from courier_menu import courier_menu
        courier_menu()
    elif input1 == 3:
        from orders import orders
        orders()
    else:
        print('Incorrect submission please enter either 0, 1 or 2')
        main_menu()







