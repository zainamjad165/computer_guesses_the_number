import random

def computer_guess(x):
    lowest = 1
    highest = x
    guess = 0
    feed_back = ""
    while feed_back != "c":
        lowest == guess + 1
        highest == guess - 1
        guess = int(random.randint(lowest,highest))
        feed_back = input(f"Is {guess} too high (H), too low (L) or is corect (C)").lower()
        if feed_back == "h":
            highest = guess-1
            print(f"{guess} is too high")
        elif feed_back == "l":
            lowest = guess+1
            print(f"{guess} is too low")
    print("Your guess is correct.")            

computer_guess(1000)
