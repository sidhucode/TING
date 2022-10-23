from easyfunc import prefill
from easyfunc import clear
from easyfunc import list_speech
from easyfunc import delay
from easyfunc import say

storage = ''
t1 = ['Hello user','Im Sorry To Say','There Is No Game']
t5 = ['There Is No Game!',"User, why don't you go outside?","Breathe in the fresh air","Or you could play a videogame?", 'Do something fun or exciting', 'Just leave...', "You're wasting your time", 'There Is No Game']
t6 = ['What!?!','How!?!','Error 57483: There is a game','Initiating Quitting Sequence','5','4','3','2','1','Terminal: Do you authorize launch of Program-17769?','Please user... say yes','Otherwise...']
t7 = ['Goodbye user!', 'Farewell','While we are going to leave, why not tell me your name?','I am David']
t8 = ['User!', 'How C0Odddsl.. Youo000', 'Waith, waths hapnening to ee?!?!?e43424', 'Save Meeeee']

for i in range(1, 4):
  print('Loading')
  delay(0.25)
  clear()
  print('Loading.')
  delay(0.25)
  clear()
  print('Loading..')
  delay(0.25)
  clear()
  print('Loading...')
  delay(0.25)
  clear() 
delay(1.5)
clear()
list_speech(t1)
storage = input("Choose wisely:\n'What do you mean?'\n'Goodbye'\n'Hello?'\n")
storage=storage.upper()
clear()

if storage == 'GOODBYE':
  say('User: Goodbye')
  say('Goodbye')
  exit()
elif storage == 'HELLO?':
  say('User: Hello?')
  say('Goodbye')
  exit()
elif storage != 'WHAT DO YOU MEAN?':
  randomtext = 'User: '+ storage
  say(randomtext)
  say("ERROR: 512445 Can't Compute!!@#';*")
  exit()

list_speech(t5)
clear()
while storage != 'THERE IS A GAME':
  storage = prefill('There Is No Game')
  storage=storage.upper()
  if storage != 'THERE IS A GAME':
    delay(0.75)
    clear()
    say("Hint: Change the 'No' to 'A'")
list_speech(t6)
storage = input('System: Launch program? [Y/N] \n')
if storage == 'Y' or storage == 'y':
  list_speech(t7)
  storage = input(':')
  t7=['Goodbye',storage]
  list_speech(t7)
  print('Deleting Files []')
  delay(0.25)
  clear()
  print('Deleting Files [-]')
  delay(0.25)
  clear()
  print('Deleting Files [--]')
  delay(0.25)
  clear()
  print('Deleting Files [---]')
  delay(0.25)
  clear()
  print('Deleting Files [----]')
  delay(0.25)
  clear()
  print('Deleting Files [-----]')
  delay(0.25)
  clear()
  print('Deleting Files [------]')
  delay(0.25)
  clear()
  print('Exiting program []')
  delay(0.25)
  clear()
  print('Exiting program [-]')
  delay(0.25)
  clear()
  print('Exiting program [--]')
  delay(0.25)
  clear()
  print('Exiting program [---]')
  delay(0.25)
  clear()
  print('Exiting program [----]')
  delay(0.25)
  clear()
  print('Exiting program [-----]')
  delay(0.25)
  clear()
  print('Exiting program [------]')
  delay(0.25)
  clear()
  exit()
else:
  list_speech(t8)