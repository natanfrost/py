my_itens = []
choices_start = ['center', 'left', 'right']

def goblin_room():
    global my_itens, choices_start
    print 'You face a furious (very little) goblin.'
    print 'He is too small that acually you could crush him with your foot...'
    print 'What do you do?'

    choice = raw_input("a) crush him with your feet.\nb) scream out loud to see if it run away\nc) go back to the previous room.\n")

    if choice == "a":
        print 'You made a huge mess with your foot. But thats ok, the goblin is defeated!'
        print 'Behind were the goblin was, you now can see a shiny golden key. Do you pick it up or leave there?'

        choice_2 = raw_input("pick.\nnah\n")
        if choice_2 == 'pick':
            my_itens.append('GOLDEN KEY')
            print 'You got the GOLDEN KEY'
            print 'Since there is nothing more in this room, you have to go back to the previous one.'
            choices_start.remove('left')
            start(True)
    elif choice == "b":
        print 'When you start yelling, a horde of goblins start entering the room and attaking you until you die.'
        dead('Dilacerated by a horde of goblins.')
    elif choice == "c":
        start(True)
    else:
        call_spoodermen()

def bow_chest_room(arg):
    pass

def call_spoodermen():
    print 'don1 no1 pls spodrmen halp.'

def show_itens():
    global my_itens
    for item in my_itens:
        print item

def dead(why):
    print "WASTED!\n", why
    exit(0)

def start(restarted):
    global choices_start

    print "(tips: you can always type 'itens' and see what itens you've got so far.)"

    # if the player came back to this room from another
    if restarted:
        print "You came back to the beggining room and put yourself in the start point that you were here at first."
    else:
        print "You entered the Valhala Epic Dungeon."

    # verify if the player have cleared other doors
    if len(choices_start) > 1:
        print "There are %d doors to keep going. One in front of you, one to the right and one to the left." % len(choices_start)
        print "Which one do you take?"
    else:
        print "There is just one door left, go ahead."

    while True:
        choice = raw_input("> %s?\n" % ','.join(choices_start))

        if choice == "left":
            goblin_room()
        elif choice == "right":
            cthulhu_room()
        elif choice == "center":
            dead("You stumble around the room until you starve.")
        elif choice == "itens":
            show_itens()
        else:
            call_spoodermen()

start(False)
