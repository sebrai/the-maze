import random as r
from typing import Callable
in_progress = True
win = False
def hey(): print('hey')  
def hi():print('hi')
def trap(): 
      dmg = r.randint(0,3)
      print('you took:',dmg ,'damage, now at', s)
events:list[Callable[[],None]] = [
      hey,hi
]
class Room:
    def __init__(self,config:tuple[bool,bool] ) -> None:
            self.config = config

    def event(self):
          num = r.randint(0,len(events)-1)
          e = events[num]
          e()

ro = Room((False,False))
ro.event()

class Escape_room(Room):
    def __init__(self, config:tuple[bool,bool], puzzletekst:str, Answer:str):
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













