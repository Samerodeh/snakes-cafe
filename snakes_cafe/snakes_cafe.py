menu = ["Wings", "Cookies", "Spring Rolls", "Salmon", "Steak", "Meat Tornado", "A Literal Garden", "Ice Cream", "Cake", "Pie", "Coffee", "Tea", "Unicorn Tears"]



print(
    """
    **************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
    """
)  

order = []

def menuist():

    orders = input('>')
    
    while orders != 'quit':
        if orders in menu:
            order.append(orders)
            print(f'** {order.count(orders)} order of {orders} have been added to your meal **')
        else:
            print('Please order from the menu')
        orders = input('>')

if __name__ == '__main__':

    menuist()



