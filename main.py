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

class Escape_room(Room):
    def __init__(self, config:tuple[bool,bool], puzzletekst:str, Answer:str):
            super().__init__(config)
            self.puzzletekst = puzzletekst
            self.Answer = Answer
    def event(self):
          print(self.puzzletekst)

class Spiller():
      def __init__(self, hp:int):
            self.hp=hp
            self.Room = Room
s = Spiller(10)













