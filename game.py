import random, string

from map import rooms
from player import *
from items import *
from gameparser import *
from sys import exit

true_ending = ""

def is_drunk():
    # waiting for using items code to finish
    pass

    #if vodka["used"]:
    #   drunk = True

    #if water["used"] and drunk = true:
    #    drunk = false

def drunk_spelling(s):
    """ This function takes a string and randomly replaces some of 
        the vowels with other vowels. """
    output = ""
    vowels = ["e", "i", "o", "u", "a"]
    for char in s:
        #random.random() returns a random float between 0 and 1
        #so there is a 35% chance of this if being true if the letter is a vowel
        if char in vowels and random.random() < 0.5:
            rand_vowel = random.choice(vowels)

            #makes the new vowel the same case as the old vowel
            if char in string.ascii_uppercase:
                output += rand_vowel.upper()
            else:
                output += rand_vowel
        #if its not a vowel, add it straight to the output
        else: 
            output += char

    return output



def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:
    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'
    >>> list_of_items([item_id])
    'id card'
    >>> list_of_items([])
    ''
    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'
    """
    #Create a list of items
    item_list = ""

    #Iterate through item dictionary
    for item in items:
        #If this is the first item in the list, add it to the list
        if item_list == "":
            item_list = item_list + str(item["name"])
        #If it's not the first item, add it to the list 
        #with a comma and a space before it to get the desired format.
        else:
            item_list = item_list + (", " + str(item["name"]))
    return item_list
        


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:
    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>
    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>
    >>> print_room_items(rooms["Admins"])
    (no output)
    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    #No items, no output
    if not room["items"]:
        return
    #If items, print in desired format using the list_of_items function
    else:
        s = "There is " + list_of_items(room["items"]) + " here."
        if drunk:
            s = drunk_spelling(s)
        print(s)
        print("")
    


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:
    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>
    """
    #If there are no items, no output
    if not items:
        return
    #Else print items in format using list_of_items
    else:
        s = "You have " + list_of_items(items) + "."
        if drunk:
            s = drunk_spelling(s)
        print(s)
        print("")

def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:
    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>
    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>
    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>
    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print("--------------------------------------------------------------------------------")
    print()
    rn = room["name"].upper()
    if drunk:
        rn = drunk_spelling(rn)
    print(rn)
    print()

    # Display room description
    rd = room["description"]
    if drunk:
        rd = drunk_spelling(rd)
    print(rd)
    print()

    # Print items using previously defined functions
    print_room_items(room)



    #
    # COMPLETE ME!
    #

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:
    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:
    GO <EXIT NAME UPPERCASE> to <where it leads>.
    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print
    "TAKE <ITEM ID> to take <item name>."
    and for each item in the inventory print
    "DROP <ITEM ID> to drop <item name>."
    For example, the menu of actions available at the Reception may look like this:
    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?
    """
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for item in room_items:
        print("TAKE " +item["id"].upper()+ " to take " +item["name"])

    for item  in inv_items:
        print("DROP " +item["id"].upper()+ " to drop " +item["name"])

    for person in current_room["people"]:
        print("TALK " +person["name"].upper()+ " to talk to " +person["name"])

    for item in inv_items:
        print("USE " +item["id"].upper()+ " to use " +item["name"])

    print("What do you want to do?")

    # Print take and drop actions   

def print_speech_menu(person, inv):
    talk_input =""
    while True:
        print()
        for item in inv:
            print("GIVE " +item["id"].upper()+ " to give " +item["id"]+ " to " +person["name"])

        for item in person["items"]:
            print("TAKE " +item["id"].upper()+ " to take " +item["name"]+" from " +person["name"])

        for item in inv_items:
            print("USE " +item["id"].upper()+ " to use " +item["name"] + " on " +person["name"])

        print("IGNORE to exit speech")
        print()
        print("What do you want to do?")

        talk_input = input("> ")
        talk_input = normalise_input(talk_input)

        if talk_input[0] == "ignore":
            return
        else:
            execute_command(talk_input, person)




def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:
    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    return chosen_exit in exits

def enough_space(item):
    total = 0
    for i in inventory:
        total += i["mass"]

    if (total+item["mass"] > 10):
        print("You cannot pick up any more items!")
        return False
    else:
        return True

def item_usable(item, where):
    if where == current_room:
        if item in self_usable_items:
            return True
    elif item in where["usable_items"]:
        return True
    else:
        return False



def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """

    global current_room

    if is_valid_exit(current_room["exits"], direction):
        current_room = rooms[current_room["exits"][direction]]
        print("You have moved to " + current_room["name"] + ".")
        print()
    else:
        print("You cannot go there.")
    return


def execute_take(item_id, where):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """

    i = 0
    for item in where["items"]:
        if (item_id == item["id"]):
            if enough_space(item):
                inventory.append(item)
                del where["items"][i]
                print(item_id.upper()+ " has been taken")
                print()
                return
            else:
                print("You cannot take this item, too much weight")
        i += 1

    if where == current_room:
        print(item_id.upper()+ " is not in this room")
    else: 
        print(where["name"]+ " does not have this item")
    return

def execute_drop(item_id, where):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    i = 0
    for item in inventory:
        if item_id == item["id"]:
            where["items"].append(item)
            del inventory[i]
            if where == current_room:
                print(item_id.upper()+ " has been dropped")
                print()
            else:
                print(item_id.upper()+ " has been given to " +where["name"])
                print()
            return
        i += 1
    print(item_id.upper()+ " is not in your inventory")
    return


def execute_talk(person, where):
    for ppl in where["people"]:
        if person == ppl["name"]: 
            print()  
            print(ppl["speech"])
            print_speech_menu(ppl, inventory)
            return

    print(person+ " is not in this room")
    return

def execute_use(item_id, where):
    i=0
    for item in inventory:
        if item_usable(item, where) and item_id == item["id"]:
            item["used"] = where
            del inventory[i]
            if where in everyone:
                print()
                print(where["item_used_speech"])
                print()
            return
        i+=1
    print(item_id.upper()+ " cannot be used as it has no effect")
    return

    

def execute_command(command, where):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.
    """

    if 0 == len(command):
        return
    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1], where)
        else:
            print("Take what?")

    elif command[0] == "drop" or command[0] == "give":
        if len(command) > 1:
            execute_drop(command[1], where)
        else:
            print("Drop what?")

    elif command[0] == "talk" and where == current_room:
        if len(command) > 1:
            execute_talk(command[1], where)
        else:
            print("Talk to who?")

    elif command[0] == "use":
        if len(command) > 1:
            execute_use(command[1], where)
        else:
            print("Use what?")

    elif command[0] == "exit":
        if len(command) == 1:
            exit()
    else:
        print("This makes no sense.")



def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.
    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)
    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:
    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]


def Check_win_condition():
    global true_ending

    if item_dynamite in maypac["items"]:
        print ("dynamite given to guard, everyone blows up (or you could get arrested for having dynamite)")
        return True

    elif current_room == room_utility_room:
        print ("true ending, you turn off power and go to sleep")
        true_ending = True
        return True

    elif current_room == room_security_office and item_dynamite["used"] == "Security office":
        print("tried to use dynamite to blow open door, you blow yourself up")
        return True

    elif current_room == room_security_office and item_saw["used"] == "Security office":
        print("tried to use saw to open door, door was electric and you electrocute youself and die")
        return True

    elif current_room == room_street and (item_saw["used"] == room_street or item_dynamite["used"] == room_street):
        print("you die trying to fight the zombies")
        return True        
    
    elif current_room == room_security_office and item_fluffy in inventory:
        print ("Guard shoots fluffy, you go to jail for having a pet zombie")
        return True



# This is the entry point of our program
def main():

    print("""
88      a8P  88 88          88                 88   ,ad8888ba, 8b        d8  
88    ,88'   88 88          88                 88  d8"'    `"8b Y8,    ,8P   
88  ,88"     88 88          88                 88 d8'        `8b Y8,  ,8P    
88,d88'      88 88          88                 88 88          88  "8aa8"     
8888"88,     88 88          88                 88 88          88   `88'      
88P   Y8b    88 88          88                 88 Y8,        ,8P    88       
88     "88,  88 88          88         88,   ,d88  Y8a.    .a8P     88       
88       Y8b 88 88888888888 88888888888 "Y8888P"    `"Y8888Y"'      88""")

    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        is_drunk()
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command, current_room)
        
        if Check_win_condition():
            break
            if true_ending:
                print("""
                    8b        d8 ,ad8888ba,   88        88    I8,        8        ,8I 88 888b      88  
                     Y8,    ,8P d8"'    `"8b  88        88    `8b       d8b       d8' 88 8888b     88  
                      Y8,  ,8P d8'        `8b 88        88     "8,     ,8"8,     ,8"  88 88 `8b    88  
                       "8aa8"  88          88 88        88      Y8     8P Y8     8P   88 88  `8b   88  
                        `88'   88          88 88        88      `8b   d8' `8b   d8'   88 88   `8b  88  
                         88    Y8,        ,8P 88        88       `8a a8'   `8a a8'    88 88    `8b 88  
                         88     Y8a.    .a8P  Y8a.    .a8P        `8a8'     `8a8'     88 88     `8888  
                         88      `"Y8888Y"'    `"Y8888Y"'          `8'       `8'      88 88      `888 
                                                
                                                """)
            else:
                 print("""____    ____  ______    __    __      __        ______        _______. _______ 
                          \   \  /   / /  __  \  |  |  |  |    |  |      /  __  \      /       ||   ____|
                           \   \/   / |  |  |  | |  |  |  |    |  |     |  |  |  |    |   (----`|  |__   
                            \_    _/  |  |  |  | |  |  |  |    |  |     |  |  |  |     \   \    |   __|  
                              |  |    |  `--'  | |  `--'  |    |  `----.|  `--'  | .----)   |   |  |____ 
                              |__|     \______/   \______/     |_______| \______/  |_______/    |_______|
                                """)


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
