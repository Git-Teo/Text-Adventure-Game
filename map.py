from items import *
from people import *

blocks = {
    "party_room": "",
    "comsci_room": "",
    "security_room": "",
    "utility_room": ""
}


room_your_room = {
    "name": "Your room",

    "description":
    """Your once peaceful and comfortable bedroom has been invaded by the thumping sound of bass from a party playing stupidly loud music. 
    Also, having your window ajar has allowed the stench of cigarette smoke to enter your once febreeze fresh room. """,

    "exits": {"south": "West Hallway"},

    "items": [],

    "people": [],

    "locked": False,

    "blocked_text": "",

    "usable_items": []
}

room_chem_room = {
    "name": "Chemistry flatmate's room",

    "description":
    """You stumble into Toby's bedroom, who happens to be a chemistry student.
     A poster of the Periodic Table covers the ceiling as if Toby lays in bed studying it.
     Shelves are full of chemistry joke books, which amuses his poor sense of humour. """,

    "exits":  {"south": "East Hallway"},

    "items": [item_dynamite],

    "people": [toby],

    "locked": False,

    "blocked_text": "",

    "usable_items": []
}

room_comsci_room = {
    "name": "Comsci flatmate's room",

    "description":
    """Storming into Jill's bedroom with rage, you discover that your anti-social computer scientist of a room mate is more of a geek than you originally thought.
    One of the bedroom walls is filled with large computer screens, with wires everywhere, and a self built gaming computer sits on the desk. """,

    "exits": {"west": "East Hallway"},

    "items": [item_hammer],

    "people": [jill],

    "locked": True,

    "blocked_text": "*knock* *knock*, it surprisingly seems like your flat mate has gone out, you notice the lock to the door has an odd pattern",

    "usable_items": [item_heart_key]
}

room_hallway_west = {
    "name": "West Hallway",

    "description":
    """You find yourself in a poorly lit hallway, barely being able to see your hand in front of your face.
     A mosaic of graffiti covers the walls, leading to the cobwebbed window frame at the end of the East part of the hallway. """,

    "exits": {"west": "Kitchen", "south": "Party house", "north": "Your room", "east": "East Hallway"},

    "items": [item_heart_key],

    "people": [maypac],

    "locked": False,

    "blocked_text": "",

    "usable_items": []
}

room_hallway_east = {
    "name": "East Hallway",

    "description":
    """You find yourself in the east part of the poorly lit hallway, barely being able to see your hand in front of your face.
     A mosaic of graffiti continues to cover the walls, leading to the cobwebbed window frame at the end of the corridor. """,

    "exits": {"north": "Chem room", "east": "Comsci room", "west": "West Hallway", "south" : "Street"},

    "items": [item_heart_key],

    "people": [],

    "locked": False,

    "blocked_text": "",

    "usable_items": []
}

room_kitchen = {
    "name": "Kitchen",

    "description":
    """As you force the kitchen door open, which is being held shut by piles of rubbish on the floor, you see that all surfaces are hidden among dirty dishes. """,

    "exits": {"east": "West Hallway"},

    "items": [],

    "people": [],

    "locked": False,

    "blocked_text": "",

    "usable_items": []
}

room_party_house = {
    "name": "Party house",

    "description":
    """Much to your dismay, the scene is worse than you thought. 
    This house has been converted to look like Prism on a Friday night, with strobe lights, huge speakers, a DJ table and a DIY bar.
    There's at least 50 people squeezed into the house, with alcohol spilling over carpets and making all the surfaces sticky underfoot. """,

    "exits": {"north": "West Hallway"},

    "items": [item_vodka],

    "people": [eric, david, sally, my_friends_wall],

    "locked": True,

    "blocked_text": "The guard blocks your way, your not equiped enough",

    "usable_items": []
}

room_street = {
    "name": "Street",

    "description":
    """Amongst the smell of smoke, the laughter from drunken students on nights out echoes in the air. 
    The floor is a sea of broken glass crunching beneath your feet, with cigarette butts sticking to your shoes. """,

    "exits": {"east": "Security office", "south": "Utility room", "north": "East Hallway"},

    "items": [],

    "people": [fluffy],

    "locked": True,

    "blocked_text": "There seems to be a wooden blockade blocking your way out",

    "usable_items": []
}

room_security_office = {
    "name": "Security office",

    "description":
    """Having to shield your eyes on entrance, the security office is filled with the bright light from the surveilance screens, which watch over the Halls of Residence.
    The only sounds you can hear is the buzzing of the tape recorder and the heavy exhale from the sleeping security guard. """,

    "exits": {"west": "Street", "east" : "Utility room"},

    "items": [item_lockpick],

    "people": [],

    "locked": True,

    "blocked_text": "You look through the window and see a security officer 'relaxing', but the door is locked",

    "usable_items": []
}

room_utility_room = {
    "name": "Utility room",

    "description":
    """You end up in a dark, dingy, small damp-smelling utility room.
     The sounds of humming electricals is all you can hear, and all you can see is the flashing LED lights of the control panels.
      """,

    "exits": {"north": "Street", "west" : "Security office"},

    "items": [],

    "people": [],

    "locked": True,

    "blocked_text": "You hear the sound of POWER, but a door blocks your way",

    "usable_items": []
}

rooms = {
    "Your room": room_your_room,
    "West Hallway": room_hallway_west,
    "East Hallway": room_hallway_east,
    "Party house": room_party_house,
    "Comsci room": room_comsci_room,
    "Chem room": room_chem_room,
    "Security office": room_security_office,
    "Utility room": room_utility_room,
    "Street": room_street,
    "Kitchen" : room_kitchen

}
