
def check(comp , user):
    if comp == user:
        return 0
    
    if(comp == 0 and user == 1):
        return -1
    
    if(comp ==1 and user == 2):
        return -1
    
    if(comp == 2 and user == 0):
        return -1
    
    return 1
import random
comp = random.randint(0,2)
user = int(input("0 for snake \n ,1 for water \n and -1 for gun: "))

score = check(comp,user)

print("you:",user)
print("computer:",comp)
if(score == 0):
    print("its draw")
elif(score == -1):
    print("you lose")

else:
    print("you win")