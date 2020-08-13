# Name: Jainamkumar Patel
# Student #: 214 913 396
# Date: 10/11/2017

def madlibs():

    print("MAD LIBS | Vacation Edition")
    print("")

    # A list of nouns, verbs and adjectibes to be used in this MADLIBS!!
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    pluralNoun = input("Enter a plural noun: ")
    game = input("What is your favourite game? ")
    verbING = input("Enter a verb ending in ING: ")
    plant = input("What is your favourite plant? ")
    partOfBody = input("What is your favourite part of the body? ")
    place = input("What is your favourite place to visit? ")
    number = int(input("Please enter a random number: "))

    print("A vacation is when you take a trip to some " + adjective + " place with your " + adjective + "family.")
    print("Usually you go to some place that is near a/an " + noun + "or up on a/an " + noun + ".")
    print("A good vacation place is one where you can ride " + pluralNoun + " or play " + game + " or go hunting for " + pluralNoun + ".")
    print("I like to spend my time " + verbING + " or " + verbING + ".")
    print("When parents go on a vacation, they spend their time eating three " + pluralNoun + " a day, and fathers play gold, and mothers sit around " + verbING + ".")
    print("Last summer, my little brother fell in a/an " + noun + " and poison " + plant + " all over his " + partOfBody + ".")
    print("My family is going to go to (the) " + place + ", and I will practice " + verbING + ".")
    print("Parents need vacations more than kids because parents are always very " + adjective + " and because they have to work " + str(number) + " hours every day all year making enough " + pluralNoun + " to pay for the vacation.")

madlibs()