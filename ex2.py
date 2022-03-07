
class lastcall:
    def __init__(self, func) -> None:
        self.func = func
        # init
        self.last_call = ""
        self.last_ret = ""

    def __call__(self, *args, **kwds):
        argument = str(args) + str(kwds) # combine to str for easy checking
        if argument == self.last_call:
            return f"I already told you that the answer is {self.last_ret}!"

        self.last_call = argument
        self.last_ret = self.func(*args, **kwds)
        return self.last_ret

class List(list):
    def __init__(self, list) -> None:
        super().__init__(list)

    def __getitem__(self, pos: int | tuple):
        if not isinstance(pos,tuple): # if only 1 num then send to super
            return super().__getitem__(pos)
        
        # make the return list
        tmp_list = super(List, self).__getitem__(pos[0])
        for x in pos[1:]:
            tmp_list = tmp_list[x]
        return tmp_list
