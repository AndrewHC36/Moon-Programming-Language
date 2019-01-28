from src.state import *

fname = "../testing.mn" #input("File Name: ")

with open(fname, "r") as fobj:
    fdt = fobj.readlines()
    PROGRAM = OUT
    for line in fdt:
        token = line.split(".")
        if token[0] == "@":
            if token[1] == "begin":
                PROGRAM = IN
            elif token[1] == "end":
                PROGRAM = OUT
        if PROGRAM == IN:
            if token[0] == "print":
                print(token[1])


# testing.shc