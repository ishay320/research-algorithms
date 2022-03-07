# this is example for testing ex2
import math

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
    '''
    class doc
    '''
    x = 3
    def __init__(self) -> None:
        super().__init__()
        self.item = "item"

    def firstFunction(self,a:int,b:str):
        '''
        class function
        '''
        pass
