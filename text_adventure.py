import random
import time


#create the rooms
room=[]
for i in range(10):
    if i==0:
        a={}
    else:
        a={'apples':random.randint(0,3),'box':random.randint(0,2),'plate':random.randint(0,1),'bullets':random.randint(0,5),'map':random.randint(0,1)}
    room.append(dict(a))


#some code to make sure the rooms are created right
for i in range(10):
    print('room',i,'apples',room[i].get('apples'),'boxes',room[i].get('box'))
print(room[5])
room[5]['apples']=6
print(room[5])

#player
playerInv={}
currentRoom=0
     

#some little talk to let the player know his task
print("Greetings!")
time.sleep(1)
print("Your name is Bob. ")
time.sleep(1)
print("Your sole purpose in life is to eat the GOLDEN DONUTS!!!")
time.sleep(1)
print("After years of research you found out they are hidden in the Great Golden Castle ")
time.sleep(1)
print("I guess you know what you have to do now, if not you will figure something out")
time.sleep(1)
falsename=input("Enter your name: ")
time.sleep(1)
if falsename !="Bob":
    print("...")
    time.sleep(1)
    print("I just told you your name is Bob, please pay attention")
    time.sleep(1)
    print("Anyway, let's begin")
else:
    print("Oh, I see you are a clever adventurer")
    time.sleep(1)
    print("Let's begin")
    time.sleep(1)


