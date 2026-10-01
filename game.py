# First Period Rush
# A prompt game about trying to get to class on time.

state = "home"
energy = 3

while state != "late":

    print("\nCurrent state:", state)
    print("Energy:", energy)

    if state == "home":
        choice = input("You are late for school! Do you run or take the bus? ")

        if choice.lower() == "run":
            energy -= 1
            state = "street"
        else:
            state = "bus_stop"

    elif state == "bus_stop":
        choice = input("The bus is taking forever. Wait or walk? ")

        if choice.lower() == "wait":
            state = "bus"
        else:
            energy -= 1
            state = "street"

    elif state == "street":
        choice = input("You see a shortcut through the park. Take it or stay on the sidewalk? ")

        if choice.lower() == "take it":
            energy -= 1
            state = "school"
        else:
            state = "crosswalk"

    elif state == "crosswalk":
        print("You safely cross the street.")
        state = "school"

    elif state == "bus":
        print("The bus finally arrives!")
        state = "school"

    elif state == "school":
        if energy > 0:
            print("You made it to first period just in time!")
            state = "on_time"
        else:
            print("You are completely exhausted and stop to catch your breath.")
            state = "late"

    elif state == "on_time":
        print("ENDING: You made it to class on time!")
        break

print("\nThanks for playing First Period Rush!")
