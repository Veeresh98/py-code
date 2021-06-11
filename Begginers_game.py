'''
rock, Paper, Scissor game using simple while loop with if_else statements.
'''
import random  # import randint, it's for computer to choose [Rock, Paper, Scissor] random.
while True:  # using loop, if the condition is true.
    # player input to choose [Rock, Paper, Scissor]
    player = input("choose( r = 'Rock', p = 'Paper',s = 'Scissor')")
    # only available options [Rock, Paper, Scissor].
    possible_actions = ["Rock", "Paper", "Scissor"]
    # with ranndom option it will choose [Rock, Paper, Scissor] any one of them by random order.
    computer = random.choice(possible_actions)
    # if both the players and computer choosen the same gesture then it's draw.
    print(f'if {player} and {computer} are same , match is drawn. ')

    if player == computer:
        print("Both are same, Match is drawn.")
    elif player == "Rock":  # try your input and hope you win agains com.
        if computer == "Paper":
            print("Hooray! computer wins.")
        else:
            print("oops! you smashed scissor you win.")
    elif player == "Paper":
        if computer == "Rock":
            print("yohoho!, you win.")
        else:
            print("sorry, you lose to coputer.")
    elif player == "Scissor":
        if computer == "Paper":
            print("Yeyy!, player wins.")
        else:
            # try out all posssible [Rock, Paper, Scissor] hand gestures with total of 6 differnrt types and their output.
            print("ohh!, soory you lost.")

    # if you want to play the game again, no need to run th program again and again
    play_again = input("choose y/n")
    if play_again.lower() != "y":  # the condition will break and come out of the loop when you choose other than "y" and you will exit from the loop as well as from RockPaperScissor game.
        break
