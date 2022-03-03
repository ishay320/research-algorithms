# this is example for testing ex2

def firstFun(a:int,b:str)-> list:
    '''
    this is first function
    '''
    return []

def secondFun(test:list,*args)-> str:
    '''
    this is second function
    '''
    return str(test)

class FirstClass(int):
    def __init__(self) -> None:
        super().__init__()
    def firstFunction(self,a:int,b:str):
        pass
