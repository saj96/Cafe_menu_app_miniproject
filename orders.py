import main_menu
import pymysql
import os
from dotenv import load_dotenv
from prettytable import PrettyTable

clear = lambda: os.system('cls')

def orders():
    print("-Orders menu options- \n\t Enter 0 to return to Main Menu \n\t Enter 1 to see Orders \n\t Enter 2 to create new Orders\n\t Enter 3 to update an existing Order's Status \n\t Enter 4 to update an existing Order \n\t Enter 5 to delete an Order")#can this print one after the next
    input2 = int(input('Enter option:'))
    if input2 == 0:
        main_menu.main_menu() 
    elif input2 == 1:#print orders
        print_orders()
        orders()
    elif input2 == 2:#make new orders
        print('Add a new Order')
        numb = type_check(send = 'how many orders would you like to add?')
        cursor, connection = activate_cursor()
        for x in range(numb):
            print('New Customer')
            cust_name = str(input('Enter customer name:'))
            cust_addr = input('Enter the address:')
            cust_phone = input('Enter phone number:')
            #order status default preparing on database
            #insert into products here
            cursor.execute("INSERT INTO orders(customer_name, customer_address, customer_phone) VALUES (%s, %s, %s)", (cust_name, cust_addr, cust_phone))
            connection.commit()
            #to select courier
            cursor.execute('SELECT * FROM courier')
            rows = cursor.fetchall()
            column_names = [i[0] for i in cursor.description]
            print(column_names)
            for row in rows:
                print(row)
            #ensure input is enough and option to exit if mind changes
            # gets the number of rows affected by the command executed
            courier_index = type_check(send = 'Pick a courier_id:')
            cursor.execute("SELECT courier_id, COUNT(*) FROM courier WHERE courier_id = %s", (courier_index))
            row_count = cursor.fetchone()
            check = row_count[0]
            while check == None :
                print("Pick a valid courier_id")
                courier_index = type_check(send = 'Pick a courier_id:')
                cursor.execute("SELECT courier_id, COUNT(*) FROM courier WHERE courier_id = %s", (courier_index))
                # gets the number of rows affected by the command executed
                row_count = cursor.fetchone()
                check = row_count[0]
            cursor.execute("SELECT order_id FROM orders WHERE order_id=(SELECT max(order_id) FROM orders)")
            get_id = cursor.fetchone()
            cursor.execute("INSERT INTO courier_order(order_id, courier_id) VALUES (%s, %s)", (get_id[0], courier_index))
            connection.commit()
            #select product
            cursor.execute('SELECT * FROM products')
            rows = cursor.fetchall()
            column_names = [i[0] for i in cursor.description]
            print(column_names)
            for row in rows:
                print(row)
            numb2 = type_check(send = 'how many products would you like to add?')
            items = []
            for x in range(numb2):
                product_index = type_check(send = 'Pick a product_id:')
                cursor.execute("SELECT product_id, COUNT(*) FROM products WHERE product_id = %s", (product_index))
                # gets the number of rows affected by the command executed
                row_count = cursor.fetchone()
                check = row_count[0]
                while check == None:
                    print ("Pick a valid product_id")
                    product_index = type_check(send = 'Pick a product_id:')
                    cursor.execute("SELECT product_id, COUNT(*) FROM products WHERE product_id = %s", (product_index))
                    # gets the number of rows affected by the command executed
                    row_count = cursor.fetchone()
                    check = row_count[0]
                items.append(product_index)
            for x in range(numb2):
                cursor.execute("INSERT INTO products_orders(order_id, products) VALUES (%s, %s)", (get_id[0], items[x]))
                connection.commit()
            if numb2 == 0:
                cursor.execute("INSERT INTO products_orders(order_id, products) VALUES (%s, NULL)", (get_id[0]))
                connection.commit()
        cursor.close()
        connection.close()
        if numb != 0:
            print('Orders uploaded')
        orders()
    elif input2 == 3:#update an order status
        print('Update Order status')
        cursor, connection = activate_cursor()##print the orders
        cursor.execute('SELECT order_id, customer_name, customer_address, customer_phone, order_status FROM orders')
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        print(column_names)
        if not rows:
            print('Table Empty')
        for row in rows:
            print(row)
        if rows:
            change_status = type_check(send = 'Select an order_id to change:')
            cursor.execute("SELECT order_id, COUNT(*) FROM orders WHERE order_id = %s", (change_status))
            # gets the number of rows affected by the command executed
            row_count = cursor.fetchone()
            check = row_count[0]
            while check == None :
                print ("Pick a valid order_id")
                change_status = type_check(send = 'Pick an order_id')
                cursor.execute("SELECT order_id, COUNT(*) FROM orders WHERE order_id = %s", (change_status))
                # gets the number of rows affected by the command executed
                row_count = cursor.fetchone()
                check = row_count[0]
            select_status(change_status)
            cursor.close()
            connection.close()
            print('Status Updated')
        orders()
    elif input2 == 4:#update existing order
        # PRINT orders list with its index values
        print('Update existing Order')
    ##print the orders
        print_orders()
        cursor, connection = activate_cursor()
        cursor.execute('SELECT order_id, customer_name, customer_address, customer_phone, order_status, products, courier_id FROM orders AS o JOIN products_orders using (order_id) JOIN courier_order using (order_id)')
        rows = cursor.fetchall()
        if rows:
            change_status = type_check(send = 'Select an order_id to update:')
            cursor.execute("SELECT order_id, COUNT(*) FROM orders WHERE order_id = %s", (change_status))
            # gets the number of rows affected by the command executed
            row_count = cursor.fetchone()
            check = row_count[0]
            while check == None :
                print ("Pick a valid order_id")
                change_status = type_check(send = 'Select an order_id to update:')
                cursor.execute("SELECT order_id, COUNT(*) FROM orders WHERE order_id = %s", (change_status))
                # gets the number of rows affected by the command executed
                row_count = cursor.fetchone()
                check = row_count[0]
            cursor.execute("SELECT order_id, customer_name, customer_address, customer_phone, order_status FROM orders WHERE order_id = %s", (check))
            rows = cursor.fetchall()
            product_dict = {}
            for row in rows:
                product_dict['customer name']= row[1]
                product_dict['address']= row[2]
                product_dict['phone']= row[3]
            for i,j in product_dict.items():
                change = input(f'Press Enter to skip or input new {i}:')
                if not change:
                    continue
                else:
                    product_dict[i] = change
            cursor.execute("UPDATE orders SET customer_name = %s, customer_address = %s, customer_phone = %s WHERE order_id = %s", (product_dict['customer name'], product_dict['address'], product_dict['phone'], check))
            connection.commit()
            print('Update Order Status')
            answer1 = one_enter(send= 'Enter to skip updating order status or enter 1 to update:')
            if answer1 == '1':
                select_status(check)
            print('Update courier')
            answer3 = one_enter(send= 'Enter to skip updating courier or enter 1 to update:')
            if answer3 == '1':
                cursor.execute('SELECT * FROM courier')
                rows = cursor.fetchall()
                column_names = [i[0] for i in cursor.description]
                print(column_names)
                for row in rows:
                    print(row)
                courier_index = type_check(send = 'Pick a courier_id:')
                cursor.execute("SELECT courier_id, COUNT(*) FROM courier WHERE courier_id = %s", (courier_index))
                # gets the number of rows affected by the command executed
                row_count = cursor.fetchone()
                select = row_count[0]
                while select == None :
                    print ("Pick a valid courier_id")
                    courier_index = type_check(send = 'Pick a courier_id:')
                    cursor.execute("SELECT courier_id, COUNT(*) FROM courier WHERE courier_id = %s", (courier_index))
                    # gets the number of rows affected by the command executed
                    row_count = cursor.fetchone()
                    select = row_count[0]
                cursor.execute("UPDATE courier_order SET courier_id = %s WHERE order_id = %s", (courier_index, check))
                connection.commit()
            # update products
            print('Update products')
            answer2 = one_enter(send= 'ENTER TO SKIP UPDATING PRODUCTS OR ENTER 1 TO REPLACE AND UPLOAD PRODUCTS:')
            # answer2 = input('ENTER TO SKIP UPDATING PRODUCTS OR ENTER 1 TO UPLOAD A NEW \n\t SELECTION OF PRODUCTS WHICH WILL DELETE THE OLD PRODUCTS FOR THIS ORDER: ')
            if answer2 == '1':
                cursor.execute('SELECT * FROM products')
                rows = cursor.fetchall()
                column_names = [i[0] for i in cursor.description]
                print(column_names)
                for row in rows:
                    print(row)
                numb2 = type_check(send = 'Enter number of products to add')
                items = []
                for x in range(numb2):
                    product_index = type_check(send = 'Pick an product_id:')
                    cursor.execute("SELECT product_id, COUNT(*) FROM products WHERE product_id = %s", (product_index))
                    # gets the number of rows affected by the command executed
                    row_count = cursor.fetchone()
                    select = row_count[0]
                    while select == None :
                        print ("Pick a valid product_id")
                        product_index = type_check(send = 'Pick an product_id:')
                        cursor.execute("SELECT product_id, COUNT(*) FROM products WHERE product_id = %s", (product_index))
                        # gets the number of rows affected by the command executed
                        row_count = cursor.fetchone()
                        select = row_count[0]
                    items.append(product_index)
                #insert into link here
                if numb2 != 0:
                    cursor.execute("DELETE FROM products_orders WHERE order_id = %s", (check))
                    connection.commit()
                    print('Updated!')
                for x in range(numb2):
                    cursor.execute("INSERT INTO products_orders(order_id, products) VALUES (%s, %s)", (check, items[x]))
                    connection.commit()
                cursor.close()
            # Closes the connection to the DB, make sure you ALWAYS do this
                connection.close()
            elif not answer2:
                cursor.close()
                connection.close()
        orders()
    elif input2 == 5:#delete order
        print('Delete Order')
        print_orders()
        cursor, connection = activate_cursor()
        cursor.execute('SELECT order_id, customer_name, customer_address, customer_phone, order_status, products, courier_id FROM orders AS o JOIN products_orders using (order_id) JOIN courier_order using (order_id)')
        rows = cursor.fetchall()
        if rows:
            order_index = type_check(send = 'Enter the order_id of the row you would like to delete:')
            cursor.execute("SELECT order_id, COUNT(*) FROM orders WHERE order_id = %s", (order_index))
            # gets the number of rows affected by the command executed
            row_count = cursor.fetchone()
            check = row_count[0]
            while check == None :#make sure i can exit outside if there isnt a table what can i do
                print ("Pick a valid order_id")
                order_index = type_check(send = 'Enter the order_id of the row you would like to delete:')
                cursor.execute("SELECT order_id, COUNT(*) FROM orders WHERE order_id = %s", (order_index))
                # gets the number of rows affected by the command executed
                row_count = cursor.fetchone()
                check = row_count[0]
            # cursor.execute("DELETE FROM link_it_all WHERE orders = %s", (order_index))
            cursor.execute("DELETE FROM products_orders WHERE order_id = %s", (order_index))
            cursor.execute("DELETE FROM courier_order WHERE order_id = %s", (order_index))
            cursor.execute("DELETE FROM orders WHERE order_id = %s", (order_index))
            connection.commit()
            cursor.close()
            # Closes the connection to the DB, make sure you ALWAYS do this
            connection.close()
            print('Deleted')
        orders()
    else:
        print('Please pick a valid option')
        orders()
        
def print_orders():
    print('Your orders')
    cursor, connection = activate_cursor()
    cursor.execute('SELECT order_id, customer_name, customer_address, customer_phone, order_status, products, courier_id FROM orders AS o JOIN products_orders using (order_id) JOIN courier_order using (order_id)')
    rows = cursor.fetchall()
    if not rows:
        print('No live orders')
    if rows:
        column_names = [i[0] for i in cursor.description]
        values = []
        # print(rows[1])
        for row in rows:
            values.append(list(row))
            # print(row)
        #print(values)
        mytable = PrettyTable()
        mytable.field_names = column_names
        mytable.add_rows(values)
        print(mytable)
    cursor.close()
    # Closes the connection to the DB, make sure you ALWAYS do this
    connection.close()
    
def type_check(send):
    while True:
        try:
            variable = int(input(f'{send}:'))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return variable
        
def one_enter(send):
    while True:
        variable = input(f'{send}:')
        if variable == '1':
            break
        elif not variable :
            break
        else:
            continue
    return variable
        
def activate_cursor():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )
    cursor = connection.cursor()
    return cursor, connection

def select_status(change_status):
        ##select new status
        # load_dotenv()
        # host = os.environ.get("mysql_host")
        # user = os.environ.get("mysql_user")
        # password = os.environ.get("mysql_pass")
        # database = os.environ.get("mysql_db")
        # # Establish a database connection
        # connection = pymysql.connect(
        #     host,
        #     user,
        #     password,
        #     database
        # )
        # cursor = connection.cursor()
        cursor, connection = activate_cursor()
        for i, value in enumerate(main_menu.order_status):
            print(i, value)
        index = int(input('Pick a Order status:'))#ensure input is enough
        while main_menu.order_status[index] not in main_menu.order_status:
                for i, value in enumerate(main_menu.order_status):
                    print(i, value)
                print('Enter a valid status index: ')
                index = int(input('Pick a status:'))
        cursor.execute("UPDATE orders SET order_status = %s WHERE order_id = %s", (main_menu.order_status[index], change_status))
        connection.commit()
        cursor.close()
        connection.close()