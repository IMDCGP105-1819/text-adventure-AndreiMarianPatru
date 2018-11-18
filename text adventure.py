
import random
import time
import sys

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
    print()


#player
playerInv={'apple':0,'box':0,'bullet':0,'map':0,'knife':0,'DONUTS':0,'gun':1}


#create the rooms
room=[]
for i in range(10):
    if i==0:
        a={'apple':0,'box':0,'bullet':0,'map':0,'knife':0,'DONUTS':0}
    else:
        a={'apple':random.randint(0,3),'box':random.randint(0,2),'bullet':random.randint(0,5),'map':random.randint(0,1),'knife':random.randint(0,1),'DONUTS':0}
    room.append(dict(a))
rightroom=random.randint(7,9)
room[rightroom].update({'DONUTS':1})
global currentRoom
currentRoom=0
roomNames=["THE GREAT HALL","THE LORDS & LADIES CHAMBER","THE SOLAR","THE WARDROBE","THE BOWER","THE MINSTREL'S GALLERY","THE THRONE ROOM","THE BATHROOM","THE KITCHEN","THE BUTTERY"]
unshootable=['bullet','map','knife','DONUTS','gun']
undroppable=['gun','DONUTS']

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

    print(" go up - gets you in northen room")
    print(" go down - gets you in the southern room")
    print(" go right - gets you in the eastern room")
    print(" go left - gets you in the western room ")
    print(" look - gets you a list of items in your current room ")
    print(" look object - gets you a short description of an item which is in your inventory or in the current room ")
    print(" drop object - drop a certain item which is in your inventory ")
    print(" use object - uses a specific item in your inventory")
    print(" take object - will take an item from current room and will put in your inventory")
    print(" restart - will restart your adventure")
    print(" shoot <object - will shoot a item in your room")

#movement
def go_up():
    global currentRoom
    if  currentRoom>=8:

        print_slow("You can't go higher! ")
    else:
        currentRoom +=2

        print_slow("You are now in "+str(roomNames[currentRoom]))
def go_down():
    global currentRoom
    if currentRoom<=1:

        print_slow("You can't go lower! ")
    else:
        currentRoom -=2
        print_slow("You are now in "+str(roomNames[currentRoom]))
def go_left():
    global currentRoom
    if currentRoom%2==0:

        print_slow("There is no door on that wall ")
    else:
        currentRoom -=1

        print_slow("You are now in "+str(roomNames[currentRoom]))
def go_right():
    global currentRoom
    if currentRoom%2==1:

        print_slow("There is no door on that wall ")
    else:
        currentRoom +=1

        print_slow("You are now in "+str(roomNames[currentRoom]))

def drop_item(key):
    if key not in playerInv and room[currentRoom]:

        print_slow("You don't have that item")
        return
    elif playerInv[key]==0:

        print_slow("There is nothing to drop")
    elif key in undroppable:

        print_slow("There is no point in dropping that")
    else:
        playerInv[key]-=1
        print_slow('the '+str(key)+'is now in the current room')
        room[currentRoom][key]+=1

def inventory():
    keys=list(playerInv.keys())
    values=list(playerInv.values())
    if sum(values)==0:

        print_slow("There is nothing in your invenotry, go and search some stuff")
    else:
        for j in range(len(playerInv)):
            if int(values[j])>0:
                print_slow(str(keys[j])+" "+str(values[j]))


def lookroom():
    i=currentRoom

    print_slow("With your sharp eyes you are seeing: ")
    if i==0:

        print_slow("There is nothing here, explore more")
    else:
        keyss=list(room[i].keys())
        values=list(room[i].values())
        for j in range(len(room[i])):
            if int(values[j])>0:
                print_slow(str(keyss[j])+" "+str(values[j]))

def use_gun(key):
    if playerInv['bullet']==0 and room[currentRoom]['bullet']==0:

        print_slow("A gun wiyhout bullets is useless")

        print_slow("Go and search some bullets")
        return
    if key in unshootable or key not in playerInv and room[currentRoom]:

        print_slow("There is no point in shooting that")
        return
    elif playerInv['bullet']>0:
        playerInv['bullet']-=1
    else:
        room[currentRoom]['bullet']-=1

    print_slow("RATATATA!!!")
    room[currentRoom][key]-=1

    print_slow("The "+str(key)+' is now gone')


def look_item(key):
    if key=='apple':

        print_slow("You are looking at a delicious apple")

        print_slow("If you use this apple you will gain a random object from your inventory ")
    elif key=='knife':

        print_slow('You are looking at a sharp knife')

        print_slow("It doesn't do much, but your loved one would be happy if you bring it back home. ")
    elif key=="map":

        print_slow("You are looking at an old map.")

        print_slow("When you find 4 pieces of it you will know the right room.")
    elif key=='box':

        print_slow('You are looking at a box of chocolates')

        print_slow("All you can get from it is some extra weight")
    elif key=='bullet':

        print_slow('You are looking at a rusty bullet')

        print_slow('It can be used to shoot things')
    elif key=='gun':

        print_slow("You are looking at a rusty gun")

        print_slow("You can use it to shoot a thing in your room")
    elif key=='DONUTS':

        print_slow("You are looking at THE GOLDEN DONUTS")



def take_item(key):
    if key not in playerInv and room[currentRoom]:

        print_slow("There is no such thing in this room or you took them all")
        return
    if room[currentRoom][key]==0:

        print_slow("There is no such thing in this room or you took them all")
        return
    else:
        room[currentRoom][key]-=1
        playerInv[key]+=1

        print_slow("OK")

def use_apple():
    pinv=list(playerInv.keys())
    newitem=random.choice(pinv)
    if newitem=='DONUTS':
        use_apple()
    playerInv[newitem]+=1
    print_slow("Wow, you got a new "+str(newitem))
    if playerInv['apple']>0:
        playerInv['apple']-=1
    else:
        room[currentRoom]['apple']-=1
    print_slow("You now have  "+str(playerInv['apple'])+" apples")



def use_maps():
    if playerInv['map']+room[currentRoom]['map']>=4:

        print_slow("The donuts are in "+str(roomNames[rightroom])+' !')
        if playerInv['map']<=4:
            room[currentRoom]['map']=4-playerInv['map']
            playerInv['map']=0
        else:
            playerInv['map']-=4
    else:

        print_slow("You don't have enough pieces, go and search some")

def use_donuts():
    global currentRoom
    global playerInv
    global room
    if playerInv['DONUTS']==1 or room[currentRoom]['DONUTS']==1:

        print_slow("You can now fulfill your destiny, enjoy them")
        print_slow("------")
        print()
        print()
        print()
        answer=str(input("Do you wanna play again? yes/no "))
        if answer=='yes':
            restart()
        if answer=="no":
            time.sleep()
            print_slow("All you can do now is explore and grab things")
    else:

        print_slow("Your adventure is not finished yet")

def restart():
    global currentRoom
    global playerInv
    global room
    rooms()
    playerInv={'apple':0,'box':0,'bullet':0,'map':0,'knife':0,'DONUTS':0,'gun':1}
    currentRoom=0
    print_slow("A new adventure is starting now")
    print_slow("Do you want an intro?")
    ans=input("y/n?")
    if ans=='y':
        intro()


#some little talk to let the player know his task
def intro():
    print_slow("Greetings!")

    print_slow("Your name is Bob. ")

    print_slow("Your sole purpose in life is to eat the GOLDEN DONUTS!!!")

    print_slow("After years of research you found out they are hidden in the Great GOLDEN CASTLE ")

    name=input("Enter your name: ")

    print_slow("Well done "+str(name)+"! Let's begin!")

    print_slow("You enter in the Great GOLDEN CASTLE")

    print_slow("You see 5 doors on your left and 5 doors on your right")

    print_slow("You enter the first one on the left")

    print_slow("Type help for a list of commands")

print_slow("Do you want an intro?")
ans=input("y/n?")
if ans=='y':
    intro()
elif ans=="n":
    commands()


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
                print_slow("There is no such thing in your inventory or in the current room")
        else:
            print_slow("There is no such thing in your inventory or in the current room")
    elif splitList[0]=='drop':

        drop_item(splitList[1])
    elif splitList[0]=='use':
        if splitList[1] not in playerInv and room[currentRoom]:

            print_slow("That item is not in your inventory or in the current room")
        else:
            if splitList[1]=="apple":
                if room[currentRoom]['apple']>0 or playerInv['apple']>0:
                    use_apple()
                else:

                    print_slow("You don't have any apples now")

            elif splitList[1]=='map':
                if room[currentRoom]['map']>0 or playerInv['map']>0:
                    use_maps()
                else:

                    print_slow("You don't have enough maps now")
            elif  splitList[1]=="DONUTS":
                use_donuts()
            else:

                print_slow("OK")

    elif splitList[0]=='shoot':
        use_gun(splitList[1])
    elif splitList[0]=='take':

        take_item(splitList[1])
    elif command=='help':
        commands()
    elif command=='inventory':
        inventory()
    elif command=='restart':
        restart()
    else:

        print_slow("That is not a valid option!")
