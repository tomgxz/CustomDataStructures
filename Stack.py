from Error import UnderflowError

class Stack(object):
    def __init__(self,size):
        self.object=[]
        self.size=size

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
