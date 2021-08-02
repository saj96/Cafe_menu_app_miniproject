import main_menu
import pymysql
import os
from dotenv import load_dotenv

# A cursor is an object that represents a DB cursor,
# which is used to manage the context of a fetch operation.

def products_menu():
    print('-Product menu options- Enter 0 to return to Main Menu, Enter 1 to see Products, Enter 2 to create new Products, Enter 3 to update existing products and Enter 4 to delete a product')
    input2 = int(input('Enter option:'))
    if input2 == 0:
        main_menu.main_menu() 
    elif input2 == 1:#print products
        # Load environment variables from .env file
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
        cursor.execute('SELECT * FROM products')
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        print(column_names)
        for row in rows:
            print(row)
        cursor.close()
        # Closes the connection to the DB, make sure you ALWAYS do this
        connection.close()
        products_menu()
    elif input2 == 2:#make new products
        numb = int(input('how many products would you like to add?'))
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
            food = str(input('Enter a product name:'))
            price = float(input('Enter a price:'))
            cursor.execute("INSERT INTO products(product_name, price) VALUES (%s, %s)", (food, price))
            connection.commit()
        cursor.close()
        products_menu()
    elif input2 == 3:#replace/update a product
        # for i, value in enumerate(main_menu.products_list):
        #     print(i, value)
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
        # GET user input for order index value
        cursor.execute('SELECT * FROM products')
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        print(column_names)
        for row in rows:
            print(row)
        print(len(rows))
        index = int(input('Pick an product_id:'))#ensure input is enough
        cursor.execute("SELECT product_id, COUNT(*) FROM products WHERE product_id = %s", (index))
        # gets the number of rows affected by the command executed
        row_count = cursor.fetchone()
        print(row_count[0])
        check = row_count[0]
        while check == None :
            print ("Pick a valid product_id")
            index = int(input('Pick an product_id:'))
            cursor.execute("SELECT product_id, COUNT(*) FROM products WHERE product_id = %s", (index))
            # gets the number of rows affected by the command executed
            row_count = cursor.fetchone()
            print(row_count[0])
            check = row_count[0]
        change = int(input('To change: product_name press 1, price press 2, Both press 3:'))
        while 0 < change > 4:
            change = int(input('To change: product_name press 1, price press 2, Both press 3:'))
        if change == 1:
            substitute = input('Enter new product_name:')
            cursor.execute("UPDATE products SET product_name = %s WHERE product_id = %s", (substitute, check))
            connection.commit()
        elif change == 2:
            substitute = input('Enter new price:')
            cursor.execute("UPDATE products SET price = %s WHERE product_id = %s", (substitute, check))
            connection.commit()
        elif change == 3:
            substitute = input('Enter new product_name:')
            substitute2 = input('Enter new price:')
            cursor.execute("UPDATE products SET product_name = %s, price = %s WHERE product_id = %s", (substitute, substitute2, check))
            connection.commit()
        # print('Enter a value to ammend order or enter to skip to next property')
        # for key in main_menu.products_list[index]:
        #     print(key)
        #     replace = input(f'{key}:')
        #     if not replace:
        #         continue
        #     else:
        #         main_menu.products_list[index][key] = replace
        # print(main_menu.products_list[index])
        cursor.close()
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