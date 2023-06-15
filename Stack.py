from Error import UnderflowError

class Stack(object):
    def __init__(self,size,initPopulate=True):
        self.object=[]
        self.size=size

        if initPopulate:
            for i in range(self.size):
                self.object.append(None)

        self.bottom=0
        self.top=0

    def __repr__(self):
        return str(self.object[:self.top])

    def __str__(self):
        return str(self.object)

    def isFull(self):
        return self.bottom==0 and self.top == self.size+1

    def isEmpty(self):
        return self.bottom == self.top == 0

    def push(self,item):
        if self.isFull(): raise OverflowError()
        self.object[self.top]=item
        self.top+=1

    def pop(self):
        if self.isEmpty(): raise UnderflowError()
        self.top-=1
        return self.object[self.top]

    full=property(isFull,None)
    empty=property(isEmpty,None)

"""

Create a program which emulates a processor Stack, the program should…

Have a maximum stack size of 10 items

Initially generate 5 items to populate the stack

After this, at random intervals up to 10 seconds, add a new item to the stack

Each item should have a random total task time of up to 7 seconds

The processor should work on the “top” task in the stack and if a job is complete it can leave, if a new task comes
the task can be paused – it does not need to be reset

To do this completely will require you to use threading to manage the task addition and processing.

"""

from random import randint
from threading import Thread
import time

class ProcessorStack(Stack):
    def __init__(self):
        super().__init__(10,initPopulate=False)
        self.threads=[]

        self.newProcessThread=Thread(target=self.newProcessRepeat)
        self.threads.append(self.newProcessThread)
        self.newProcessThread.start()

        self.currentTaskThreads=[]

    def newProcessRepeat(self):
        while True:
            time.sleep(randint(1,10))
            if not self.isFull(): self.push(randint(1,7))

    def queueTask(self):
        currentTask=self.object[self.top-1]
        

    def task(self,time,active=True):
        for i in range(time):
            if active:
                time.sleep(1)
