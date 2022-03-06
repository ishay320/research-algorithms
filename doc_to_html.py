import inspect
import sys
from tracemalloc import start
from typing import Callable


def eprint(*args, **kwargs) -> None:
    print(*args, file=sys.stderr, **kwargs)


def print_usage(file_name: str) -> None:
    split_filename = file_name.split(sep="\\")
    eprint(f"""\nUsage: {split_filename[-1]} <python file> <output file>\n""")


def parser(argv: list[str]):
    if (len(argv) != 3):
        print_usage(argv[0])
        exit(1)

    return (argv[1], argv[2])


def main(argv: list[str]):
    (input_name, output_name) = parser(argv)
    # TODO: print to file
    # with open(output_name) as output_file:
    try:
        print("python file name: " + input_name.removeprefix(".\\"))
        command_module = __import__(input_name[2:-3])

        for obj in dir(command_module): # if hidden continue
            if("__" == obj[:2]):
                continue

            print(obj + "  " + str(eval("type(command_module."+obj+")"))+" :") # name + type

            doc = eval("command_module." + obj + ".__doc__") # doc
            if(doc != None):
                print(str(doc)) 
            
            # function printing
            if(str(type(eval("command_module." + obj))) == "<class 'function'>"): 
                print("Function arguments:")
                for arg in eval("command_module." + obj + ".__code__.co_varnames"):
                    print("\t" + arg, end=' ')
                    if(arg in eval("command_module." + obj + ".__annotations__")):
                        print("| type: " + str(eval("command_module."+obj+".__annotations__")[arg]))
                    else:
                        print(" |")
                if('return' in eval("command_module." + obj + ".__annotations__")):
                    print()
                    print("return type: " + str(eval("command_module." + obj + ".__annotations__")['return']))

            # TODO: print class type
            # print(inspect.getmembers(eval("command_module." + obj )))
            print("------------------------")
            
    except ImportError as err:
        eprint(err)


if __name__ == "__main__":
    main(sys.argv)