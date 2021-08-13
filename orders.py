import main_menu
import pymysql
import os
from dotenv import load_dotenv

# A cursor is an object that represents a DB cursor,
# which is used to manage the context of a fetch operation.
clear = lambda: os.system('cls')

def orders():
    print("-Orders menu options- \n\t Enter 0 to return to Main Menu \n\t Enter 1 to see Orders \n\t Enter 2 to create new Orders\n\t Enter 3 to update an existing Order's Status \n\t Enter 4 to update an existing Order \n\t Enter 5 to delete an Order")#can this print one after the next
    input2 = int(input('Enter option:'))
    if input2 == 0:
        main_menu.main_menu() 
    elif input2 == 1:#print orders
        clear()
        print('Your orders')
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
        cursor = connection.cursor()### join two tables and print it out##########
        cursor.execute('SELECT order_id, customer_name, customer_address, customer_phone, order_status, products, courier FROM orders AS o JOIN link_it_all AS l ON o.order_id = l.orders')
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        print(column_names)
        if not rows:
            print('Table Empty')
        for row in rows:
            print(row)
        cursor.close()
        # Closes the connection to the DB, make sure you ALWAYS do this
        connection.close()
        orders()
    elif input2 == 2:#make new orders
        clear()
        print('Add a new Order')
        numb = int(input('how many orders would you like to add?'))
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
            courier_index = int(input('Pick an courier_id:'))#ensure input is enough and option to exit if mind changes
            cursor.execute("SELECT courier_id, COUNT(*) FROM courier WHERE courier_id = %s", (courier_index))
            # gets the number of rows affected by the command executed
            row_count = cursor.fetchone()
            check = row_count[0]
            while check == None :
                print ("Pick a valid courier_id")
                courier_index = int(input('Pick an courier_id:'))
                cursor.execute("SELECT courier_id, COUNT(*) FROM courier WHERE courier_id = %s", (courier_index))
                # gets the number of rows affected by the command executed
                row_count = cursor.fetchone()
                check = row_count[0]
            #select product
            cursor.execute('SELECT * FROM products')
            rows = cursor.fetchall()
            column_names = [i[0] for i in cursor.description]
            print(column_names)
            for row in rows:
                print(row)
            numb2 = int(input('how many products would you like to add?'))
            items = []
            for x in range(numb2):
                product_index = int(input('Pick an product_id:'))#ensure input is enough and option to exit if mind changes
                cursor.execute("SELECT product_id, COUNT(*) FROM products WHERE product_id = %s", (product_index))
                # gets the number of rows affected by the command executed
                row_count = cursor.fetchone()
                check = row_count[0]
                while check == None :
                    print ("Pick a valid product_id")
                    product_index = int(input('Pick an product_id:'))
                    cursor.execute("SELECT product_id, COUNT(*) FROM products WHERE product_id = %s", (product_index))
                    # gets the number of rows affected by the command executed
                    row_count = cursor.fetchone()
                    check = row_count[0]
                items.append(product_index)
            #insert into link here
            cursor.execute("SELECT order_id FROM orders WHERE order_id=(SELECT max(order_id) FROM orders)")
            get_id = cursor.fetchone()
            for x in range(numb2):
                cursor.execute("INSERT INTO link_it_all(orders, products, courier) VALUES (%s, %s, %s)", (get_id[0], items[x], courier_index))
                connection.commit()
        cursor.close()
        connection.close()
        print('Orders uploaded')
        orders()
    elif input2 == 3:#update an order status
        clear()
        print('Update Order status')
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
        cursor = connection.cursor()##print the orders
        cursor.execute('SELECT order_id, customer_name, customer_address, customer_phone, order_status FROM orders')
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        print(column_names)
        if not rows:
            print('Table Empty')
        for row in rows:
            print(row)
        change_status = input('Select an order_id to change:')
        cursor.execute("SELECT order_id, COUNT(*) FROM orders WHERE order_id = %s", (change_status))
        # gets the number of rows affected by the command executed
        row_count = cursor.fetchone()
        check = row_count[0]
        while check == None :
            print ("Pick a valid order_id")
            change_status = int(input('Pick an order_id:'))
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
        clear()
        print('Update existing Order')
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
        cursor = connection.cursor()##print the orders
        cursor.execute('SELECT order_id, customer_name, customer_address, customer_phone, order_status FROM orders')
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        print(column_names)
        if not rows:
            print('Table Empty')
        for row in rows:
            print(row)
        change_status = input('Select an order_id to update:')
        cursor.execute("SELECT order_id, COUNT(*) FROM orders WHERE order_id = %s", (change_status))
        # gets the number of rows affected by the command executed
        row_count = cursor.fetchone()
        check = row_count[0]
        while check == None :
            print ("Pick a valid order_id")
            change_status = int(input('Pick an order_id:'))
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
        answer1= input('Enter to skip updating order status or enter 1 to update: ')
        if answer1 == '1':
            select_status(check)
        else:
            pass
        ##change courier
        cursor.execute("SELECT courier, products FROM link_it_all WHERE orders = %s", (check))
        rows = cursor.fetchone()
        courier_index = rows[0]
        items = []
        items.append(rows[1])
        print('Update courier')
        answer3 = input('Enter to skip updating courier or enter 1 to update: ')##if skip courier or product it fails to update because no index
        if answer3 == '1':
            cursor.execute('SELECT * FROM courier')
            rows = cursor.fetchall()
            column_names = [i[0] for i in cursor.description]
            print(column_names)
            for row in rows:
                print(row)
            courier_index = int(input('Pick an courier_id:'))#ensure input is enough and option to exit if mind changes
            cursor.execute("SELECT courier_id, COUNT(*) FROM courier WHERE courier_id = %s", (courier_index))
            # gets the number of rows affected by the command executed
            row_count = cursor.fetchone()
            select = row_count[0]
            while select == None :
                print ("Pick a valid courier_id")
                courier_index = int(input('Pick an courier_id:'))
                cursor.execute("SELECT courier_id, COUNT(*) FROM courier WHERE courier_id = %s", (courier_index))
                # gets the number of rows affected by the command executed
                row_count = cursor.fetchone()
                select = row_count[0]
        else:
            # cursor.execute("SELECT courier FROM link_it_all WHERE orders = %s", (check))
            # rows = cursor.fetchone()
            # courier_index = rows[0]
            # print(rows[0])
            pass
        # update products
        print('Update products')
        answer2 = input('ENTER TO SKIP UPDATING PRODUCTS OR ENTER 1 TO UPLOAD A NEW ORDER OF PRODUCTS WHICH WILL DELETE THE OLD PRODUCTS FOR THIS ORDER: ')
        if answer2 == '1':
            cursor.execute('SELECT * FROM products')
            rows = cursor.fetchall()
            column_names = [i[0] for i in cursor.description]
            print(column_names)
            for row in rows:
                print(row)
            numb2 = int(input('how many products would you like to add?'))
            items = []
            for x in range(numb2):
                product_index = int(input('Pick an product_id:'))#ensure input is enough and option to exit if mind changes
                cursor.execute("SELECT product_id, COUNT(*) FROM products WHERE product_id = %s", (product_index))
                # gets the number of rows affected by the command executed
                row_count = cursor.fetchone()
                select = row_count[0]
                while select == None :
                    print ("Pick a valid product_id")
                    product_index = int(input('Pick an product_id:'))
                    cursor.execute("SELECT product_id, COUNT(*) FROM products WHERE product_id = %s", (product_index))
                    # gets the number of rows affected by the command executed
                    row_count = cursor.fetchone()
                    select = row_count[0]
                items.append(product_index)
            #insert into link here
            for x in range(numb2):
                cursor.execute("INSERT INTO link_it_all(orders, products, courier) VALUES (%s, %s, %s)", (check, items[x], courier_index))
                connection.commit()
            print('Updated!')
        else:
                cursor.execute("DELETE FROM link_it_all WHERE orders = %s", (check))
                cursor.execute("DELETE FROM orders WHERE order_id = %s", (check))
                cursor.execute("INSERT INTO link_it_all(orders, products, courier) VALUES (%s, %s, %s)", (check, items[0], courier_index))
                connection.commit()
                print('Updated!')
        cursor.close()
        # Closes the connection to the DB, make sure you ALWAYS do this
        connection.close()
        orders()
    elif input2 == 5:#delete order
        clear()
        print('Delete Order')
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
        cursor.execute('SELECT * FROM orders')
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        print(column_names)
        if not rows:
            print('Table Empty')
        for row in rows:
            print(row)
        order_index = int(input('Enter the order_id of the row you would like to delete:'))#make sure after each delete it saves and you can delete many e.g. in one command if i delete and come back to delete again without going to main then it doesnt save deleted
        #check if product id exists
        cursor.execute("SELECT order_id, COUNT(*) FROM orders WHERE order_id = %s", (order_index))
        # gets the number of rows affected by the command executed
        row_count = cursor.fetchone()
        check = row_count[0]
        while check == None :#make sure i can exit outside if there isnt a table what can i do
            print ("Pick a valid order_id")
            order_index = int(input('Enter the order_id of the row you would like to delete:'))
            cursor.execute("SELECT order_id, COUNT(*) FROM orders WHERE order_id = %s", (order_index))
            # gets the number of rows affected by the command executed
            row_count = cursor.fetchone()
            check = row_count[0]
        cursor.execute("DELETE FROM link_it_all WHERE orders = %s", (order_index))
        cursor.execute("DELETE FROM orders WHERE order_id = %s", (order_index))
        connection.commit()
        cursor.close()
        # Closes the connection to the DB, make sure you ALWAYS do this
        connection.close()
        print('Deleted')
        orders()
    else:
        print('option not recognised')
        orders()

def select_status(change_status):
        ##select new status
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