
class lastcall:
    def __init__(self, func):
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
