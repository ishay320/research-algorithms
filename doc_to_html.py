import inspect
import sys


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

def print_name_doc(obj_name, module) -> str:
    tmp_string: str = ""
    tmp_string += (obj_name + "  " + str(eval("type(module."+obj_name+")"))+" :") # name + type
    tmp_string += "\n"
    doc = eval("module." + obj_name + ".__doc__") # doc

    if(doc != None):
        tmp_string += (str(doc)) 
    else:
        tmp_string += "\n"

    return tmp_string
    
def print_class(class_name, module) -> str:
    tmp_string: str = ""
    tmp_string += print_name_doc(class_name, module)
    for arg in inspect.getmembers(eval("module." + class_name),predicate=inspect.isfunction):
        tmp_string += "\n"
        tmp_string += print_function(arg[0],eval("module." +class_name))
    return tmp_string
  
def print_function(func_name, module) -> str:
    tmp_string: str = ""
    tmp_string += print_name_doc(func_name, module)

    tmp_string += ("Function arguments:\n")
    for arg in eval("module." + func_name + ".__code__.co_varnames"):
        tmp_string += ("\t" + arg)
        if(arg in eval("module." + func_name + ".__annotations__")):
            tmp_string += ("| type: " + str(eval("module." + func_name+".__annotations__")[arg])+ "\n")
        else:
            tmp_string += (" |\n")
    if('return' in eval("module." + func_name + ".__annotations__")):
        tmp_string += ("return type: " + str(eval("module." + func_name + ".__annotations__")['return'])+ "\n")
    return tmp_string

def main(argv: list[str]):
    (input_name, output_name) = parser(argv)
    tmp_string: str = ""
    try:
        tmp_string += ("python file name: " + input_name.removeprefix(".\\"))
        tmp_string += ("\n")

        command_module = __import__(input_name[2:-3])
        for obj in dir(command_module):  # run on what inside the file
            if("__" == obj[:2]):# if hidden continue
                continue

            # class printing 
            if(str(type(eval("command_module." + obj))) == "<class 'type'>"):
                tmp_string += print_class(obj, command_module)

            # function printing
            elif(str(type(eval("command_module." + obj))) == "<class 'function'>"): 
                tmp_string += print_function(obj, command_module)

            # module printing
            elif(str(type(eval("command_module." + obj))) == "<class 'module'>"): 
                tmp_string += print_name_doc(obj, command_module)

            # if not found then need to be added
            else:
                tmp_string += (obj + " (need to be added)  " + str(eval("type(command_module."+obj+")"))+" :") # name + type

            tmp_string += ("\n------------------------\n")
            
    except ImportError as err:
        eprint(err)
    
    # print to file
    with open(output_name,"w") as output_file:
        output_file.write(tmp_string)


if __name__ == "__main__":
    main(sys.argv)