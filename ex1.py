from typing import Callable
def safe_call(f:Callable, **kwargs):
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

        # # check the args arguments
        # print('function_args: ',function_args)
        # print('f.__code__.co_varnames: ',f.__code__.__annotations__)
        # print('args: ',args)
        # for i, key in enumerate(function_args): # FIXME: need to add the non annotated args
        #     if len(args) <= i:  # check for out of bound
        #         raise TypeError("ERROR: not enough args to send to function")
        #     if function_args[key] is not type(args[i]):
        #         raise TypeError("ERROR: expected in arg '" + str(key) + "' :" +
        #                         str(function_args[key]) + " but got " +
        #                         str(type(args[i])))
    return f(**kwargs)
