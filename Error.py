class UnderflowError(Exception):
    def __init__(self,message="The stack is empty"):
        self.message=message
        super().__init__(message)
