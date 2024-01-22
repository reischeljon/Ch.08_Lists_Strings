'''
ADVENTURE GAME (4pts)
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
# Game setup
room_list = []
room = ["This is the first room the shuttle bay.", None, None, None, 1]  # Example room directions, modify as needed
room_list.append(room)

room = ["cargo with not many things in here just shipment of Bantha milk", 4, 0, 2, 3]
room_list.append(room)

room = ["power", 1, None, 5, None]
room_list.append(room)

room = ["A place with a clumsy and random blasters behind a protected glass. You perfer your lightsaber for a more civilized age.", 6, 1, None, None]
room_list.append(room)

room = ["walking into the prison a wookie speaks his language. You decipher it as he tells you of a hidden passage leading to the observation room.", None, None, 1, 7]
room_list.append(room)

room = ["the generator room with modern Imperial technology all of it is easily disrupted by a code. How clever.", 2, None, None, None]
room_list.append(room)

room = ["The emperors throne stands a key in the observation room.", None, 7, 3, None]
room_list.append(room)

room = ["the secret passage is filled with dust mites. You would think a probe droid or a mouse droid would clean this by now.", None, 4, None, 6]
room_list.append(room)

inventory = []

current_room = 0
done = False

while not done:
    print()
    print(room_list[current_room][0])

    if current_room == 6 and "code" not in inventory:
        print("You spot a small piece of paper that has a code.")
        answer = input("What do you want to do? (Take or Ignore): ")

        if answer.lower() == "take":
            print("You pick up the key.")
            inventory.append("code")
    else:
        answer = input("Which direction do you want to go? (N, E, W, S, or Q to quit): ")

# Direction North
    if answer.lower() == "n" or answer.lower() == "north":
        next_room = room_list[current_room][1]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room

# Direction East
    if answer.lower() == "e" or answer.lower() == "east":
        next_room = room_list[current_room][2]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room

# Direction South
    if answer.lower() == "s" or answer.lower() == "south":
        next_room = room_list[current_room][3]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room

# Direction West
    if answer.lower() == "w" or answer.lower() == "west":
        next_room = room_list[current_room][4]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room

    elif answer.lower() == "q" or answer.lower() == "quit":
        done = True

    else:
        print("Sorry, I don't understand that input.")

    if current_room == 5 and "code" in inventory:
        print("You entered the generator and shut it of. This will explode the first Death Star and you escaped!")
        done = True
