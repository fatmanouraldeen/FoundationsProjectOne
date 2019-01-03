####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Unicorn Cafe"
signature_flavors = ["red velvet", "pharphor", "salted caramel"]
order_list = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]

def print_menu():
    """
    Print the items in the menu dictionary.

    """
    # your code goes here!
    print ("Welcome to %s, my name is Fatma" % cupcake_shop_name)

    print ("Our menu is:")
    l = list(menu.keys())
    i = 0
    while i < len(l):
        print(l[i])
        i += 1

def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    i = 0
    while i < len(original_flavors):
        print(original_flavors[i])
        i += 1

def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    i = 0
    while i < len(signature_flavors):
        print(signature_flavors[i])
        i += 1

def is_valid_order(order): 
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if order in menu or order in signature_flavors or order in original_flavors:
        return True
    else:
       return False
 
def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    print("Please enter your order then type exit to submit.")
    while True:
        order = input()
        if order != 'exit':
            if is_valid_order(order) == True:
                order_list.append(order)
            else: 
                print('not a valid order!')
                continue
        else:
            return order_list



def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5: 
        return True 
    else:
        return False

def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    i = 0
    while i < len(order_list):
        if menu.get(order_list[i]):
            total += menu.get(order_list[i])
        elif order_list[i] in signature_flavors:
            total += signature_price
        else: 
           total += original_price

        i += 1
    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print("Your order is: %s " % order_list)
    # your code goes here!
    print("Your total is %s " % get_total_price(order_list))
    if accept_credit_card(get_total_price(order_list)) == True:
        print("You can pay by Credit Card")
