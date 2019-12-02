from mysql.connector import Error, MySQLConnection


try:

    conn = MySQLConnection(host="localhost", database="mysql",
                           user="user_mysql_study", password="rootroot")

    print(conn)

    except Error as e:
        print(e)