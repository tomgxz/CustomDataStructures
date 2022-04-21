class Queue(object):
    def __init__(self,size):
        self.object=[]
        self.size=size

        for i in range(self.size):
            self.object.append(None)

        self.front=0
        self.end=0

    def isFull(self):
        if not self.isCircular(): return self.front==0 and self.end==self.size
        return self.end == self.front

    def isEmpty(self):
        return self.front == self.end

    def isCircular(self):
        return self.end < self.front

    def enQueue(self,item):
        assert not self.isFull()
        if self.end==self.size-1 and self.front < 0:
            self.object[0]=item
            self.end=0
        else:
            self.object[self.end]=item
            self.end+=1
        return None

    def deQueue(self):
        if self.isEmpty(): return None
        item=self.object[self.front]
        self.front+=1
        if self.front>=self.size: self.front=0
        return item

    full=property(isFull,None)
    empty=property(isEmpty,None)
    circular=property(isCircular,None)
