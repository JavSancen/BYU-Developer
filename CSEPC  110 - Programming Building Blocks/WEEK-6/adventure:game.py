# Decisions Game

game = input("Write PLAY to start: ")

if game.upper() == "PLAY":
    desition1 = input("""    You were in a deep sleep.
    Suddenly you start to open your eyes little by little;
    the ceiling is white, all the room is white; in the corner,
    you can see a computer and a door next to the computer.
    "Do you want to CHECK the computer or OPEN the door to look around? "
    """)

    if desition1.upper() == "CHECK":
        desition2 = input("""
        You feel your body very slowly and weak, but you don't know what is going on; your steps sound on the metallic floor at the end of the hallway; there is a sealed gate. Do you want to TURN to the right hallway or UNLOCK the gate? """)

    elif desition1.upper() == "OPEN":
        desition2 = input("""
        You walk throught the hallway, and you find a big control center
        Do you want to EXPLORE the controls or BACK to the gate?
        """)

        if desition2.upper() == "TURN":
            print("""You enter to the room where you wake up and there SOMEBODY else in the computer trying to understand what is going on.

            """)

        elif desition2.upper() == "UNLOCK":
            print("""An alarm is activated you enter a room with astronaut equipment and there is a countdown because the principal hall will be unlock you have 5 minutes to enter in the custom""")

        elif desition2.upper() == "EXPLORE":
            print("""You find a vitacore of travel to Jupiter""")

        elif desition2.upper() == "BACK":
            print("""You find a old friend and suddenly you remember all, this is an expedition to colonize Jupiter.""")

            if desition2.upper() == "SOMEBODY":
                print("""You walk towards the person and when you see her face is Alika a friend in the Spacial station, you are in a travel to Jupiter and you are there to try colonize the planet and study the life there.""")

        else:
            print("""You start to feel acquainted with this situation and you are trying to remember.""")

    else:
        print("""   You are standing up trying to understand what is going on.
        """)

else:
    print("""You are there sitting down on this unknown place thinking what to do.
    """)

# I show and explain the code to a teammate student, my brother and my wife




