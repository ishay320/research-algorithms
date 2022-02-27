from typing import Callable


def safe_call(f: Callable, **kwargs):
    # check if the first is function
    if callable(f):
        # check the kwargs arguments
        function_args: dict = f.__annotations__.copy()
        function_args.pop("return", None)
        for key in kwargs:
            if key not in function_args:  # check for bound
                if key in f.__code__.co_varnames:  # check if not annotated
                    continue
                raise TypeError('ERROR: arg "' + key +
                                '" is not arg of the function')

            if type(kwargs[key]) is function_args[key]:
                function_args.pop(key, None)
            else:
                raise TypeError('ERROR: expected arg "' + key + '" to be ' +
                                str(function_args[key]) + " but got " +
                                str(type(kwargs[key])))
    return f(**kwargs)

def sort_list(l:list)->list:
    l = l.copy()
    l.sort()
    return l

def sort_set(s:set)->set:
    s = [s.copy()]
    s.sort()
    return s[0]

def sort_dict(d:dict)->dict:
    return  {k: v for k, v in sorted(d.items(), key=lambda x: x[0])}

def sort_tuple(t:tuple)->tuple:
    t = sorted(t)
    return tuple(t)


def print_sorted(obj:set):
    if(obj.__class__ == list):
        obj = sort_list(obj)
    elif(obj.__class__ == set):
        obj = sort_set(obj)
    elif(obj.__class__ == dict):
        obj = sort_dict(obj)
    elif(obj.__class__ == tuple):
        obj = sort_tuple(obj)
    # maybe function for every type and like recursive but wide
    return obj

def find_root():
    assert False, "not implemented yet"