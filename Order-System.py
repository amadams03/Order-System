"""Stage2.py Developed by Team 5
Austin Adams, Alex Frye, Claire Ke, Alex Ma, Justin Sialm

This is an inventory and order management application developed by Team 5. It maintains 
a product catalog with items like shirts, pants, and hats, each with a specific price and stock 
quantity. Customers and managers can log in using their IDs and passwords, where customers 
can place orders for products, and their orders are tracked with unique order IDs. Managers 
have additional capabilities to view all orders, edit product prices, and reorder inventory.
"""

#globals
current_order_id = 10000    # order ID begins at 10001
customer_id = 0             # keeps track of current user's customer ID to add to dictionary
manager_id = 0              # keeps track of current user's manager ID to add to dictionary

products = {

    101: {'Product': 'Shirts', 'Price': 10.0, 'Stock': 2000},
    102: {'Product': 'Pants', 'Price': 15.0, 'Stock': 2000},
    103: {'Product': 'Hats', 'Price': 5.5, 'Stock': 2000} 
}

orders = {}

customers = {
  1: {'Password': 'ABC'},
  2: {'Password': 'DEF'}
}

managers = {
  3: {'Password': 'XYZ'}
}

#functions
def compute_order(quantity, product_id):
    global products
    price = products[product_id]['Price']
    stock = products[product_id]['Stock']
    if stock == 0:
        print('The item you are looking for is out of stock.')
        return
    else:
        while quantity > stock:
            print('There is not enough stock.') 
            print('Please enter -1 to cancel the order')
            quantity = int(input('Or enter in a new number of the amount you want to order >> '))

            while quantity <= 0:
                if quantity == -1:
                    print('Going back to menu.')
                    return 
                    
                print('Invalid quantity. Please enter a positive quantity.')
                quantity = int(input('>> '))
                
    total = price * quantity
    stock -= quantity
    products[product_id]['Stock'] = stock
    return total


def compute_date():
    import random
    from datetime import datetime, timedelta
    start_date = datetime(2022,1,1)
    end_date = datetime(2023,12,31)

    time_between = end_date - start_date
    days_between = time_between.days

    random_num_days = random.randrange(days_between)
    random_date = start_date +timedelta(days = random_num_days)
    
    return random_date

def submit():
    global current_order_id, orders, products, customer_id

    line = '='*34
    print(line)
    print(f'|{"ID":^10s}|{"Product":^10s}|{"Price":^10s}|')
    print(line)
    for id in products: 
        name = products[id]['Product']
        price = products[id]['Price']
        print(f'|{id:^10d}|{name:^10s}|{price:^10.2f}|')
        print(line)

    product_id = int(input('Enter product ID  >> '))
    while product_id not in products:
        print('Invalid product ID')
        product_id = int(input('Please put in a valid product ID >> '))
    quantity = int(input('How many? > '))
    if quantity <= 0:
        print('No order placed.')
        return
    if product_id in products:
        order_total = compute_order(quantity, product_id)
        if order_total is None:
            return
    else:
        print('Invalid product ID')
        return

    #computations
    date_today = compute_date()
    date_s = date_today.strftime('%m/%d/%y')

    #outputs
    if order_total is not None:
        current_order_id += 1
        
        print(date_s)
        print(current_order_id)
        product_name = products[product_id]['Product']
        print(f'Order total is ${order_total:.2f} for {quantity} {product_name:s}')

        orders_details = {}
        orders_details['Order ID'] = current_order_id
        orders_details['Quantity'] = quantity
        orders_details['Products'] = product_name
        orders_details['Product ID'] = product_id
        orders_details['Total Cost'] = order_total
        orders_details['Date'] = date_s
        orders_details['Customer ID'] = customer_id

        orders[current_order_id] = orders_details


def summary():  
   pass
    
def customer_view_orders():
    global orders, customer_id

    if not orders:
        print('No orders found.')
        return

    customer_orders = False

    for order_id in orders:
        if orders[order_id]['Customer ID'] == customer_id:
            customer_orders = True
            break
    if not customer_orders:
        print('No orders found for the logged-in customer.')
        return
    
    line = '=' * 67
    print(line)
    print(f'|{"Order ID":^10s}|{"Date":^10s}|{"Product ID":^10s}|{"Products":^10s}|{"Quantity":^10s}|{"Total Cost":^10s}|')
    print(line)
    for order_id in orders:
        details = orders[order_id]
        if details['Customer ID'] == customer_id:  
            order_number = details['Order ID']
            product_name = details['Products']
            product_id = details['Product ID']
            total_cost = details['Total Cost']
            quantity = details['Quantity']
            date = details['Date']
            print(f'|{order_number:^10d}|{date:^10s}|{product_id:^10d}|{product_name:^10s}|{quantity:^10d}|{total_cost:^10.2f}|')
            print(line)

#Managers viewing orders
def manager_view_orders():
    global orders, customer_id

    if not orders: 
        print('No orders found.')
        return 

    line = '=' * 69
    print(line)
    print(f'|{"Customer ID":^12s}|{"Order ID":^10s}|{"Products":^10s}|{"Product ID":^10s}|{"Total Cost":^10s}|{"Date":^10s}|')
    print(line)
    for order_id in orders:
        details = orders[order_id]
        customer_id = details['Customer ID']
        order_number = details['Order ID']
        product_name = details['Products']
        product_id = details['Product ID']
        total_cost = details['Total Cost']
        date = details['Date']
        print(f'|{customer_id:^12d}|{order_number:^10d}|{product_name:^10s}|{product_id:^10d}|{total_cost:^10.2f}|{date:^10s}|')
        print(line)
    
def summary_data():
    pass 

#edit prices
def display_manager_info():
    global products
    line = '='*45
    print(line)
    print(f'|{"ID":^10s}|{"Product":^10s}|{"Price":^10s}|{"Stock":^10s}|')
    print(line)
    for id in products: 
        name = products[id]['Product']
        price = products[id]['Price']
        stock = products[id]['Stock']
        print(f'|{id:^10d}|{name:^10s}|{price:^10.2f}|{stock:^10d}|')
        print(line)
        

def edit_prices():
    global products
    
    while not quit:
        print('Below is a table with all of the current information about the items')
        display_manager_info()
        print('1. Edit Prices    2. Quit')
        action = int(input('Choose 1 or 2 >> '))
        if action == 1:
            print('Enter the product ID and the new price.')
            product_id = int(input('Product ID: '))
            new_price = float(input('New Price: '))
            if product_id in products:
                products[product_id]['Price'] = new_price
                print(f"The price of product {product_id} has been updated to ${new_price:.2f}")
                print('Here is the updated table')
                display_manager_info()
                print('\n\n\n')
            else:
                print('Invalid product ID')
        else:
            break
    
def reorder_inventory():
    global products 
    
    while not quit:
        print('Below is a table with all of the current information about the items')
        display_manager_info()
        print('1.  Order Inventory        2. Quit')
        selection= int(input('Please pick 1 or 2>>>  '))
        if selection == 1:
            print('Enter the product ID and reorder quantity.')
            product_id = int(input('Enter product ID: '))
            inv_order = int(input('How much? > '))
            if product_id in products:
                products[product_id]['Stock'] += inv_order
            else:
                print('Invalid Product ID')
                return
            print(f'Manager has reordered {inv_order:d} {products[product_id]["Product"]}.')
        else: 
            break
            
#main
quit = False
while not quit:
  print('1. Login   2. Quit')
  action = int(input('Choose 1 or 2 >> '))
  if action == 1:
    id = int(input('Enter ID > '))
    #validate ID is in the dictionary:
    while id in customers or id in managers:
          password = input('Enter password > ')
          if id in customers and password == customers[id]['Password']:
              customer_id = id
              break
          elif id in managers and password == managers[id]['Password']:
              manager_id = id
              break
          else:
              print('Incorrect password')
    else:
          print('Invalid ID')

    if id in customers:  # if id is found in 'customer' dictionary:
      while True: #screen 2a "customer screen"
        print('1.Submit Order 2.Display Orders 3.Logout')
        choice = int(input('Choose 1,2, or 3 >> '))
        if choice == 1:
            submit()
        elif choice == 2:
            customer_view_orders()
        elif choice == 3:
            print('Successfully logged out')
            break


    elif id in managers:  # if id is found in 'manager' dictionary:
      while True: #screen 2b "manager screen"
        print('1.View All Orders 2.Summary Data 3. Edit Prices 4.Reorder inventory 5.Logout')
        choice = int(input('Choose 1,2,3,4, or 5 >> '))
        if choice == 1:
            manager_view_orders()
        elif choice == 2:
            summary_data()
        elif choice == 3:
            edit_prices()
        elif choice == 4:
            reorder_inventory()
        elif choice == 5:
            print('Successfully logged out')
            break

  elif action == 2:
    quit = True
    print('Goodbye!')
  else:
    print('Invalid choice')
