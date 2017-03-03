import random
import time

play = 'yes'
while play.lower() == 'yes':
    print("Let's see how lucky you really are")
    time.sleep(3)
    print("can you handle the anticipation??")
    time.sleep(3)
    print("the result is almost here...")
    time.sleep(3)
    tails = random.randint(0, 1)
    if tails == 0:
        print("You Lose! So much for time consumption lol")
    else:
        print("You Win! It was worth the wait, am I right?")
    play = input("Care to try again? [yes/no]: ")
    if play == 'no':
        print("oh come on, you scared?")
    
