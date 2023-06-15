class UnderflowError(Exception):
    def __init__(self,message="The stack is empty"):
        self.message=message
        super().__init__(message)

# deprecated

#class SizeOverflowError(Exception):
    #def __init__(self,requestedSize,message="The requested stack size is too large (maximum 10)"):
        #self.message=message
        #self.requestedSize=requestedSize
        #super().__init__(message)

    #def __str__(self):
        #return f'{self.requestedSize} -> {self.message}'
