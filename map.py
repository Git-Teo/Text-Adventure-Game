from items import *
from people import *

room_your_room = {
    "name": "Your room",

    "description":
    """Your once peaceful and comfortable bedroom has been invaded by the thumping sound of bass from a party playing stupidly loud music. 
    Also, having your window ajar has allowed the stench of cigarette smoke to enter your once febreeze fresh room. """,

    "exits": {"south": "Hallway", "east": "Chem room"},

    "items": [],

    "people": []
}

room_chem_room = {
    "name": "Chemistry flatmate's room",

    "description":
    """You stumble into Toby's bedroom, who happens to be a chemistry student.
     A poster of the Periodic Table covers the ceiling as if Toby lays in bed studying it.
     Shelves are full of chemistry joke books, which amuses his poor sense of humour. """,

    "exits":  {"west": "Your room", "east" : "ComSci room"},

    "items": [item_dynamite],

    "people": []
}

room_comsci_room = {
    "name": "Comsci flatmate's room",

    "description":
    """Storming into Jill's bedroom with rage, you discover that your anti-social computer scientist of a room mate is more of a geek than you originally thought.
    One of the bedroom walls is filled with large computer screens, with wires everywhere, and a self built gaming computer sits on the desk. """,

    "exits": {"west": "Chem room", "south": "Hallway"},

    "items": [item_saw],

    "people": []
}

room_hallway = {
    "name": "Hallway",

    "description":
    """You find yourself in a poorly lit hallway, barely being able to see your hand in front of your face.
     A mosaic of graffiti covers the walls, leading to the cobwebbed window frame at the end of the corridor. """,

    "exits": {"west": "Kitchen", "south": "Party house"},

    "items": [item_heart_key],

    "people": []
}

room_kitchen = {
    "name": "Kitchen",

    "description":
    """As you force the kitchen door open, which is being held shut by piles of rubbish on the floor, you see that all surfaces are hidden among dirty dishes. """,

    "exits": {"east": "Hallway"},

    "items": [],

    "people": []
}

room_party_house = {
    "name": "Party house",

    "description":
    """Much to your dismay, the scene is worse than you thought. 
    This house has been converted to look like Prism on a Friday night, with strobe lights, huge speakers, a DJ table and a DIY bar.
    There's at least 50 people squeezed into the house, with alcohol spilling over carpets and making all the surfaces sticky underfoot. """,

    "exits": {"east": "Street"},

    "items": [item_spade_key, item_vodka],

    "people": []
}

room_street = {
    "name": "Street",

    "description":
    """Amongst the smell of smoke, the laughter from drunken students on nights out echoes in the air. 
    The floor is a sea of broken glass crunching beneath your feet, with cigarette butts sticking to your shoes. """,

    "exits": {"east": "Security office"},

    "items": [],

    "people": []
}

room_security_office = {
    "name": "Security office",

    "description":
    """Having to shield your eyes on entrance, the security office is filled with the bright light from the surveilance screens, which watch over the Halls of Residence.
    The only sounds you can hear is the buzzing of the tape recorder and the heavy exhale from the sleeping security guard. """,

    "exits": {"west": "Street", "east" : "Utility room"},

    "items": [item_club_key],

    "people": []
}

room_utility_room = {
    "name": "Utility room",

    "description":
    """You end up in a dark, dingy, small damp-smelling utility room.
     The sounds of humming electricals is all you can hear, and all you can see is the flashing LED lights of the control panels.
      """,

    "exits": {"east": "Street", "north" : "Security office"},

    "items": [],

    "people": []
}

rooms = {
    "Your room": room_your_room,
    "Hallway": room_hallway,
    "Party house": room_party_house,
    "Comsci room": room_comsci_room,
    "Chem room": room_chem_room,
    "Security office": room_security_office,
    "Utility room": room_utility_room,
    "Street": room_street,
    "Kitchen" : room_kitchen

}
