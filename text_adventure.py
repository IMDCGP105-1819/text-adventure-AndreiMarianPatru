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
def nouse():

    for i in range(10):
        print('room',i,'apples',room[i].get('apples'),'boxes',room[i].get('box'))
    print(room[5])
    room[5]['apples']=6
    print(room[5])
nouse()

#basic comands
def go_up():
    if currentRoom>=9:
        time.sleep(1)
        print("You can't go higher! ")
    else:
        currentRoom +=2
def go_down():
    if currentRoom<=1:
        time.sleep(1)
        print("You can't go lower! ")
    else:
        currentRoom -=2
def go_left():
    if currentRoom%2==0:
        time.sleep(1)
        print("There is no door on that wall ")
    else:
        currentRoom -=1
def go_right():
    if currentRoom%2==1:
        time.sleep(1)
        print("There is no door on that wall ")
    else:
        currentRoom +=1

def look():
    i=currentRoom
    time.sleep(1)
    print("With your sharp eyes you are seeing: ")
    keys=list(room[i].keys())
    values=list(room[i].values())
    for j in range(len(room[5])):
        print(keys[j]," ",values[j])
def look_item(key):
    i=currentRoom
    keys=list(room[i].keys())
    if key not in keys:
        time.sleep(1)
        print("You don't have that item and there is none in your current room")
    else:
        if key=='apples':
            time.sleep(1)
            print("You are watching a delicious apple")
            time.sleep(1)
            print("If you use this apple you will gain a random object from your inventory ")
        elif key=='knife':

            
#player
playerInv={}
currentRoom=0
playerInv["gun"]=1
     
#some little talk to let the player know his task
print("Greetings!")
time.sleep(1)
print("Your name is Bob. ")
time.sleep(1)
print("Your sole purpose in life is to eat the GOLDEN DONUTS!!!")
time.sleep(1)
print("After years of research you found out they are hidden in the Great GOLDEN CASTLE ")
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
time.sleep(1)
print("You enter in the Great GOLDEN CASTLE")
time.sleep(1)
print("You see 5 doors on your left and 5 doors on your right")
time.sleep(1)
print("You enter the first one on the left")
time.sleep(1)
print("Enter your command adventurer")

