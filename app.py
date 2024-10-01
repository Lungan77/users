import mysql.connector

def connection():
    try:
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Lungan@7@7',
            database = 'user_management_system'
        )

        print('Database connected')

        return conn
    
    except mysql.connector.Error as error:
        print(f'Connection failed: {error}')


def add(username, email, password, role, registarion_date):
    db = connection()

    cursor = db.cursor()
    sql = 'INSERT INTO users(Username, Email, Password, Role, Registration_date) VALUE(%s, %s, %s, %s, %s)'
    values = (username, email, password, role, registarion_date)

    try:
        cursor.execute(sql, values)
        db.commit()
        print('User added!!!')
    
    except mysql.connector.Error as error:
        print(f'Failed to add user: {error}')
    
    finally:
        db.close()
        cursor.close()

def getUserById(id):
    db = connection()
    r = None

    cursor = db.cursor()
    sql = 'SELECT * FROM users WHERE ID = %s'
    id = (id,)

    try:
        cursor.execute(sql, id)
        print(cursor.fetchone())
        r = cursor.fetchone

    except mysql.connector.Error as error:
        print(f'Failed to retrive a user: {error}')
    
    finally:
        db.close()
        cursor.close()

    return r


def update(id):
    if getUserById(id) == None:
        return

    db = connection()

    cursor = db.cursor()
    
    try:
        prompt = int(input('Enter a number of attribute to update:\n1. Username \n2. Email \n3. Password \n4. Role \n5. To update all\n> '))

        if prompt == 1:
            sql = 'UPDATE users SET Username = %s WHERE ID = %s'
            username = input('Enter a new username: ')
            attr = (username, id)
            cursor.execute(sql, attr)
            print('Username updated')

        elif prompt == 2:
            sql = 'UPDATE users SET Email = %s WHERE ID = %s'
            email = input('Enter a new email: ')
            attr = (email, id)
            cursor.execute(sql, attr)
        
        elif prompt == 3:
            sql = 'UPDATE users SET Password = %s WHERE ID = %s'
            password = input('Enter a new password: ')
            attr = (password, id)
            cursor.execute(sql, attr)
        
        elif prompt == 4:
            sql = 'UPDATE users SET Role = %s WHERE ID = %s'
            role = input('Enter a new role: ')
            attr = (role, id)
            cursor.execute(sql, attr)
        
        elif prompt == 5:
            sql = 'UPDATE users SET Username = %s, Email = %s, Password = %s, Role = %s WHERE ID = %s'
            username = input('Enter a new username: ')
            email = input('Enter a new email: ')
            password = input('Enter a new password: ')
            role = input('Enter a new role: ')

            attr = (username, email, password, role, id)
            cursor.execute(sql, attr)
        
        db.commit()

    except ValueError:
        print(f'Value Error: {ValueError}')

    except mysql.connector.Error as error:
        print(f'Failed to update: {error}')
    
    finally:
        db.close()
        cursor.close()

def delete(id):
    if getUserById(id) == None:
        return
    
    db = connection()
    cursor = db.cursor()

    try:
        sql = 'DELETE FROM users WHERE ID = %s'
        id = (id, )
        cursor.execute(sql, id)
        db.commit()
        print('User deleted')

    except mysql.connector.Error as error:
        print(f'Failed to delete a user: {error}')
    
    finally:
        db.close()
        cursor.close()

def getUserByRole(role):

    db = connection()
    cursor = db.cursor()

    try:
        sql = 'SELECT * FROM users WHERE Role = %s'
        id = (role, )
        cursor.execute(sql, id)
        
        for i in cursor.fetchall():
            print(i)

    except mysql.connector.Error as error:
        print(f'Failed to get the users: {error}')
    
    finally:
        db.close()
        cursor.close()

def getUserByDate(date):
    db = connection()
    cursor = db.cursor()

    try:
        sql = 'SELECT * FROM users WHERE Registration_Date = %s'
        date = (date, )
        cursor.execute(sql, date)
        
        for i in cursor.fetchall():
            print(i)

    except mysql.connector.Error as error:
        print(f'Failed to get the users: {error}')
    
    finally:
        db.close()
        cursor.close()

getUserByDate('2023-04-18')