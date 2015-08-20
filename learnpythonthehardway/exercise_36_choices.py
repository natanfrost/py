

choices_goblin_key = {1: 'pick', 2: 'nah. I think i\'ll go back to the prev room.' }

choices_start_room = {1: 'center',
                      2: 'left',
                      3: 'right'}

choices_bow_chest_room = {1: 'verify portrait.',
                          2: 'verify chest',
                          3: 'go through the door in the left distant corner',
                          4: 'go back to main entrance'}

choices_globlin_encounter = {1: 'crush him with your feet',
                             2: 'scream out loud to see if it run away',
                             3: 'go back to the previous room'}

def get_goblin_key():
    return choices_goblin_key

def get_start_room(arg):
    return choices_start_room

def get_bow_chest_room():
    return choices_bow_chest_room

def get_goblin_encounter():
    return choices_globlin_encounter
