import psycopg2
from secrets import Secrets


def store_passwords(password, user_email, username, url, app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO accounts (password, email, username, url, app_name) VALUES (%s, %s, %s, %s, %s)"""
        record_to_insert = (password, user_email, username, url, app_name)
        print(f'{record_to_insert = }')
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print(error)

def connect():
    try:
        connection = psycopg2.connect(user='postgres', password=Secrets.postgresql_password, host='localhost', database='PasswordManager')
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Couldn't connect")
        print(error)

def find_password(app_name):
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT password FROM accounts WHERE app_name = '""" + app_name + "'"
        cursor.execute(postgres_select_query, app_name)
        connection.commit()
        result = cursor.fetchone()
        cursor.close()
        print('Password is: ' )
        print(result[0])

    except (Exception, psycopg2.Error) as error:
        print(error)
def find_users(user_email):
    data = ('Password: ', 'Email: ', 'Username: ', 'url: ', 'App/Site name: ')
    try:
        connection = connect()
        cursor = connection.cursor()
        postgres_select_query = """ SELECT * FROM accounts WHERE email = '""" + user_email + "'"
        cursor.execute(postgres_select_query, user_email)
        connection.commit()
        result = cursor.fetchall()
        print('')
        print('RESULT')
        print('')
        print(result)
        for row in result:
            for i in range(0, len(row)):
                print(data[i] + row[i])
        print('')
        print('-'*30)
        cursor.close()
    except (Exception, psycopg2.Error) as error:
        print(error)
