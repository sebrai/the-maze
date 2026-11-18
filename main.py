import random as r # imports
from typing import Callable #<- this is used so that functions can be used as a datatype 
in_progress = True # false when game is over or won
win = False # has player won
def trap1(): # traps
      dmg = r.randint(0,3)
      s.take_dmg(dmg)
      if dmg>0:
            print('you were hit by an arrow. you took:',dmg ,'damage, now at', s.get_hp(),"hp")
      else:
            print("You dodged an arrow. you took:",dmg ,"damage")
      

def trap2():
      dmg = r.randint(3,5)
      s.take_dmg(dmg)
      print('A blade swings out of the wall! You took', dmg, 'damage, now at', s.get_hp(),"hp")


def trap3():
      dmg = round(s.get_hp()/2)
      s.take_dmg(dmg)
      print('You step on a cursed rune and feel half your life drain away. You took', dmg, 'damage, now at', s.get_hp(),"hp")

def trap4():
      dmg=s.get_hp()
      s.take_dmg(dmg)
      print("you have fallen in a pittrap. you have died")
     

def heal(): # heals you
      if s.get_hp() >= 10:
            print('You found a potion, but you are already at full health.')
      else:
            amount = r.randint(2,4)
            new_hp = s.get_hp() + amount
            if new_hp > 10:
                  new_hp = 10
            s.set_hp(new_hp)
            print('You found a potion and healed to', s.get_hp(),"hp")
      
class Room: # objekt for room
    events:list[Callable[[],None]] = [ # list is specified to be a list of callables/functions 
      trap1,trap1,trap1,trap1,trap1,trap2,trap2,trap3,trap3,trap3,trap3,trap4,heal,heal,heal
      ] # elements can be called with events[index]()
    def __init__(self,config:tuple[bool,bool,bool] ) -> None:
            self._config = config # config is witch rooms the player can go to afterwards
            num = r.randint(0,len(Room.events)-1)
            self.e = Room.events[num]
    def event(self):
          self.e()
    def get_config(self)-> tuple[bool,bool,bool]:
          return self._config

ro = Room((False,False,False))


class Escape_room(Room):
      puzzles: list[tuple[str, str]] = [ # a list full of tuples with questions and answers 
      ("true or false: git pull puts your code on the internet: ", "false"),
      ("true or false: git push uploads your commits to GitHub: ", "true"),
      ("true or false: a variable can change its value while the program runs: ", "true"),
      ("true or false: 7 / 2 gives 3 in Python: ", "false"),
      ("true or false: HTML is a programming language: ", "false"),
      ("true or false: 1 byte is 8 bits: ", "true"),
      ("true or false: RAM keeps its data after the computer is turned off: ", "false"),
      ("true or false: == checks if two values are equal: ", "true"),
      ("true or false: Python starts counting list positions at 1: ", "false"),
      ("true or false: a while loop runs as long as its condition is true: ", "true"),
      ("what keyword do you use to make a function in Python?: ", "def"),
      ("what data type is the value True?: ", "bool"),
      ("what is 10 % 3?: ", "1"),
      ("what git command saves a snapshot of your changes?: ", "commit"),
      ("what is the output of print(len('maze'))?: ", "4"),
      ("what do we call a mistake in code that makes it behave wrong?: ", "bug"),
      ("in binary, what is 101 in decimal?: ", "5"),
      ("what symbol starts a comment in Python?: ", "#"),
      ("what does 'int' stand for?: ", "integer"),
      ("what is the result of 'a' + 'b' in Python?: ", "ab"),
      ("what does Bool stand for?: ","boolean")
      ]
      def __init__(self, config:tuple[bool,bool,bool], puzzletekst:str, Answer:str):
            super().__init__(config)
            self._puzzletekst = puzzletekst
            self._answer = Answer
      def event(self):
            a = input(self._puzzletekst+ ": ").strip().lower()
            global win, in_progress
            if a == self._answer:
                  win = True
                  in_progress = False
                  print('correct you are safe')
            else:
                  print('incorrect, you fell down a pitfall and took 3 dmg')
                  s.take_dmg(3)

class Spiller():
    def __init__(self, hp:int):
            self._hp=hp
    def get_hp(self):
          return self._hp
    def set_hp(self,new:int):
          self._hp = new
    def take_dmg(self,dmg:int):
          self.set_hp(self._hp - dmg)
          if self._hp <= 0:
                global in_progress
                in_progress = False
                print('you have died in the maze')
      
s = Spiller(10)

print("You have woken up in a dark and cold maze try and get out")

dirs = ('left', 'forward','right')
curent_room = Room((r.choice([True,False]),True,r.choice([True,False])))
while in_progress:
      paths = [val for flag, val in zip(curent_room.get_config(),dirs) if flag]
      direction = input('choose  a direction to move, possible directions: ('+str(paths).replace("['","").replace("']","").replace("', '", ", ").strip() +'): ')
      while not direction.strip().lower() in paths:
            print(direction, ' was not an option, you may have mistyped')
            direction = input('choose  a direction to move, possible directions: ('+str(paths)+'): ')
      if not (r.randint(1,6) == 6 and s.get_hp() < 5):
            curent_room = Room((r.choice([True,False]),True,r.choice([True,False])))
      else:
            a,b = r.choice(puzzles)
            curent_room = Escape_room((False,True,False),a,b)
      curent_room.event()

if win:
      print('you got out alive')
else:
      print('try again next time')
