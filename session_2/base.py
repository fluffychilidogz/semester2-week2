import sqlite3
# you will need to pip install pandas matplotlib
import pandas as pd
import matplotlib as mpl

def get_connection(db_path="orders.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_path)
#    conn.row_factory = sqlite3.Row
    return conn

def First(x):
    '''
    Take database and query
    '''

    query = '''
            SELECT category FROM products JOIN order_items GROUP BY category
            '''
    
    result = x.execute(query)

    written = result.fetchone()

    if written:
        print(written)
    else:
        print('Result not found')


def Second(x):
    '''
    Take database and query
    '''

    query = '''
            SELECT COUNT(customer_id)
            FROM customers;
            '''
    
    result = x.execute(query)

    written = result.fetchone()

    if written:
        print(written)
    else:
        print('Result not found')

def Third(x):
    '''
    Take customer ID (int) and database, then query
    '''

    query = '''
            SELECT orders.order_id, orders.customer_id, orders.order_date, orders.status, orders.total_amount
            FROM orders JOIN customers ON orders.customer_id=customers.customer_id
            WHERE customers.customer_id=?;
            '''
    
    customer_id = input('Enter a customer ID:')

    
    result = x.execute(query, (customer_id,))

    written = result.fetchone()

    if written:
        print(written)
    else:
        print('Result not found')

def Fourth(x):
    '''
    Take price (int) and database, then query
    '''

    query = '''
            SELECT products.name, category, price
            FROM products
            WHERE price<=?;
            '''
    
    price = input('Enter a price:')

    
    result = x.execute(query, (price,))

    written = result.fetchone()

    if written:
        print(written)
    else:
        print('Result not found')



def menu():
    '''
    Print options and return choice (string)
    '''

    print('Please choose from the following options:\n')
    print(f'4 - {task4}')
    print(f'3 - {task3}')
    print(f'2 - {task2}')
    print(f'1 - {task1}')
    print('0 - Exit\n')
    print('What would you like to do? (Enter 0-4)')
    choice = '-1'

    while choice not in ['0','1','2','3','4']:
        choice = input(':')

    return choice


def main():

    db = get_connection()

    while True:
        choice = menu()

        if choice == '0':
            db.close()
            exit()

        elif choice == '1':
            First(db)

        elif choice == '2':
            Second(db)

        elif choice == '3':
            Third(db)

        elif choice == '4':
            Fourth(db)




task1 = 'List all product categories'
task2 = 'Count all customers'
task3 = 'Show all orders of a customer'
task4 = 'Show products that are or below a price'

if __name__=="__main__":
    main()

