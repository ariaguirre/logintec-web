import mysql.connector 


def get_database():
    try:
        connection = mysql.connector.connect(host='localhost', user='root', password='Cubiscan2023')
        print('Succesfully connected to Database.')
    except mysql.connector.Error as error:
        print("Failed connect"(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")