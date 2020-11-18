import random
import json
import datetime


def play_game():
    name = input("I want to save you name, score and secret number. Could you tell me you name? ")
    secret = random.randint(1, 10)
    attempts = 0
    time = datetime.datetime.now()
    current_time = time.strftime("%A " "%d-" "%m-" "%Y  " "%H:" "%M:" "%S")
    score_list = get_score_list()

    wrong_guesses = []

    while True:
        guess = int(input("Please guess the secret number between 1 and 10: "))

        attempts += 1    # += adds a number to a variable, changing the variable itself in the process

        if guess == secret:
            print("Congratulations! Secret number is number " + str(secret) + ".")
            print("Attempts needed: {0}" .format(attempts))    # format method to join 2 strings

            score_list.append({"attempts": attempts, "date": current_time, "name": name, "secret": secret,
                               "wrong guesses": wrong_guesses})

            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))
            break  # break the loop

        elif guess > 10:
            print("Choose number between 1 and 10!")

        elif guess > secret:
            print("Your guess is not correct. Try something smaller.")

        elif guess < secret:
            print("Your guess is not correct. Try something bigger.")

        # if guess != secret
        wrong_guesses.append(guess)


# return all scores
def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


# return top 3
def get_top_scores():
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]
    return top_score_list


# run a game
while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, C) see all attempts, "
                      "D) See wrong guesses, E) quit? ")

    if selection.upper() == "A":
        play_game()
    elif selection.upper() == "B":
        for score_dict in get_top_scores():
            print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
    elif selection.upper() == "C":
        for score_dict in get_score_list():
            print(score_dict)
    elif selection.upper() == "D":
        for score_dict in get_score_list():
            print(str("Wrong guesses: " + str(score_dict["wrong guesses"])))
        break
    elif selection.upper() == "E":
        print("Bye")
        break
    else:
        print("Don't understand you. Use only A, B, C, D, E")