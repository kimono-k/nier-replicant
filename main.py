# Text-based game from the Bird Riddle in Nier Replicant
# Source: https://www.youtube.com/watch?v=IdSbDAamNow
print("Thank you for playing this text base adventure game it is based on one of my favorite games Nier Replicant. I hope you enjoy this adventure game with this Python script")
print("Bird: To whom does the true voice speak?\n")
print("Bird: To whom does the true form show itself?\n")
print("Bird: You must answer.\n")
print("Emil: It can talk!\n")
print("Bird: I ask:\n")
print("Bird: Why did humans disappear from the world?")
print("Nier: The hell is this?")
print("Grimoire Weiss: I believe this is some manner of password.")
print("Nier: Password?")
print("Grimoire Weiss: Yes. The correct answer should grant us access to the castle.")
print("Grimoire Weiss: I feel confident I have heard this somewhere before...")
print("Bird: To whom does the true voice speak?")
print("Bird: To whom does the true form show itself?")
print("Bird: I ask:")


question1 = input(
    "Why did humans disappear from the world?' You must answer.\n Because their lives are short.\n Because of a black disease.\n")
question1.lower()

if question1 == "because of a black disease.":
    print("Grimoire Weiss: I answer: Because of a black disease.")  # 1:28
    print("I ask:")
    print("How can humans extend their lives?")
    question2 = input(
        "By acquiring leaves of the sacred tree. \n By separating body from soul.\n")
    question2.lower()
    if question2 == "by separating body from soul.":
        print("Grimoire Weiss: I answer: by separating body from soul.")
        print("I ask: what is a destination of souls?")
        question3 = input(
            "They are placed in their corresponding shells. \n They are in the promised land, bursting with light.\n")
        question3.lower()
        if question3 == "they are placed in their corresponding shells.":
            print("Very well.")
            print("You are acknowledged as a master.")
            print("You may enter.")
            print("Well then! It seems the way is open.")
            print("Congratulations! You finished I hope you android is adventure game with disabled python scripts the game!")
    else:
        print("Access denied please try again.")
else:
    print("Access denied please try again.")
