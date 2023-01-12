import time
import os
import math
from datetime import datetime
print()
print()
print('Split Board Dart Game')
print('Inspired by the Game "Section 5" from godartspro.com')
print()
print()
print('0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
print('0______________________________________________________________________________________0')
print('0___________#######________#########_______####__________####___################_______0')
print('0_________##########_______###########_____####__________####___################_______0')
print('0________####____####______####____####____####__________####_________####_____________0')
print('0_________####_____________####____####____####__________####_________####_____________0')
print('0__________####____________###########_____####__________####_________####_____________0')
print('0____________####__________#########_______####__________####_________####_____________0')
print('0______________####________####____________####__________####_________####_____________0')
print('0________####___####_______####____________####__________####_________####_____________0')
print('0_________##########_______####____________###########___####_________####_____________0')
print('0___________#####__________####____________###########___####_________####_____________0')
print('0______________________________________________________________________________________0')
print('0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
print()
print('Rules:')
print('The Dartboard is splitted in 5 different Areas')
print('Area 1 = The Fields 5 - 20 - 1')
print('Area 2 = The Fields 13 - 6 - 10')
print('Area 3 = The Fields 17 - 3 - 19')
print('Area 4 = The Fields 8 - 11 - 14')
print('Area 5 = The Fields Bull - Bullsey')
print('in each Round you have to hit the fields from its Area (Round 1 - Area 1)')
print('for the inner fields (for example 20) you earn 5 Points and for the outer fields (for example 5 or 1) you earn 1 Point')
print('this is "Hard Mode", if you hit the wrong fields you get minus Points')
print('You can Abort the Game if you type exit')
while True:
    user_input = input("Do you want to start the game? (y/n)")
    if user_input == "y":
        os.system('clear')
        print()
        print("Game on")
        break
    elif user_input == "n":
        print("Goodbye")
        exit()
    elif user_input =='exit':
                exit()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        print("In 5 seconds i will ask you again")
        time.sleep(5)
        os.system('clear')



scores_r1 = {
    'player1': {'1': 0,'2': 0,'3': 0,'4': 0,'5': 0,'6': 0,'7': 0,'8': 0,'9': 0,'10': 0,'11': 0,'12': 0,'13': 0,'14': 0,'15': 0,'16': 0,'17': 0,'18': 0,'19': 0,'20': 0,'25': 0,'50': 0,'0': 0},
}

# Initialize number of rounds
rounds = 1

# Loop for the number of rounds
for i in range(rounds):
    # Loop for each player
    for player in scores_r1.keys():
        print()
        print()
        print ('try to hit 20 for 5 Points')
        print ('try to hit 1 for 1 Point')
        print ('try to hit 5 for 1 Point')
        # Loop for 3 darts per turn
        for j in range(3):
            print()
            print("Which field do you hit with dart", j+1, "?")
            dart_score = input()
            while not dart_score.isdigit():
                print("Invalid input. Please enter a number.")
                dart_score = input()
            if dart_score == '20':
                scores_r1[player][dart_score] += 5
            elif dart_score == '1':
                scores_r1[player][dart_score] += 1
            elif dart_score == '5':
                scores_r1[player][dart_score] += 1
            elif dart_score is not '20' or '1' or '5':
                scores_r1[player][dart_score] -= 2
            elif dart_score == 'exit':
                exit()

player1_round1_score = sum(scores_r1['player1'].values())
scores_r1 = player1_round1_score

os.system('clear')

# Initialize scores for player for second Round
scores_r2 = {
    'player1': {'1': 0,'2': 0,'3': 0,'4': 0,'5': 0,'6': 0,'7': 0,'8': 0,'9': 0,'10': 0,'11': 0,'12': 0,'13': 0,'14': 0,'15': 0,'16': 0,'17': 0,'18': 0,'19': 0,'20': 0,'25': 0,'50': 0,'0': 0},
}

# Initialize number of rounds
rounds = 1

# Loop for the number of rounds
for i in range(rounds):
    # Loop for each player
    for player in scores_r2.keys():
        print('Current Score:', player1_round1_score)
        print()
        print('Second Round')
        print()
        print ('try to hit 6 for 5 Points')
        print ('try to hit 10 for 1 Point')
        print ('try to hit 13 for 1 Point')
        # Loop for 3 darts per turn
        for j in range(3):
            print()
            print("Which field do you hit with dart", j+1, "?")
            dart_score = input()
            while not dart_score.isdigit():
                print("Invalid input. Please enter a number.")
                dart_score = input()
            if dart_score == '6':
                scores_r2[player][dart_score] += 5
            elif dart_score == '10':
                scores_r2[player][dart_score] += 1
            elif dart_score == '13':
                scores_r2[player][dart_score] += 1
            elif dart_score is not '6' or '10' or '13':
                scores_r2[player][dart_score] -= 2
            elif dart_score == 'exit':
                exit()
player1_round2_score = sum(scores_r2['player1'].values())

scores_r2 = player1_round2_score
player1_total_score = scores_r1 + scores_r2


os.system('clear')

# Initialize scores for player for third Round
scores_r3 = {
    'player1': {'1': 0,'2': 0,'3': 0,'4': 0,'5': 0,'6': 0,'7': 0,'8': 0,'9': 0,'10': 0,'11': 0,'12': 0,'13': 0,'14': 0,'15': 0,'16': 0,'17': 0,'18': 0,'19': 0,'20': 0,'25': 0,'50': 0,'0': 0},
}

# Initialize number of rounds
rounds = 1

# Loop for the number of rounds
for i in range(rounds):
    # Loop for each player
    for player in scores_r3.keys():
        print('Current Score:', player1_total_score)
        print()
        print('Third Round')
        print()
        print ('try to hit 3 for 5 Points')
        print ('try to hit 19 for 1 Point')
        print ('try to hit 17 for 1 Point')
        # Loop for 3 darts per turn
        for j in range(3):
            print()
            print("Which field do you hit with dart", j+1, "?")
            dart_score = input()
            while not dart_score.isdigit():
                print("Invalid input. Please enter a number.")
                dart_score = input()
            if dart_score == '3':
                scores_r3[player][dart_score] += 5
            elif dart_score == '19':
                scores_r3[player][dart_score] += 1
            elif dart_score == '17':
                scores_r3[player][dart_score] += 1
            elif dart_score is not '3' or '19' or '17':
                scores_r3[player][dart_score] -= 2
            elif dart_score == 'exit':
                exit()
    
player1_round3_score = sum(scores_r3['player1'].values())

scores_r3 = player1_round3_score
player1_total_score = scores_r1 + scores_r2 + scores_r3


os.system('clear')

# Initialize scores for player for fourth Round
scores_r4 = {
    'player1': {'1': 0,'2': 0,'3': 0,'4': 0,'5': 0,'6': 0,'7': 0,'8': 0,'9': 0,'10': 0,'11': 0,'12': 0,'13': 0,'14': 0,'15': 0,'16': 0,'17': 0,'18': 0,'19': 0,'20': 0,'25': 0,'50': 0,'0': 0},
}

# Initialize number of rounds
rounds = 1

# Loop for the number of rounds
for i in range(rounds):
    # Loop for each player
    for player in scores_r4.keys():
        print('Current Score:', player1_total_score)
        print()
        print('Fourth Round')
        print()
        print ('try to hit 11 for 5 Points')
        print ('try to hit 14 for 1 Point')
        print ('try to hit 8 for 1 Point')
        # Loop for 3 darts per turn
        for j in range(3):
            print()
            print("Which field do you hit with dart", j+1, "?")
            dart_score = input()
            while not dart_score.isdigit():
                print("Invalid input. Please enter a number.")
                dart_score = input()
            if dart_score == '11':
                scores_r4[player][dart_score] += 5
            elif dart_score == '14':
                scores_r4[player][dart_score] += 1
            elif dart_score == '8':
                scores_r4[player][dart_score] += 1
            elif dart_score is not '11' or '14' or '8':
                scores_r4[player][dart_score] -= 2
            elif dart_score == 'exit':
                exit()

player1_round4_score = sum(scores_r4['player1'].values())

scores_r4 = player1_round4_score
player1_total_score = scores_r1 + scores_r2 + scores_r3 + scores_r4

os.system('clear')
# Initialize scores for player for final Round
scores_r5 = {
    'player1': {'n': 0,'y': 0,'1': 0,'2': 0,'3': 0,'4': 0,'5': 0,'6': 0,'7': 0,'8': 0,'9': 0,'10': 0,'11': 0,'12': 0,'13': 0,'14': 0,'15': 0,'16': 0,'17': 0,'18': 0,'19': 0,'20': 0,'25': 0,'50': 0,'0': 0},
}


# Initialize number of rounds
rounds = 1

# Loop for the number of rounds
for i in range(rounds):
    # Loop for each player
    for player in scores_r5.keys():
        print('Current Score:', player1_total_score)
        print()
        print('Final Round')
        print()
        print ('try to hit the Bull or Bullseye for 5 Points')
        print ('every other hit increses your Points by 2')
        print ('For Bull or Bullseye enter "y"')
        
        # Loop for 3 darts per turn
        for j in range(3):
            print()
            print("Do you hit the Bull or Bullseye? (y/n)")
            dart_score = input()
            while dart_score != 'y' and dart_score != 'n':
                print("Invalid input. Please enter 'y' or 'n'.")
                print("Do you hit the Bull or Bullseye?")
                dart_score = input()
            if dart_score == 'y':
                scores_r5[player][dart_score] += 5
            elif dart_score == 'n':
                scores_r5[player][dart_score] -= 2
            elif dart_score == 'exit':
                exit()
           
player1_round5_score = sum(scores_r5['player1'].values())

scores_r5 = player1_round5_score
player1_total_score = scores_r1 + scores_r2 + scores_r3 + scores_r4 + scores_r5

os.system('clear')

print()
print()
print("Your previous scores:")
print()
now = datetime.now()
current_time = now.strftime("%d.%m.%Y %H:%M:%S")

with open("score.txt", "a") as file:
    file.write(current_time + " " + "Score:" + " " + str(player1_total_score) + "\n")

with open("score.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)
print()
print('Finals Score:', player1_total_score)
print()
print('Thanks for Playing')
print()
