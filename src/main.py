from src.state import *
import src.exception as exception

fname = "../testing.mn" #input("File Name: ")

with open(fname, "r") as fobj:
    fdt = fobj.readlines()
    PROGRAM = OUT
    LINE = -1
    STACK_FRAME = {}

    for line in fdt:
        LINE += 1
        token = line.strip("\n").split(".")
        if token[0] == "@":
            if token[1] == "begin":
                PROGRAM = IN
            elif token[1] == "end":
                PROGRAM = OUT
        elif PROGRAM == IN:
            if token[0] == "print":
                if token[1] == "use":
                    print(STACK_FRAME[token[2]])
                elif token[1] == "not":
                    print(token[2])
            elif token[0] == "set":
                if token[1] == "str":
                    STACK_FRAME[token[2]] = token[3]
                elif token[1] == "int":
                    STACK_FRAME[token[2]] = int(token[3])
            elif token[0] == "add":  # add
                if token[1] == "use":
                    if token[2] == "new":
                        STACK_FRAME[token[3]] = STACK_FRAME[token[4]]+STACK_FRAME[token[5]]
                    else:
                        STACK_FRAME[token[3]] = STACK_FRAME[token[3]]+STACK_FRAME[token[4]]
                elif token[1] == "not":
                    print(token[2])
            elif token[0] == "sub":  # subtraction
                if token[1] == "use":
                    if token[2] == "new":
                        STACK_FRAME[token[3]] = STACK_FRAME[token[4]]-STACK_FRAME[token[5]]
                    else:
                        STACK_FRAME[token[3]] = STACK_FRAME[token[3]]-STACK_FRAME[token[4]]
                elif token[1] == "not":
                    print(token[2])
            elif token[0] == "mlp":  # multiply
                if token[1] == "use":
                    if token[2] == "new":
                        STACK_FRAME[token[3]] = STACK_FRAME[token[4]]*STACK_FRAME[token[5]]
                    else:
                        STACK_FRAME[token[3]] = STACK_FRAME[token[3]]*STACK_FRAME[token[4]]
                elif token[1] == "not":
                    print(token[2])
            elif token[0] == "div":  # division
                if token[1] == "use":
                    if token[2] == "new":
                        STACK_FRAME[token[3]] = STACK_FRAME[token[4]]/STACK_FRAME[token[5]]
                    else:
                        STACK_FRAME[token[3]] = STACK_FRAME[token[3]]/STACK_FRAME[token[4]]
                elif token[1] == "not":
                    print(token[2])
            elif token[0] == "nop": pass
            else:
                raise exception.ProgramError("Line {0}: Invalid code".format(LINE))

# testing.shc