my_itens = []

choice_goblin_key = {1: 'pick', 2: 'nah. I think i\'ll go back to the prev room.' }

choices_start_room = {1: 'center',
                      2: 'left',
                      3: 'right'}

choices_bow_chest_room = {1: 'verify portrait.',
                          2: 'verify chest',
                          3: 'go through the door in the left distant corner'}

choices_globlin_encounter = {1: 'crush him with your feet',
                             2: 'scream out loud to see if it run away',
                             3: 'go back to the previous room',
                             4: 'previous room'}

bow_chest_room_trap = True
goblin_dead = False 

def goblin_room():
    if goblin_dead:
        goblin_killed()

    print_goblin()
    while True:
        answer = int(raw_input(print_choices(choices_globlin_encounter)))
        # allow player to exit if he came back to this room
        if answer != 3:
            try:
                del choices_globlin_encounter[answer]
            except:
                invalid(answer)
        if answer == 1:
            goblin_killed()
        elif answer == 2:
            dead('When you start yelling, a horde of goblins start entering the room, attaking and dilacerate you and you die.')
        elif answer == 3:
            start(True)

def invalid(operation):
    print 'Invalid operation: %s. Try again, motherfucker.' % operation

def print_key():
    print """
    -----------------------------------------------------
    |You made a huge mess with your foot. But thats ok, |
    |the goblin's body parts is all over the floor!     |
    |Behind were the goblin was, you now can see a      |
    |shiny golden key. Do you pick it up or leave there?|
    |                                                   |
    |            ooo,    .---.                          |
    |           o`  o   /    |\________________         |
    |          o`   'oooo()  | ________   _   _)        |
    |          `oo   o` \    |/        | | | |          |
    |            `ooo'   `---'         "-" |_|          |
    |                                       hjw         |
    |                    [GOLDEN KEY]                   |
    -----------------------------------------------------
    """

def print_goblin():
    print """
    -------------------------------------------------------------------
    | You face a furious (very little) goblin.                        |
    | He is too small that acually you could crush him with your foot.|
    | What do you do?                                                 |
    -------------------------------------------------------------------

                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
    """

def goblin_killed():
    print_key()

    answer = int(raw_input(print_choices(choice_goblin_key)))

    remove_option(answer, choice_goblin_key)

    if answer == 1:
        my_itens.append('GOLDEN KEY')
        print 'You got the GOLDEN KEY'
        print 'Since there is nothing more in this room, you have to go back to the previous one.'
        del choices_start_room[2] # 'close' the entering of this room after go back
        start(True)
    elif answer == 2:
        start(True)

def print_choices(choices):
    formated_choices = ''
    for k, v in choices.items():
        formated_choices += "%s: %s\n" % (k, v)
    return formated_choices + '>'

def remove_option(option, choices_list):
    try:
        del choices_list[option]
    except:
        invalid(option)

def bow_chest_room():
    print '----------------------------------------------------------------'
    print "In this room there is a %s." % ','.join(choices_bow_chest_room)
    print '----------------------------------------------------------------'
    while True:
        answer = int(raw_input(print_choices(choices_bow_chest_room)))

        remove_option(answer, choices_bow_chest_room)

        if answer == 2:
            if not bow_chest_room_trap and 'GOLDEN KEY' in my_itens:
                print 'You just used you GOLDEN KEY and discarded it'
                print 'Congratulations, you just found the DEMON BOW OF ETERNITY!'
                my_itens.remove('GOLDEN KEY')
                tip('Keys are excenssial to go on in this game. You can open chests, doors and maybe a gate to hell.')
                my_itens.append('DEMON BOW OF ETERNITY')

                del choices_bow_chest_room[2]
            elif bow_chest_room_trap:
                dead('Arrows came in every direction and pierce all your vital organs. It seems you activate a trap, thats bad.')
            else:
                print "This chest needs a key but you have none. Try to find out where is this key first."
        elif answer == 1:
            choices_bow_chest_room.remove('a portrait')
            bow_chest_room_trap = False
            print "You heard a 'click' and nothing happens. Well, since your alive it is something."
        elif answer == 4:
            start(True)
        elif answer == 3:
            if not bow_chest_room_trap:
                go_to_hall()
            else:
                dead('Arrows came in every direction and pierce all your vital organs. It seems you activate a trap, thats bad.')
        elif answer == "itens":
            show_itens()

def go_to_hall():
    print 'Entered in the Main Hall!'
    exit(0)

def show_itens():
    global my_itens
    print '----------------------------------------------------------------'
    for item in my_itens:
        print item
    print '----------------------------------------------------------------'

def dead(why):
    print '----------------------------------------------------------------'
    print "WASTED!\n", why
    print '----------------------------------------------------------------'
    exit(0)

def tip(tip):
    print '----------------------------------------------------------------'
    print "(tip: %s)" % tip
    print '----------------------------------------------------------------'

def welcome_start(restarted):
    # if the player came back to this room from another
    print '----------------------------------------------------------------'
    if restarted:
        print "You came back to the beggining room and put yourself in the start point that you were here at the very first moment."
    else:
        print "You entered the Valhala Epic Dungeon."
    print '----------------------------------------------------------------'

def verify_start_doors():
    # verify if the player have cleared other doors
    if len(choices_start_room) > 1:
        print "There are %d doors to keep going. One in front of you, one to the right and one to the left." % len(choices_start_room)
        print "Which one do you take?"
    else:
        print "There is just one door left, go ahead."

def start(restarted):
    tip("you can always type 'itens' and see what itens you've got so far.")

    welcome_start(restarted)

    while True:
        choice = int(raw_input(print_choices(choices_start_room)))

        if choice == 2:
            goblin_room()
        elif choice == 3:
            bow_chest_room()
        elif choice == 1:
            dead("You stumble around the room until you starve.")
        elif choice == "itens":
            show_itens()

start(False)
