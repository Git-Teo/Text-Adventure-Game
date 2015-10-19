import random, string
random_characters = random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(20)

def drunk():
    if item_vodka["used"] = True:
        print("Oh no, you are very drunk.")
        return True
    else:
        return False

def print_drunk_room(current_room):
    print()
    print(room["name"].upper().join(random_characters))
    print()

    # Display room description
    print(room["description"].join(random_characters))
    print()

    # Print items using previously defined functions
    print_drunk_room_items(room) 

def print_drunk_room_items(room):

    #No items, no output
    if not room["items"]:
        return
    #If items, print in desired format using the list_of_items function
    else:
        s = "There is " + list_of_items(room["items"]) + " here."
        print(s.join(random_characters))
        print("") 

def print_drunk_inventory_items(items):
        #If there are no items, no output
    if not items:
        return
    #Else print items in format using list_of_items
    else:
        s = "You have " + list_of_items(items) + "."
        print(s.join(random_characters))
        print("")

#main loop
        if drunk() == False:
            print_room(current_room)
            print_inventory_items(inventory)
        else:
            print_drunk_room(current_room)
            print_drunk_inventory_items(inventory))

            

