
import sys  

print("welcome to python RPG Game \'Treasure Hunter\'! What's your name?")

x = input()

while not x.isalpha():
    x = input("Please enter only alphabets: ")
print (f"hello, {x}! You are on a journey in Lost Island to find a treasure.\nYou will have two choices of moves in this game.\n\
the game is over when the player get lost, dead, or when the player finds the treasure.")
print("Please input 1 to continue.")
while True:
    q = input()
    if q == "1":
        print ("Good luck !")
        break
    else:
        print("invalid input. Please try again.")

print("The ship has arrived on the beach.\n\
Your feet lands on the sand, you put your attention on the forest in front of your eyes.\n\
But it doesn't seem to hurt to take a bit of your time to relax and explore the beach first.")
print("a. go to the forest")
print("b. explore the beach")
print("please input a or b")
while True:
    s = input()
    if s == "a":
        print ("You decided to go right away to the forest.\n\
The trees surrounding the forest creates a darkness that gives you an eerie feeling.\n\
You spotted a ripped out flesh of a deer near the brushes. Your curiosity strikes.")
        print("a. Go near the flesh to examine it.")
        print("b. Go far away from the flesh.")
        while True:
            t = input()
            if t == "a":
                print ("You take a walk to the flesh to check.\n\
There is a bite mark all over it, looks like the hunter was bored with its meal and left it.")
                print ("You see something bright after you walked past the flesh, and walk closer to it.\n\
There's a small lake inside the forest. You could see the water illuminating the sunlight. You wonder if something's in it.")
                print ("a. Dive inside the lake.")
                print("b. Leave the lake and continue the journey.")
                while True:
                    p = input()
                    if p == "a":
                        print("You decide to dive in. You found a chest full of golds inside the lake.")
                        print("*****The End*****")
                        sys.exit()
                    if p == "b":
                        print("You decide to leave the lake alone and continues the journey, but to no avail.\n\
The sun is starting to drown and you still haven't found anything. You get lost inside the forest.")
                        print("*****Game Over*****")
                        sys.exit()          
            elif t == "b": 
                print("You decided to take the other side of the walk to avoid risk of wild animals.\n\
Unfortunately, your decision isn't much of a charm. You saw a big cat with black stripes appearing out of the brushes. \n\
Looks like it wants you as its next meal.")
                print("*****Game Over*****")
                sys.exit()
                
            else:
                print("Invalid input. Please try again.")

    elif s == "b" :
        print("You decided to explore the beach a bit before going to the forest.\n\
fortunately, you found a treasure map buried under the sands.\n\
It's unknown whether the treasure is taken or not, but at least you could save a lot of time with the map.")
        print("*****The End*****")
        sys.exit()
    else:
        print("invalid input. please try again.")
