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

def _sort_list(l:list)->list:
    l = sorted(l)
    return list(print_sorted(x) for x in l)

def _sort_set(s:set)->set:
    s = sorted([s.copy()])
    return set(print_sorted(x) for x in s[0])

def _sort_dict(d:dict)->dict:
    return  {k: print_sorted(v) for k, v in sorted(d.items(), key=lambda x: x[0])}

def _sort_tuple(t:tuple)->tuple:
    t = sorted(t)
    for x in t:
        print_sorted
    return tuple(print_sorted(x) for x in t)

def print_sorted(obj):
    if(obj.__class__ == list):
        obj = _sort_list(obj)
    elif(obj.__class__ == set):
        obj = _sort_set(obj)
    elif(obj.__class__ == dict):
        obj = _sort_dict(obj)
    elif(obj.__class__ == tuple):
        obj = _sort_tuple(obj)
    return obj

def find_root():
    assert False, "not implemented yet"