import random


def game(comp,you):
# If two values are equal declare a tie!
    if comp == you:
        return None

# Check all possibilities if comp  choose R
    elif comp == 'R':
        if you== 'S':
            return False
        elif you== 'P':
            return True

# Check all possibilities if comp choose P
    elif comp == 'P':
        if you == 'S':
            return True
        elif you == 'R':
            return False

# Check all possibilities if comp choose S
    elif comp == 'S':
        if you == 'R':
            return True
        elif you == 'P':
            return False


print("Comp turn: Rock(R), Paper(P), Scissors(S)?")
randNo= random.randint(1,3)
if randNo==1:
    comp='R'
if randNo==2:
    comp='P'
if randNo==3:
    comp='S'



you= input("Player's turn: Rock(R), Paper(P), Scissors(S)?")
a= game(comp,you)



print(f"You chose {you}")
print(f"Computer chose {comp}")

if a == None:
    print('The game is a Tie!')
elif a:
    print ('You win!')
else:
    print=('You loose!')




