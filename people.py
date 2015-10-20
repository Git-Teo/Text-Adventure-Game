from items import *

#chemistry student (dynamite)
toby = {
    "name": "toby",

    "description": 
    """ A typical mad scienctist look with hair like Ablert Einstein,
    who wears a lab coat 24/7. Toby is the blackmarket of chemicals
    and explosives.""",

    "speech": "Oh hey there Yu, how's it going? Do you need anything?? *Wink wink*",

    "items": [item_dynamite, item_vodka],

    "take": False,

    "item_used_speech": "Good Call!",

    "usable_items": [item_phone]
}

#antisocial roommate comscience
jill = {
    "name": "jill",

    "description":
    """ Jill is as silent as silent night, doesn't really speak to anyone. 
    She spends most of her time reading comic books and watching Friends and How I
     Met Your Mother. Aside from that, she knows her stuff about computers.""",

    "speech": "It's you again Yu, what is it now? take what you want and leave.",

    "items": [item_hammer],

    "take": False,

    "item_used_speech": "",

    "usable_items": []
}

#party people 1
eric = {
    "name": "eric",

    "description":
    """ If you look up party in a dictionary, you'd see his face.""",

    "speech": "Everyday I'm shuffling!!!!",

    "items": [],

    "take": False,

    "item_used_speech": "",

    "usable_items": []
}


#party people 2
david = {
    "name": "david",

    "description":
    """ David A.K.A the alcoholic. He basically drinks and
    gets drunk every week, last person you would want to 
    play drinking games with. """,

    "speech": "Hmmmm??? Whhaaat?? *Hiccup* ",

    "items": [],

    "take": False,

    "item_used_speech": "",

    "usable_items": []
}

#party people 3
sally = {
    "name": "sally",

    "description":
    """ Sally is medical student, she's friendly, loves to socialize and meeting new people. Sometiems 
    maybe a little too enthusiastic and a little weird.""",

    "speech": "HI YOU!!!!! COME JOIN THE PARTY!!!",

    "items": [item_brain],

    "take": False,

    "item_used_speech": "",

    "usable_items": []
}

#guard to the party
maypac = {
    "name": "maypac",

    "description":
    """ Tough guy, big in size and looks like he could knock anyone out
    with a single punch.""",

    "speech": "Did you bring any drinks?",

    "items": [],

    "take": False,

    "item_used_speech": "",

    "usable_items": [item_vodka]
}

#zombie
fluffy = {
    "name": "fluffy",

    "description":
    """Well, he's a zombie. Before he was turned, he was a thief.""",

    "speech": "Brrraaaaiinnnnssss, BBBRRaaaaIINNSss",

    "items": [item_key],

    "take": False,

    "item_used_speech": "",

    "usable_items": []
}

my_friends_wall = {
    "name": "wall",

    "description":
    """There seems to be brittle.""",

    "speech": "Hello Im a Wall please dont hurt me!",

    "items": [],

    "take": False,

    "item_used_speech": "For the night's watch! *honorable death*",

    "usable_items": [item_hammer]
}




everyone = {
	"toby" : toby,
	"fluffy" : fluffy,
    "jill" : jill,
    "eric" : eric,
    "david" : david,
    "sally" : sally,
    "maypac" : maypac,
    "wall" : my_friends_wall
}
