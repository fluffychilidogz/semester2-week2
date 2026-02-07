import sqlite3
import pandas as pd
import matplotlib as mpl

def get_connection(db_path="orders.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def First(x):
    # Print all categories
    query = '''
            SELECT category FROM products JOIN order_items GROUP BY category
            '''
    result = x.execute(query)
    print('')

    if result:
        for a in result:
                print(f'Category: {a[0]}')         
    else:
        print('Result not found')
    
    print('')

def Second(x):
    # Print total number of customers
    query = '''
            SELECT COUNT(customer_id)
            FROM customers;
            '''
    result = x.execute(query)
    
    for a in result:
        print(f'\nTotal: {a[0]}\n')

def Third(x):
    # Take customer ID (int) and database, then query
    # Print Order ID, Customer ID, Order Date, Order Status and Total Price
    query = '''
            SELECT orders.order_id, orders.customer_id, orders.order_date, orders.status, orders.total_amount
            FROM orders JOIN customers ON orders.customer_id=customers.customer_id
            WHERE customers.customer_id=?;
            '''
    customer_id = input('Enter a customer ID:')
    result = x.execute(query, (customer_id,))
    print('')

    if result:
        for a in result:
                print(f'Order ID: {a[0]}\tCustomer ID: {a[1]}\tOrder Date: {a[2]}\tOrder Status: {a[3]}\tTotal Amount: {a[4]}')
    else:
        print('Result not found')

    print('')

def Fourth(x):
    # Take price (int) and database, then query
    # Print Product name, Category and Price
    query = '''
            SELECT products.name, category, price
            FROM products
            WHERE price<=?;
            '''
    price = input('Enter a price:')
    result = x.execute(query, (price,))
    print('')

    if result:
        for a in result:
                print(f'Product Name: {a[0]}\nCategory: {a[1]}\tPrice: {a[2]}\n')
    else:
        print('Result not found')

    print('')

def menu():
    '''
    Print options and return choice (string)
    '''
    print('Please choose from the following options:\n')
    print(f'4 - Show products that are or below a price')
    print(f'3 - Show all orders of a customer')
    print(f'2 - Count all customers')
    print(f'1 - List all product categories')
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

if __name__=="__main__":
    main()

