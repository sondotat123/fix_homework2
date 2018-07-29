chosen_item = input("welcome to our shop, what do you want (C, R, U, D)?")
things = ["T-shirt", "Sweater"]
shop_items = things
if chosen_item == "R":
    print("Our items: ", *shop_items)
if chosen_item == "C":
    new_item = input("Enter new item: ")
    things.append(new_item)
    print("Our items: ", *shop_items)
if chosen_item == "U":
    change_position = int(input("Update position ?"))
    if -2 <= change_position <= 2:
        new_item = input("New item ?")
        things[change_position - 1] = new_item
        print("Our items: ", *shop_items)
    else:
        print("Our shop doesn't have that item to update")
if chosen_item == "D":
    delete_item = int(input("Delete position ?"))
    if -2 <= delete_item <= 2:
        things.pop(delete_item - 1)
        print("Our items: ", *shop_items)
    else:
        print("Our shop doesn't have that item to delete")