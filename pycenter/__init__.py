# https://github.com/billythegoat356

# Version : 2.3

# <3


from os import get_terminal_size


def center(var: str, space: int = None, icon: str = " ", sep: bool = False):
    if not space:
        space = (get_terminal_size().columns -
                 len(var.splitlines()[int(len(var.splitlines())/2)])) / 2

    if not sep:
        return "\n".join((icon * int(space)) + var for var in var.splitlines())
    else:
        return "\n".join((icon * int(space)) + var + (icon * int(space)) for var in var.splitlines())


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


def makesimplebox(content: str):
    l = 1
    for c in content.splitlines():
        if len(c) > l:
            l = len(c)
    box = f"─{'═'*l}☆☆{'═'*l}─"
    return box + "\n" + center(content, l) + "\n" + box
