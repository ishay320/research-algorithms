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

def print_sorted():
    # maybe function for every type and like recursive but wide
    assert False, "not implemented yet"

def find_root():
    assert False, "not implemented yet"