import main_menu
import pymysql
import os
from dotenv import load_dotenv

#sql injections
clear = lambda: os.system('cls')
def courier_menu():
    print('-Courier menu options-\n\t Enter 0 to return to Main Menu \n\t Enter 1 to see Couriers \n\t Enter 2 to create new Couriers \n\t Enter 3 to update existing Couriers \n\t Enter 4 to delete a Courier')
    input2 = int(input('Enter option:'))
    if input2 == 0:
        main_menu.main_menu() 
    elif input2 == 1:#print couriers
        clear()
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
        cursor.execute('SELECT * FROM courier')
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        print(column_names)
        if not rows:
            print('table empty')
        for row in rows:
            print(row)
        cursor.close()
        # Closes the connection to the DB, make sure you ALWAYS do this
        connection.close()
        courier_menu()
    elif input2 == 2:#make new courier
        clear()
        numb = int(input('how many couriers would you like to add?'))
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
            courier_name = str(input('Enter a courier name:'))
            phone_no = input('Enter a phone number:')
            cursor.execute("INSERT INTO courier(courier_name, phone) VALUES (%s, %s)", (courier_name, phone_no))
            connection.commit()
        cursor.close()
        connection.close()
        courier_menu()
    elif input2 == 3:#replace/update a courier
        clear()
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
        cursor.execute('SELECT * FROM courier')
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        print(column_names)
        if not rows:
            print('Table Empty')
        for row in rows:
            print(row)
        index = int(input('Pick an courier_id:'))#ensure input is enough and option to exit if mind changes
        cursor.execute("SELECT courier_id, COUNT(*) FROM courier WHERE courier_id = %s", (index))
        # gets the number of rows affected by the command executed
        row_count = cursor.fetchone()
        check = row_count[0]
        while check == None :
            print ("Pick a valid courier_id")
            index = int(input('Pick an courier_id:'))
            cursor.execute("SELECT courier_id, COUNT(*) FROM courier WHERE courier_id = %s", (index))
            # gets the number of rows affected by the command executed
            row_count = cursor.fetchone()
            check = row_count[0]
        change = int(input('To change: courier_name press 1, phone_no press 2, Both press 3:'))
        while 0 < change > 4:
            change = int(input('To change: courier_name press 1, phone_no press 2, Both press 3:'))
        if change == 1:
            substitute = input('Enter new courier_name:')
            cursor.execute("UPDATE courier SET courier_name = %s WHERE courier_id = %s", (substitute, check))
            connection.commit()
        elif change == 2:
            substitute = input('Enter new phone_no:')
            cursor.execute("UPDATE courier SET phone = %s WHERE courier_id = %s", (substitute, check))
            connection.commit()
        elif change == 3:
            substitute = input('Enter new courier_name:')
            substitute2 = input('Enter new phone_no:')
            cursor.execute("UPDATE courier SET courier_name = %s, phone = %s WHERE courier_id = %s", (substitute, substitute2, check))
            connection.commit()
        cursor.close()
        connection.close()
        courier_menu()
    elif input2 == 4:#delete a courier
        clear()
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
        cursor.execute('SELECT * FROM courier')
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        print(column_names)
        if not rows:
            print('Table Empty')
        for row in rows:
            print(row)
        index = int(input('Enter the courier_id of the row you would like to delete:'))#make sure after each delete it saves and you can delete many e.g. in one command if i delete and come back to delete again without going to main then it doesnt save deleted
        #check if product id exists
        cursor.execute("SELECT courier_id, COUNT(*) FROM courier WHERE courier_id = %s", (index))
        # gets the number of rows affected by the command executed
        row_count = cursor.fetchone()
        check = row_count[0]
        while check == None :#make sure i can exit outside if there isnt a table what can i do
            print ("Pick a valid courier_id")
            index = int(input('Enter the courier_id of the row you would like to delete:'))
            cursor.execute("SELECT courier_id, COUNT(*) FROM courier WHERE courier_id = %s", (index))
            # gets the number of rows affected by the command executed
            row_count = cursor.fetchone()
            check = row_count[0]
        cursor.execute("DELETE FROM courier WHERE courier_id = %s", (index))
        connection.commit()
        cursor.close()
        # Closes the connection to the DB, make sure you ALWAYS do this
        connection.close()
        courier_menu()
    else:
        print('Option not recognised')
        courier_menu()