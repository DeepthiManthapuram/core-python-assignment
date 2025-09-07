
def addingRemovingMenu(menu_list,add_item,remove_item):
    if(add_item not in menu_list):
        menu_list.append(add_item) #adding item into menu

    if(remove_item in menu_list):
        menu_list.remove(remove_item) #removing item into menu
    return menu_list

def checkingMenu(menu_list,check_item):
    if(check_item in menu_list):            #checking for availability of menu
        return f"{check_item} is available"
    else:
        return f"{check_item} is not available"

menu = eval(input("initial_menu = "))   #converting input into list using eval
add_item = input("add_item = ").strip('"').strip("'")   #removing quotes in input string using strip()
remove_item = input("remove_item = ").strip('"').strip("'")
check_item = input("check_item = ").strip('"').strip("'")


updated_list = addingRemovingMenu(menu,add_item,remove_item)
print("Updated menu: ",updated_list)
print("Availability: ",checkingMenu(updated_list,check_item))
