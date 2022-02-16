import random

def computer_guess(x):
    low=1
    high=x
    guess=0
    feed_back= ""
    while feed_back != "c":
        low == guess + 1
        high == guess - 1
        guess=int(random.randint(low,high))
        feed_back=input(f"is {guess} too high (H), too low (L) or is corect (C)").lower()
        if feed_back == "h":
            high=guess-1
            print(f"{guess} is too high")
        elif feed_back == "l":
            low=guess+1
            print(f"{guess} is too low")
    print("you have guees the number corect!")            

computer_guess(1000)
