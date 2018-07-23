import random
import time

possible_answers = ["A hotdog", "Not a hotdog", "cystic fibrosis"]

def analysis():
    print( "Type in the conditions you've been feeling below, and HotdogFibrosis will use cloud and learning techniques to figure out your condition.")
    text=input("How are you feeling?")
    print("Hold on... HotdogFibrosis' algorithms are working hard!")
    time.sleep(2)
    x = random.randint(0, 2)
    print("You've got: " + possible_answers[x])
    again=input("Run again?")
    if again=="Yes":
        print("Restarting...")
        time.sleep(3.5)
        analysis()
    else:
        print("Thanks! Please run again when you need help!")

def main():
    print("Welcome to HotdogFibrosis, the very first command line diagnostic service.")
    dont_care=input("Are you ready?")
    time.sleep(1.5)
    print("Great!")
    time.sleep(0.5)
    analysis()

if __name__ == '__main__':
    main()
