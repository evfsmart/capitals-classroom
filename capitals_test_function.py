import random
import capitals_dictionaries

def african_capitals_test():
    print("\nYou scored {0} out of 5.\n".format(asking_questions(capitals_dictionaries.african_capitals_dictionary)))

def asking_questions(african_capitals_dictionary):

    score = 0
    qs = list(african_capitals_dictionary.items())
    random.shuffle(qs)

    for i, qa in enumerate(qs, start=1):
        if i > 5:
            break

        q, a = qa

        if input(q).lower() == a.lower():
            score += 1
            print("> Correct\n")

        else:
            print("> Incorrect. The correct answer is \"{}\".\n".format(a))


    return score

#######################################

def asian_capitals_test():
    print("\nYou scored {0} out of 5.\n".format(asking_questions(capitals_dictionaries.asian_capitals_dictionary)))

def asking_questions(asian_capitals_dictionary):

    score = 0
    qs = list(asian_capitals_dictionary.items())
    random.shuffle(qs)

    for i, qa in enumerate(qs, start=1):
        if i > 5:
            break

        q, a = qa

        if input(q).lower() == a.lower():
            score += 1
            print("> Correct\n")
        else:
            print("> Incorrect. The correct answer is \"{}\".\n".format(a))

    return score

#######################################

def european_capitals_test():
    print("\nYou scored {0} out of 5.\n".format(asking_questions(capitals_dictionaries.european_capitals_dictionary)))

def asking_questions(european_capitals_dictionary):

    score = 0
    qs = list(european_capitals_dictionary.items())
    random.shuffle(qs)

    for i, qa in enumerate(qs, start=1):
        if i > 5:
            break

        q, a = qa

        if input(q).lower() == a.lower():
            score += 1
            print("> Correct\n")
        else:
            print("> Incorrect. The correct answer is \"{}\".\n".format(a))

    return score

#######################################

def north_american_capitals_test():
    print("\nYou scored {0} out of 5.\n".format(asking_questions(capitals_dictionaries.north_american_capitals_dictionary)))

def asking_questions(north_american_capitals_dictionary):

    score = 0
    qs = list(north_american_capitals_dictionary.items())
    random.shuffle(qs)

    for i, qa in enumerate(qs, start=1):
        if i > 5:
            break

        q, a = qa

        if input(q).lower() == a.lower():
            score += 1
            print("> Correct\n")
        else:
            print("> Incorrect. The correct answer is \"{}\".\n".format(a))

    return score

#######################################

def south_american_capitals_test():
    print("\nYou scored {0} out of 5.\n".format(asking_questions(capitals_dictionaries.south_american_capitals_dictionary)))

def asking_questions(south_american_capitals_dictionary):

    score = 0
    qs = list(south_american_capitals_dictionary.items())
    random.shuffle(qs)

    for i, qa in enumerate(qs, start=1):
        if i > 5:
            break

        q, a = qa

        if input(q).lower() == a.lower():
            score += 1
            print("> Correct\n")
        else:
            print("> Incorrect. The correct answer is \"{}\".\n".format(a))

    return score

#######################################

def oceania_capitals_test():
    print("\nYou scored {0} out of 5.\n".format(asking_questions(capitals_dictionaries.oceania_capitals_dictionary)))

def asking_questions(oceania_capitals_dictionary):

    score = 0
    qs = list(oceania_capitals_dictionary.items())
    random.shuffle(qs)

    for i, qa in enumerate(qs, start=1):
        if i > 5:
            break

        q, a = qa

        if input(q).lower() == a.lower():
            score += 1
            print("> Correct\n")
        else:
            print("> Incorrect. The correct answer is \"{}\".\n".format(a))

    return score
