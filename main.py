import random as r
from typing import Callable
in_progress = True
win = False
def hey(): print('hey')  
def hi():print('hi')
def trap1(): 
      dmg = r.randint(0,3)
      if dmg<0:
            print('you were hit by an arrow. you took:',dmg ,'damage, now at', s.get_hp())
      else:
            print("You dodged an arrow. you took:",dmg ,"damage")
      s.take_dmg(dmg)

def trap2():
      dmg = r.randint(4,6)
      print('you took:',dmg ,'damage, now at', s.get_hp())
      s.take_dmg(dmg)

def trap3():
      dmg = round(s.get_hp()/2)
      print('you took:',dmg ,'damage, now at', s.get_hp())
      s.take_dmg(dmg)
def trap4():
      pass

events:list[Callable[[],None]] = [
      trap1,trap1,trap1,trap2,trap3,trap3
]

class Room:
    def __init__(self,config:tuple[bool,bool,bool] ) -> None:
            self._config = config

    def event(self):
          num = r.randint(0,len(events)-1)
          e = events[num]
          e()
    def get_config(self)-> tuple[bool,bool,bool]:
          return self._config

ro = Room((False,False,False))

class Escape_room(Room):
    def __init__(self, config:tuple[bool,bool,bool], puzzletekst:str, Answer:str):
            super().__init__(config)
            self.puzzletekst = puzzletekst
            self.Answer = Answer
    def event(self):
          print(self.puzzletekst)

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


dirs = ('left', 'forward','right')
curent_room = Room((r.choice([True,False]),r.choice([True,False]),r.choice([True,False])))
while in_progress:
    curent_room.event()
    paths = [val for flag, val in zip(curent_room.get_config(),dirs) if flag]
    direction = input('choose  a direction to move, possible directions: ()'+str(paths)+'): ')
    while not direction in paths:
        print(direction, ' was not an option, you may have mistyped')
        direction = input('choose  a direction to move, possible directions: ()'+str(paths)+'): ')
    curent_room = Room((r.choice([True,False]),r.choice([True,False]),r.choice([True,False])))

if win:
      pass
else:
      pass