# billythegoat356

# https://github.com/billythegoat356

# Version : 2.1

# <3


from os import get_terminal_size



def center(var: str, space: int = None, icon: str = " ", sep: bool = False):

    if space is None:
        space = (get_terminal_size().columns - max(int(len(v)/2) for v in var.splitlines())) / 2
    
    if not sep:
        return "\n".join((icon * int(space)) + var for var in var.splitlines())
    else:
        return "\n".join((icon * int(space)) + var + icon * int(space) for var in var.splitlines())


def makebox(content: str):
    l = 0
    lines = content.splitlines()
    for a in lines:
        if len(a) > l:
            l = len(a)
    if l % 2 == 1:
        l += 1
    box = "__" + ("_" * l) + "__\n"
    box += "| " + (" " * int(l / 2)) + (" " * int(l / 2)) + " |\n"
    for line in lines:
        box += "| " + line + (" " * int((l - len(line)))) + " |\n"
    box += "|_" + ("_" * l) + "_|\n"

    return box
