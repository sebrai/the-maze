import random as r
from typing import Callable
def hey(): print('hey')  
def hi():print('hi')
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

class Spiller():
      def __init__(self, hp:int, Room:dict[str,int]):
            self.hp=hp
            self.Room = Room
s = Spiller(10,{'x':1,'y':1})