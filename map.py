from items import *

room_your_room = {
    "name": "Your room",

    "description":
    """ Players room""",

    "exits": {"south": "Hallway", "east": "Chem room"},

    "items": [item_water]
}

room_chem_room = {
    "name": "Your-roommate-who-studys-Chemistry's room",

    "description":
    """ """,

    "exits":  {"west": "Your room", "east" : "ComSci room"},

    "items": [item_dynamite]
}

room_comsci_room = {
    "name": "Your-roommate-who-studys-computer-science's room",

    "description":
    """ """,

    "exits": {"west": "Chem room"},

    "items": [item_saw]
}

room_hallway = {
    "name": "Hallway",

    "description":
    """ """,

    "exits": {"west": "Kitchen", "south": "Party house"},

    "items": [item_heart_key]
}

room_kitchen = {
    "name": "Kitchen",

    "description":
    """ """,

    "exits": {"east": "Hallway"},

    "items": [item_heart_key]
}

room_party_house = {
    "name": "Party house",

    "description":
    """ """,

    "exits": {"east": "Street"},

    "items": [item_spade_key, item_vodka]
}

room_street = {
    "name": "Street",

    "description":
    """ """,

    "exits": {"east": "Security office"},

    "items": []
}

room_security_office = {
    "name": "Security office",

    "description":
    """ """,

    "exits": {"west": "Street", "east" : "Utility room"},

    "items": [item_club_key]
}

room_utility_room = {
    "name": "Utility room",

    "description":
    """ """,

    "exits": {"east": "Street", "north" : "Security office"},

    "items": []
}

rooms = {
    "Your room": room_your_room,
    "Hallway": room_hallway,
    "Party house": room_party_house,
    "Your-roommate-who-studys-computer-science": room_comsci_room,
    "Your-roommate-who-studys-Chemistry's room": room_chem_room,
    "Security office": room_security_office,
    "Utility office": room_utility_room,
    "Street": room_street,
    "Kitchen" : room_kitchen

}
