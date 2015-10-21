from items import *
from map import rooms

inventory = [item_phone, item_earplugs, item_vodka, item_brain, item_hammer, item_dynamite]

drunk = False
# Start game at the reception
current_room = rooms["Your room"]

self_usable_items = [item_phone, item_vodka, item_water, item_earplugs]
