#menu
import csv
#when it goes to main menu and it reads lines again and appends it to the products list it appends
products_list = []
courier_list = []
orders_list = []
order_status = ['Preparing', 'Cooking', 'Out for delivery', 'Delivered', 'Cancelled']
#read and make products list #didn't use with as that will erase the list as a global variable
products_file = None

try:
    products_file = open('products.csv', 'r')
    reader = csv.DictReader(products_file)
    for row in reader:
        products_list.append(row)
except Exception as e:
    print('products.csv could not be opened' + str(e))
finally:
    products_file.close()

#read and make courier_list 
courier_file = None
try:
    courier_file = open('courier.csv', 'r')
    reader = csv.DictReader(courier_file)
    for row in reader:
        courier_list.append(row)
except Exception as e:
    print('courier.csv could not be opened' + str(e))
finally:
    courier_file.close()
#open and append orders from csv to list of dict
orders_file = None
try:
    orders_file = open('orders.csv', 'r')
    reader = csv.DictReader(orders_file)
    for row in reader:
        orders_list.append(row)
except Exception as e:
    print('orders.csv could not be opened' + str(e))
finally:
    orders_file.close()
def main_menu():
    #print main menu options
    print('-Main menu options- \n\t Enter 0 to Exit \n\t Enter 1 for the Products Menu \n\t Enter 2 for Courier Menu \n\t Enter 3 for Orders Menu')

    input1 = int(input('Enter option:'))
    if input1 == 0:
        #save products into csv
        if not products_list:
            pass
        else:
            try:
                keys = products_list[0].keys()
                products_file = open("products.csv", "w")
                dict_writer = csv.DictWriter(products_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(products_list)
            except Exception as e:
                print('error occured:' + str(e))       
            finally:
                products_file.close() 
    #save couriers into csv
        if not courier_list:
            pass
        else:
            try:
                keys = courier_list[0].keys()
                courier_file = open("courier.csv", "w")
                dict_writer = csv.DictWriter(courier_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(courier_list)
            except Exception as e:
                print('error occured:' + str(e))       
            finally:
                courier_file.close() 
        #save orders csv
        if not orders_list:
            pass
        else:
            try:
                keys = orders_list[0].keys()
                orders_file = open("orders.csv", "w")
                dict_writer = csv.DictWriter(orders_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(orders_list)
            except Exception as e:
                print('error occured:' + str(e))       
            finally:
                orders_file.close() 
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
        print('Incorrect submission please enter either 0, 1, 2 or 3')
        main_menu()







