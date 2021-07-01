# Christmas Program

import os
import time
import random

# Easy song Subroutine

def easy():
  randomNum = random.randint(1,5)

  if randomNum == 1:

    TGREEN =  '\033[32m' # Green Text
    print(TGREEN + '''
Finish the song:
We wish you a merry christmas,
we wish you a merry christmas,
We wish you a merry christmas...
[what comes next?! (please type in lower case with no punctuation)]:
    ''')
    answer = input()

    time.sleep(2)

    if answer == "and a happy new year":
      print(TGREEN + "Well done! You got it right!")
      time.sleep(2)
      exit("Merry Christmas!")
    else:
      print(TGREEN + "Tough luck, you got it wrong!")
      time.sleep(2)
      exit("Merry Christmas!")
    
  elif randomNum == 2:
    TGREEN =  '\033[32m' # Green Text
    print(TGREEN + '''
Finish the song:
Jingle bells,
Jingle bells...
[what comes next?! (please type in lower case with no punctuation)]:
    ''')
    answer = input()

    time.sleep(2)

    if answer == "jingle all the way":
      print(TGREEN + "Well done! You got it right!")
      time.sleep(2)
      exit("Merry Christmas!")
    else:
      print(TGREEN + "Tough luck, you got it wrong!")
      time.sleep(2)
      exit("Merry Christmas!")

  elif randomNum == 3:
    TGREEN =  '\033[32m' # Green Text
    print(TGREEN + '''
Finish the song:
We three kings of Orient are...
[what comes next?! (please type in lower case with no punctuation)]:
    ''')
    answer = input()

    time.sleep(2)

    if answer == "bearing gifts" or answer == "bearing gifts we traverse afar":
      print(TGREEN + "Well done! You got it right!")
      time.sleep(2)
      exit("Merry Christmas!")
    else:
      print(TGREEN + "Tough luck, you got it wrong!")
      time.sleep(2)
      exit("Merry Christmas!")
    
  elif randomNum == 4:
    TGREEN =  '\033[32m' # Green Text
    print(TGREEN + '''
Finish the song:
Hark! The herald angels sing...
[what comes next?! (please type in lower case with no punctuation)]:
    ''')
    answer = input()

    time.sleep(2)

    if answer == "glory to the newborn king":
      print(TGREEN + "Well done! You got it right!")
      time.sleep(2)
      exit("Merry Christmas!")
    else:
      print(TGREEN + "Tough luck, you got it wrong!")
      time.sleep(2)
      exit("Merry Christmas!")

  elif randomNum == 5:
    TGREEN =  '\033[32m' # Green Text
    print(TGREEN + '''
Finish the song:
Silent night...
[what comes next?! (please type in lower case with no punctuation)]:
    ''')
    answer = input()

    time.sleep(2)

    if answer == "holy night":
      print(TGREEN + "Well done! You got it right!")
      time.sleep(2)
      exit("Merry Christmas!")
    else:
      print(TGREEN + "Tough luck, you got it wrong!")
      time.sleep(2)
      exit("Merry Christmas!")
    
    

      

# Medium song Subroutine

def medium():
  
  randomNum = random.randint(1,5)
  
  if randomNum == 1:
    
    TGREEN =  '\033[32m' # Green Text
    print(TGREEN + '''
Finish the song:
Jingle bell,
Jingle bell,
Jingle bell ______
[what goes on the underscore?! (please type in lower case with no punctuation)]:
  ''')
    answer = input()

    time.sleep(2)

    if answer == "rock":
      print(TGREEN + "Well done! You got it right!")
      time.sleep(2)
      exit("Merry Christmas!")
    else:
      print(TGREEN + "Tough luck, you got it wrong!")
      time.sleep(2)
      exit("Merry Christmas!")

  elif randomNum == 2:

    TGREEN =  '\033[32m' # Green Text
    print(TGREEN + '''
Finish the song:
Santa tell me,
if your really there...
[what comes next?! (please type in lower case with no punctuation)]:
  ''')
    answer = input()

    time.sleep(2)

    if answer == "dont make me fall in love again":
      print(TGREEN + "Well done! You got it right!")
      time.sleep(2)
      exit("Merry Christmas!")
    else:
      print(TGREEN + "Tough luck, you got it wrong!")
      time.sleep(2)
      exit("Merry Christmas!")

  elif randomNum == 3:

    TGREEN =  '\033[32m' # Green Text
    print(TGREEN + '''
Finish the song:
Rockin' around the Christmas tree
Have a happy holiday
Everyone dancin' merrily...
[what comes next?! (please type in lower case with no punctuation)]:
  ''')
    answer = input()

    time.sleep(2)

    if answer == "in the new old fashioned way":
      print(TGREEN + "Well done! You got it right!")
      time.sleep(2)
      exit("Merry Christmas!")
    else:
      print(TGREEN + "Tough luck, you got it wrong!")
      time.sleep(2)
      exit("Merry Christmas!")

  elif randomNum == 4:
    
    TGREEN =  '\033[32m' # Green Text
    print(TGREEN + '''
Finish the song:
You know Dasher and Dancer and Prancer and Vixen
Comet and Cupid and Donner and Blitzen
But do you recall...
[what comes next?! (please type in lower case with no punctuation)]:
  ''')
    answer = input()

    time.sleep(2)

    if answer == "the most famous reindeer of all":
      print(TGREEN + "Well done! You got it right!")
      time.sleep(2)
      exit("Merry Christmas!")
    else:
      print(TGREEN + "Tough luck, you got it wrong!")
      time.sleep(2)
      exit("Merry Christmas!")

  elif randomNum == 5:

    TGREEN =  '\033[32m' # Green Text
    print(TGREEN + '''
Finish the song:
It's beginning to look a lot like Christmas
Toys in every store
But the prettiest sight to see is the holly that will be...
[what comes next?! (please type in lower case with no punctuation)]:
  ''')
    answer = input()

    time.sleep(2)

    if answer == "on your own front door":
      print(TGREEN + "Well done! You got it right!")
      time.sleep(2)
      exit("Merry Christmas!")
    else:
      print(TGREEN + "Tough luck, you got it wrong!")
      time.sleep(2)
      exit("Merry Christmas!")



  
# Hard song Subroutine

def hard():

  randomNum = random.randint(1,2)

  if randomNum == 1:
    TGREEN =  '\033[32m' # Green Text
    print(TGREEN + '''
Finish the song:
Once bitten and twice shy
I keep my distance, but you still catch my eye...
[what comes next?! (please type in lower case with no punctuation)]:
    ''')
    answer = input()

    time.sleep(2)

    if answer == "tell me baby" or answer == "tell me baby do you recognise me":
      print(TGREEN + "Well done! You got it right!")
      time.sleep(2)
      exit("Merry Christmas!")
    else:
      print(TGREEN + "Tough luck, you got it wrong!")
      time.sleep(2)
      exit("Merry Christmas!")

  elif randomNum == 2:
    TGREEN =  '\033[32m' # Green Text
    print(TGREEN + '''
Finish the song:
Where nothing ever grows
No rain nor rivers flow...
[what comes next?! (please type in lower case with no punctuation)]:
    ''')
    answer = input()

    time.sleep(2)

    if answer == "do they know its christmas time" or answer == "do they know its christmas time at all":
      print(TGREEN + "Well done! You got it right!")
      time.sleep(2)
      exit("Merry Christmas!")
    else:
      print(TGREEN + "Tough luck, you got it wrong!")
      time.sleep(2)
      exit("Merry Christmas!")



# Wait Subroutine

def wait(timer):

  import time
  import datetime

  timerLoop = 1

  currantTime = datetime.datetime.now()
  dateTime = datetime.datetime.now()
  unixtime = time.mktime(dateTime.timetuple())

  timeStamp = unixtime

  while timerLoop == 1:
    if timer <= 0:
     timerLoop = 0

    currantTime = datetime.datetime.now()
    dateTime = datetime.datetime.now()
    unixtime = time.mktime(dateTime.timetuple())

    if unixtime == timeStamp + 1:
      currantTime = datetime.datetime.now()
      dateTime = datetime.datetime.now()
      unixtime = time.mktime(dateTime.timetuple())
      timeStamp = unixtime

      timer = timer - 1


# Loading Sub Routine
def loading(timeLoad):
  while timeLoad > 0:
    os.system('clear')
    TRED =  '\033[31m' # Red Text
    print(TRED + "Loading")
    time.sleep(0.25)
    os.system('clear')
    print(TRED + "Loading.")
    time.sleep(0.25)
    os.system('clear')
    print(TRED + "Loading..")
    time.sleep(0.25)
    os.system('clear')
    print(TRED + "Loading...")
    time.sleep(0.25)
    timeLoad = int(timeLoad) - 1
  
  os.system('clear')
  print("Loading complete")
  time.sleep(1)
  os.system('clear')

loading(5)

wait(2)

TGREEN =  '\033[32m' # Green Text

print(TGREEN + "Welcome to Christmas lyric guesser!")

wait(3)

print("Time for a song!")

wait(3)

choice = input("Would you like easy [enter 1], medium [enter 2] or hard [enter 3]: ")

wait(2)

print("Great!")

wait(3)

loading(3)

if choice == "1":
  answer = easy()
elif choice == "2":
  answer = medium()

elif choice == "3":
  answer = hard()

else:
  answer = exit("Thats not an option!")

