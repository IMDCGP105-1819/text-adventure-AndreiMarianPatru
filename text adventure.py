
import random
import time

#player
playerInv={'apple':0,'box':0,'bullet':0,'map':0,'knife':0,'DONUTS':0,'gun':1}


#create the rooms
room=[]
for i in range(10):
    if i==0:
        a={}
    else:
        a={'apple':random.randint(0,3),'box':random.randint(0,2),'bullet':random.randint(0,5),'map':random.randint(0,1),'knife':random.randint(0,1),'DONUTS':0}
    room.append(dict(a))
rightroom=random.randint(7,9)
room[rightroom].update({'DONUTS':1})
global currentRoom
currentRoom=0
roomNames=["THE GREAT HALL","THE LORDS & LADIES CHAMBER","THE SOLAR","THE WARDROBE","THE BOWER","THE MINSTREL'S GALLERY","THE THRONE ROOM","THE BATHROOM","THE KITCHEN","THE BUTTERY"]


def rooms():
    room=[]
    for i in range(10):
        if i==0:
            a={}
        else:
            a={'apple':random.randint(0,3),'box':random.randint(0,2),'bullet':random.randint(0,5),'map':random.randint(0,1),'knife':random.randint(0,1),'THE GOLDEN DONUTS':0}
        room.append(dict(a))
    rightroom=random.randint(7,9)
    room[rightroom].update({'DONUTS':1})

#basic commands
def commands():
    time.sleep(1)
    print("'go up' gets you in northen room")
    print("'go down' gets you in the southern room")
    print("'go right' gets you in the eastern room")
    print("'go left' gets you in the western room ")
    print("'lookroom' gets you a list of items in your current room ")
    print("'look <object>' gets you a short description of an item which is in your inventory or in the current room ")
    print("'drop <object>' drop a certain item which is in your inventory ")
    print("'use <object>' uses a specific item in your inventory")
    print("'take <object>' will take an item from current room and will put in in your inventory")
    print("'restart' will restart your adventure")
    print("'shoot <object>' will shoot a item in your room")

#movement
def go_up():
    global currentRoom
    if  currentRoom>=8:
        time.sleep(1)
        print("You can't go higher! ")
    else:
        currentRoom +=2
        time.sleep(1)
        print("You are now in",roomNames[currentRoom])
def go_down():
    global currentRoom
    if currentRoom<=1:
        time.sleep(1)
        print("You can't go lower! ")
    else:
        currentRoom -=2
        print("You are now in",roomNames[currentRoom])
def go_left():
    global currentRoom
    if currentRoom%2==0:
        time.sleep(1)
        print("There is no door on that wall ")
    else:
        currentRoom -=1
        time.sleep(1)
        print("You are now in",roomNames[currentRoom])
def go_right():
    global currentRoom
    if currentRoom%2==1:
        time.sleep(1)
        print("There is no door on that wall ")
    else:
        currentRoom +=1
        time.sleep(1)
        print("You are now in",roomNames[currentRoom])

def drop_item(key):
    playerInv[key]-=1
    print('the ',str(key),'is now in the current room')
    room[currentRoom][key]+=1

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

def use_gun(key):
    if playerInv['bullet']==0 and room[currentRoom]['bullet']==0:
        time.sleep(1)
        print("A gun wiyhout bullets is useless")
        time.sleep(1)
        print("Go and search some bullets")
    elif playerInv['bullet']>0:
        playerInv['bullet']-=1
    else:
        room[currentRoom]['bullet']-=1
        time.sleep(1)
        print("RATATATA!!!")
        room[currentRoom][key]-=1
        time.sleep(1)
        print("The ",key,' is now gone')


def look_item(key):
    if key=='apple':
        time.sleep(1)
        print("You are looking at a delicious apple")
        time.sleep(1)
        print("If you use this apple you will gain a random object from your inventory ")
    elif key=='knife':
        time.sleep(1)
        print('You are looking at a sharp knife')
        time.sleep(1)
        print("It doesn't do much, but your wife would be happy if you bring it back home. ")
    elif key=="map":
        time.sleep(1)
        print("You are looking at an old map.")
        time.sleep(1)
        print("When you find 4 pieces of it you will know the right room.")
    elif key=='box':
        time.sleep(1)
        print('You are looking at a box of chocolates')
        time.sleep(1)
        print("All you can get from it is some extra weight")
    elif key=='bullet':
        time.sleep(1)
        print('You are looking at a rusty bullet')
        time.sleep(1)
        print('It can be used to shoot things')
    elif key=='gun':
        time.sleep(1)
        print("You are looking at a rusty gun")
        time.sleep(1)
        print("You can use it to shoot a thing in your room")
    elif key=='DONUTS':
        time.sleep(1)
        print("You are looking at THE GOLDEN DONUTS")
        time.sleep(1)


def take_item(key):
    i=currentRoom
    room[i][key]-=1
    playerInv[key]+=1
    time.sleep(1)
    print("OK")

def use_apple():
    pinv=list(playerInv.keys())
    newitem=random.choice(pinv)
    playerInv[newitem]+=1
    time.sleep(1)
    print("Wow, you got a new ",str(newitem))
    time.sleep(1)
    print("You now have  ",playerInv['apple']," apples")
    if playerInv['apple']>0:
        playerInv['apple']-=1
    else:
        room[currentRoom]['apple']-=1



def use_maps():
    if playerInv['map']+room[currentRoom]['map']>=4:
        time.sleep(1)
        print("The donuts are in",str(roomNames[rightroom]),'!')
        if playerInv['map']<=4:
            room[currentRoom]['map']=4-playerInv['map']
            playerInv['map']=0
        else:
            playerInv['map']-=4
    else:
        time.sleep(1)
        print("You don't have enough pieces, go and search some")

def use_donuts():
    global currentRoom
    global playerInv
    global room
    if playerInv['DONUTS']==1 or room[currentRoom]['DONUTS']==1:
        time.sleep(1)
        print("You can now fulfill your destiny, enjoy them")
        print("------")
        print()
        print()
        print()
        answer=str(input("Do you wanna play again? yes/no "))
        if answer=='yes':
            restart()
        if answer=="no":
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
    playerInv={'apple':0,'box':0,'bullet':0,'map':0,'knife':0,'DONUTS':0,'gun':1}
    currentRoom=0
    print("A new adventure is starting now")
    print("Do you want an intro?")
    ans=input("y/n?")
    if ans=='y':
        intro()


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

print("Do you want an intro?")
ans=input("y/n?")
if ans=='y':
    intro()


#main loop
while True:
    invlist=list(playerInv.keys())
    print()
    print()
    command=input("What are you going to do now? ")
    splitList=command.split(" ")
    print()
    if splitList[0]=='go':
        if splitList[1]=='up':
            go_up()
        elif splitList[1]=='down':
            go_down()
        elif splitList[1]=='left':
            go_left()
        elif splitList[1]=='right':
            go_right()
    elif splitList[-1]=='look':
        lookroom()
    elif splitList[0]=='look':
        if splitList[1] in playerInv or splitList[1] in room[currentRoom]:
            if playerInv.get(splitList[1])>0 or room[currentRoom].get(splitList[1])>0:
                look_item(splitList[1])
        else:
            print("There is no such thing in your inventory or in the current room")
    elif splitList[0]=='drop':
        time.sleep(1)
        drop_item(splitList[1])
    elif splitList[0]=='use':
        time.sleep(1)
        j=list(playerInv.keys())
        k=list(room[currentRoom].keys())
        if item not in j and k :
            time.sleep(1)
            print("That item is not in your inventory or in the current room")
        else:
            if splitList[1]=="apple":
                use_apple()
            elif splitList[1]=='map':
                use_maps()
            elif  splitList[1]=="DONUTS":
                use_donuts()
            else:
                time.sleep(1)
                print("OK")
        if playerInv[item]>0:
            playerInv[item]-=1
        else:room[currentRoom][item]-=1
    elif splitList[0]=='shoot':
        use_gun(splitList[1])
    elif splitList[0]=='take':
        time.sleep(1)
        take_item(splitList[1])
    elif command=='help':
        commands()
    elif command=='inventory':
        inventory()
    elif command=='restart':
        restart()
    else:
        time.sleep(1)
        print("That is not a valid option!")
