import random
import quick_draw_list
from time import sleep

def quick_draw():

    print("You will guess the population of a random country to the nearest million.\n")

    guesses = 1
    score = 0
    qs = quick_draw_list.quick_draw_list
    random.shuffle(qs)

    for i, qa in enumerate(qs, start=1):
        if i > 5:
            break

        q, a = qa

        if input(q).lower() == a.lower():
            guesses += 1
            score += 1
            print("> Well done.\n")

        else:
            print("> Incorrect. The correct answer is \"{}\".\n".format(a))

    print(f"\nYou scored {score} out of 5.\n".format(quick_draw_list.quick_draw_list)) ; sleep(1)

    print("Let's go back to the first room.") ; sleep(1)
    return 'first_room'
