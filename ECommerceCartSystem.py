#Function to find the total price of items in a cart
def totalPrice(cart_items):

    total = 0 
    #If cart is empty
    if(len(cart_items) == 0):
        return "Cart is empty"

    #calculating total price
    for value in cart_items.values():
        total += int(value)

    #Applying discount if more than 5 items
    if(len(cart_items) > 5):
        total = total - total * 0.1
    return total

cart_items_dict = eval(input("cart_items = "))
print("Total Price:",totalPrice(cart_items_dict))