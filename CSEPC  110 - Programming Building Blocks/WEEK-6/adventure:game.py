game = input("Write PLAY to start: ")

if game.upper() == "PLAY":
    print("""    You were in a deep sleep.
    Suddenly you start to open your eyes little by little;
    the ceiling is white, all the room is white; in the corner,
    you can see a computer and a door next to the computer.
    """)
else:
    print("""   You are there sit down on this unknown place thinking what to do.
    """)

desition1 = input("Do you want to CHECK the computer or OPEN the door to look around?")

if desition1.upper() == "CHECK":
    input("""
    You feel your body very slowly and weak, but you don't know what is going on; your steps sound on the metallic floor at the end of the hallway; there is a sealed gate. Do you want to TURN to the right hallway or UNLOCK the gate?""")

elif desition1.upper() == "OPEN":
    input("""
    You walk throught the hallway, and you find a big control center
    Do you want to EXPLORE the controls or BACK to the gate?
    """)

else:
    print("""   You are stand up trying to understand what is going on.
    """)

