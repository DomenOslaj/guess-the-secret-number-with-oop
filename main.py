import random
import json
import datetime


class Result:
    def __init__(self, attempts, player_name, date, guess):
        self.attempts = attempts
        self.player_name = player_name
        self.date = date
        self.guess = guess


def play_game():
    name = input("I want to save you name, score and secret number. Could you tell me you name? ")
    secret = random.randint(1, 10)
    attempts = 0
    time = datetime.datetime.now()
    current_time = time.strftime("%A " "%d-" "%m-" "%Y  " "%H:" "%M:" "%S")
    score_list = get_score_list()

    wrong_guesses = get_wrong_guesses_list()

    while True:

        guess = int(input("Please guess the secret number between 1 and 10: "))

        attempts += 1    # += adds a number to a variable, changing the variable itself in the process

        if guess == secret:
            print("Congratulations! Secret number is number " + str(secret) + ".")
            print("Attempts needed: {0}" .format(attempts))    # format method to join 2 strings

            result_obj = Result(attempts=attempts, player_name=name, date=current_time, guess=guess)
            score_list.append(result_obj.__dict__)

            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))
            break  # break the loop

        elif guess > 10:
            print("Choose number between 1 and 10!")

        elif guess > secret:
            print("Your guess is not correct. Try something smaller.")

        elif guess < secret:
            print("Your guess is not correct. Try something bigger.")

        result_obj_wrong = Result(player_name=name, attempts=attempts, guess=guess, date=current_time, )
        wrong_guesses.append(result_obj_wrong.__dict__)

        with open("wrong_guesses_list.txt", "w") as wrong_guesses_file:
            wrong_guesses_file.write(json.dumps(wrong_guesses))


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


def get_wrong_guesses_list():
    with open("wrong_guesses_list.txt", "r") as wrong_guesses_file:
        wrong_guesses_list = json.loads(wrong_guesses_file.read())
        return wrong_guesses_list


# run a game
while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, C) see all attempts, "
                      "D) See wrong guesses, E) quit? ")

    if selection.upper() == "A":
        play_game()
    elif selection.upper() == "B":
        for score_dict in get_top_scores():
            result_obj = Result(attempts=score_dict.get("attempts"),
                                player_name=score_dict.get("player_name", "Anonymous"),
                                date=score_dict.get("date"), guess=score_dict.get("guess"))

            print("Player: {0}, Attempts: {1}, Date: {2}".format(result_obj.player_name, result_obj.attempts,
                                                                 result_obj.date))

    elif selection.upper() == "C":
        for score_dict in get_score_list():
            print(score_dict)
        for score_dict in get_wrong_guesses_list():
            print(score_dict)

    elif selection.upper() == "D":
        for score_dict in get_wrong_guesses_list():
            result_obj_wrong = Result(attempts=score_dict.get("attempts"),
                                player_name=score_dict.get("player_name", "Anonymous"),
                                date=score_dict.get("date"), guess=score_dict.get("guess"))

            print("Player: {0}, Wrong guess: {1}, Date: {2}".format(result_obj_wrong.player_name,
                                                                         result_obj_wrong.guess, result_obj_wrong.date))

        break

    elif selection.upper() == "E":
        print("Bye")
        break

    else:
        print("Don't understand you. Use only A, B, C, D, E")