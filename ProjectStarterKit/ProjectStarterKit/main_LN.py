import pygame

###############################################################
# Keep this block at the beginning of your code. Do not modify.
def initEnv():
    print("\nWelcome! Before we start...")
    env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    while env not in "mri":
        print("Environment not recognized, type again.")
        env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    print("Great! Have fun!\n")
    return env

# Use the playSound() function below to play sounds.
# soundfilename does not include the .wav extension,
# e.g. playSound(apples,ENV) plays apples.wav
def playSound(soundfilename,env):
    if env == "m":
        exec("sounds." + soundfilename + ".play()")
    elif env == "r":
        from replit import audio
        audio.play_file("sounds/"+soundfilename+".wav")
    elif env == "i":
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/"+soundfilename+".wav")
        pygame.mixer.music.play()

ENV = initEnv()
###############################################################
import cmpt120image as c
import draw as d
import random as r
import main_LN as m


#list of item
apples = c.getImage("./ProjectStarterKit/ProjectStarterKit/images/apples.png")
burger = c.getImage("./ProjectStarterKit/ProjectStarterKit/images/burger.png")
bread =c.getImage("./ProjectStarterKit/ProjectStarterKit/images/bread.png")
child = c.getImage("./ProjectStarterKit/ProjectStarterKit/images/child.png")
coffee = c.getImage("./ProjectStarterKit/ProjectStarterKit/images/coffee.png")
dog =c.getImage("./ProjectStarterKit/ProjectStarterKit/images/dog.png")
door = c.getImage("./ProjectStarterKit/ProjectStarterKit/images/door.png")
eggs = c.getImage("./ProjectStarterKit/ProjectStarterKit/images/eggs.png")
fish =c.getImage("./ProjectStarterKit/ProjectStarterKit/images/fish.png")
oranges = c.getImage("./ProjectStarterKit/ProjectStarterKit/images/oranges.png")
salt = c.getImage("./ProjectStarterKit/ProjectStarterKit/images/salt.png")
tipi = c.getImage("./ProjectStarterKit/ProjectStarterKit/images/tipi.png")

#list of blackfoot item include get image file and its name [getImage,'image name']
listbf=[[apples,'apples'], [bread,'bread'],[burger,'burger'], [child,'child'], [coffee, 'coffee'], [dog,'dog'], [door,'door'], [eggs,'eggs'], [fish,'fish'], [oranges,'oranges'], [salt,'salt'], [tipi,'tipi']]
#list of default: item
item=[[apples,'apples'], [bread,'bread'],[burger,'burger']]
#listbf_new: list of item that will be modify by setting
listbf_new=item

#call out function


#definition of function

#random color
def colorR():
    red=r.randint(1,255)
    green=r.randint(1,255)
    blue=r.randint(1,255)
    colRGB=(red,green,blue)
    return colRGB


#menu
def menu():
  print('''Hello from pygame community. https://www.pygame.org/contribute.html\n'
  MAIN MENU
  1. Learn - Word Flashcards
  2. Play - Seek and Find Game
  3. Settings - Change Difficulty
  4. Exit''')
def chooseinmenu():
  ans=input('Choose an option: ')
  if ans=='1':
   learn()
   menu()
  elif ans=='2':
   play()
   menu()
  elif ans=='3':
   setting()
   menu()
  elif ans=='4':
   exit()
  return chooseinmenu()

#learn
def learn():
  canvas = c.getWhiteImage(400,300)

  for i in listbf_new:
      res = d.distributeItems(canvas,i[0],1)
      showres=c.showImage(res)
      playSound(i[1],ENV)
      input('Press Enter to continue...')
#setting
def setting():
    listbf_new.clear()
    anschoice=input('How many word do you want to learn (3-12 word)? ')
     #if the number does not in range[3,12], say do it again
    while int(anschoice) not in range(3,13):
        print('Please choose the number of word again.')
        anschoice=input('How many word do you want to learn (3-12 word)? ')
    #create a new list if the user want to choose 1,2
    r.shuffle(listbf)
    for i_3 in range(int(anschoice)):
        w=listbf[i_3]
        listbf_new.append(w)
    return listbf_new

#play(2function)

#processing image (recolor, minify, mirror)
def playsub(i_pls):
    i_pls=r.choice([d.mirror(i_pls) and d.minify(i_pls),d.mirror(i_pls),d.minify(i_pls),i_pls])
    i_pls1=d.recolorImage(i_pls,colorR())
    return i_pls1

def play():
    canvas = c.getWhiteImage(400,300)
    #intro
    print(''' Play
    This is a seek and find game. You will hear a word.
    Count how many of that item you find!''')
    #ask how many round
    ans_r=input('How many rounds would you like to play? ')
    listp=[]
    for i_r in range(int(ans_r)-1):
        #create a list of 3 item from listbf_new
        r.shuffle(listbf_new)
        for i_p in range(3):
            w_p=listbf_new[i_p]
            listp.append(w_p)
        #for every word in listplay
        #generate a number that will be the number of that item that will display
        # along with playing the sound
        for i_pl in listp:
            n=r.randint(1,4)

            i1=listp.index(i_pl)
            i_pl1=(i1)+1
            i_pl2=(i1)-1
            playSound(i_pl[1],ENV)
            #distribute items
            sn=d.distributeItems(canvas,playsub(i_pl[0]),n)
            for i_pll in listp:
                if i_pll != i_pl:
                 n_1=r.randint(1,4)
                 sn_1=d.distributeItems(canvas,playsub(i_pll[0]),n_1)
                 showsn1=c.showImage(sn_1,'play1')
            #show item i item in canvas
            showsn=c.showImage(sn,'play')

            #ask user question
            ans_p=input('Listen to the word. How many of them can you find? ')
            if int(ans_p) == n:
             cont=input('Right! Press Enter to continue')
            else:
             print('Sorry, there were',n)
             cont=input('Press Enter to continue')
#exit


def exit():
    print()

menu()
chooseinmenu()














