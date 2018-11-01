import os 
import random
import time
#player
playerInv={'apple':0,'box':0,'bullet':0,'map':0,'knife':0,'THE GOLDEN DONUTS':0,'gun':1}



#create the rooms
room=[]
for i in range(10):
    if i==0:
        a={}
    else:
        a={'apple':random.randint(0,3),'box':random.randint(0,2),'bullet':random.randint(0,5),'map':random.randint(0,1),'knife':random.randint(0,1),'THE GOLDEN DONUTS':0}
    room.append(dict(a))
rightroom=random.randint(7,9)
room[rightroom].update({'THE GOLEDN DONUTS':1})
global currentRoom
currentRoom=0

def rooms():
    room=[]
    for i in range(10):
        if i==0:
            a={}
        else:
            a={'apple':random.randint(0,3),'box':random.randint(0,2),'bullet':random.randint(0,5),'map':random.randint(0,1),'knife':random.randint(0,1),'THE GOLDEN DONUTS':0}
        room.append(dict(a))
    rightroom=random.randint(7,9)
    room[rightroom].update({'THE GOLEDN DONUTS':1})

#basic commands
def go_up():
    global currentRoom
    if  currentRoom>=8:
        time.sleep(1)
        print("You can't go higher! ")
    else:
        currentRoom +=2
        time.sleep(1)
        print("You are now in room ",currentRoom)
def go_down():
    global currentRoom
    if currentRoom<=1:
        time.sleep(1)
        print("You can't go lower! ")
        time.sleep(1)
        print("You are now in room ",currentRoom)
    else:
        currentRoom -=2
def go_left():
    global currentRoom
    if currentRoom%2==0:
        time.sleep(1)
        print("There is no door on that wall ")
    else:
        currentRoom -=1
        time.sleep(1)
        print("You are now in room ",currentRoom)
def go_right():
    global currentRoom
    if currentRoom%2==1:
        time.sleep(1)
        print("There is no door on that wall ")
    else:
        currentRoom +=1
        time.sleep(1)
        print("You are now in room ",currentRoom)

def lookroom():
    i=currentRoom
    time.sleep(1)
    print("With your sharp eyes you are seeing: ")
    if i==0:
        time.sleep(1)
        print("There is nothing here, explore more")
    else:
        keyss=list(room[i].keys())
        values=list(room[i].values())
        for j in range(len(room[i])):
            if int(values[j])>0:
                print(keyss[j]," ",values[j])

def use_gun():
    if playerInv['bullet']==0:
        time.sleep(1)
        print("A gun wiyhout bullets is useless")
        time.sleep(1)
        print("Go and search some bullets")
    else:
        time.sleep(1)
        print("RATATATA!!!")
        playerInv['bullet']-=1

def commands():
    time.sleep(1)
    print("'w' gets you in northen room")
    print("'s' gets you in the southern room")
    print("'d' gets you in the eastern room")
    print("'a' gets you in the western room ")
    print("'lookroom' gets you a list of items in your current room ")
    print("'look' gets you a short description of an item which is in your inventory or in the current room ")
    print("'drop ' drop a certain item which is in your inventory ")
    print("'use' uses a specific item in your inventory")
    print("'take' will take an item from current room and will put in in your inventory")
    print("'restart' will restart your adventure")

def look_item(key):
    j=list(playerInv.keys())
    i=currentRoom
    keys=list(room[i].keys())
    k=j+keys
    if key not in k :
        time.sleep(1)
        print("You don't have that item and there is none in your current room")
    else:
        if key=='apple':
            time.sleep(1)
            print("You are watching a delicious apple")
            time.sleep(1)
            print("If you use this apple you will gain a random object from your inventory ")
        elif key=='knife':
            time.sleep(1)
            print('You are watching a sharp knife')
            time.sleep(1)
            print("It doesn't do much, but your wife would be happy if you bring it back home. ")
        elif key=="map":
            time.sleep(1)
            print("You are watching an old map.")
            time.sleep(1)
            print("When you find 4 pieces of it you will know the right room.")
        elif key=='box':
            time.sleep(1)
            print('You are watching a box of chocolates')
            time.sleep(1)
            print("All you can get from it is some extra weight")
        elif key=='bullet':
            time.sleep(1)
            print('You are watching a rusty bullet')
            time.sleep(1)
            print('It can be used to shoot...')
            time.sleep(1)
            print("nothing because this is a child-friendly game")


def drop_item(key):
    playerInv[key]-=1
    print('the ',str(key),'is lost forever now')

def use_apple():
    if playerInv['apple']>=1:
        pinv=list(playerInv.keys())
        newitem=random.choice(pinv)
        playerInv[newitem]+=1
        time.sleep(1)
        print("Wow, you got a new ",str(newitem))
        playerInv['apple']-=1
        time.sleep(1)
        print("You now have  ",playerInv['apple']," apples")
    else:
        time.sleep(1)
        print("You don't have any apples, go and search some")

def use_maps():
    if playerInv['map']>=4:
        time.sleep(1)
        print("The donuts are in the room ",str(rightroom),'!')
    else:
        time.sleep(1)
        print("You don't have enough pieces, go and search some")

def use_donuts():
    global currentRoom
    global playerInv
    global room
    if playerInv['THE GOLDEN DONUTS']==1:
        time.sleep(1)
        print("You can now fulfill your destiny, enjoy them")
        print("------")
        print()
        print()
        print()
        restart=input("Do you wanna play again? yes/no")
        if restart=='yes':
            restart()
        if restart=="no":
            time.sleep()
            print("All you can do now is explore and grab things")
    else:
        time.sleep(1)
        print("Your adventure is not finished yet")
def restart():
    global currentRoom
    global playerInv
    global room
    rooms()
    playerInv=dict((k,0) for k in playerInv)
    currentRoom=0
    print("A new adventure is starting now")
    intro()


def take_item(key):
    i=currentRoom
    room[i][key]-=1
    playerInv[key]+=1
    time.sleep(1)
    print("OK")

def inventory():
    keys=list(playerInv.keys())
    values=list(playerInv.values())
    if sum(values)==0:
        time.sleep(1)
        print("There is nothing in your invenotry, go and search some stuff")
    else:
        for j in range(len(playerInv)):
            if int(values[j])>0:
                print(keys[j]," ",values[j])
   

#some little talk to let the player know his task
def intro():
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
    print("Type help for a list of commands")
intro()



#main loop
while True:
    invlist=list(playerInv.keys())
    #time.sleep(1)
    
    #time.sleep(1)
    print()
    print()
    command=input("What are you going to do now? ")
    print()
    if command=="w":
        go_up()
    elif command=='s':
        go_down()
    elif command=='a':
        go_left()
    elif command=='d':
        go_right()
    elif command=='lookroom':
        lookroom()
    elif command=='look':
        time.sleep(1)
        item=str(input("Which item?"))
        look_item(item)
    elif command=='drop':
        time.sleep(1)
        item=input("Which item?")
        drop_item(item)
    elif command=='use':
        time.sleep(1)
        item=input("Which item?")
        j=list(playerInv.keys())
        if item not in j:
            time.sleep(1)
            print("You don't have that item in your inventory")
        else:
            if item=="apple":
                use_apple()
            elif item=='map':
                use_maps()
            elif  item=="THE GOLDEN DONUTS":
                use_donuts()
            elif item=='gun':
                use_gun()
            else:
                time.sleep(1)
                print("OK")
    elif command=='take':
        time.sleep(1)
        item=input("Which item?")
        take_item(item)
    elif command=='help':
        commands()
    elif command=='inventory':
        inventory()
    elif command=='restart':
        restart()
    else:
        time.sleep(1)
        print("That is not a valid option!")
