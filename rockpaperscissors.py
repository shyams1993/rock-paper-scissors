import time,sys
p1counter=0
p2counter=0

p1choice = input("Player 1: Which one do you want to select?\nROCK - Enter Rock or r || SCISSORS - Enter Scissors or s || PAPER or p\n")
p2choice = input("Player 2: Which one do you want to select?\nROCK - Enter Rock or r || SCISSORS - Enter Scissors or s || PAPER or p\n")

if (p1choice == 'rock' or p1choice == 'r')  and (p2choice == 'paper' or p2choice == 'p'):
    p2counter+=1
elif (p1choice == 'rock' or p1choice == 'r') and (p2choice == 'scissors' or p2choice == 's'):
    p1counter+=1
elif (p1choice == 'paper' or p1choice == 'p') and (p2choice == 'scissors' or p2choice == 's'):
    p2counter+=1
elif (p2choice == 'rock' or p2choice == 'r')  and (p1choice == 'paper' or p1choice == 'p'):
    p1counter+=1
elif (p2choice == 'rock' or p2choice == 'r') and (p1choice == 'scissors' or p1choice == 's'):
    p2counter+=1
elif (p2choice == 'paper' or p2choice == 'p') and (p1choice == 'scissors' or p1choice == 's'):
    p1counter+=1
else:
    print("Wrong input")

if p1counter>p2counter:
    print("Player 1 : {} wins".format(p1choice))
    time.sleep(3)
    sys.exit()
else:
    print("Player 2 : {} wins".format(p2choice))
    time.sleep(3)
    sys.exit()
