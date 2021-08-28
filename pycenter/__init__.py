# billythegoat356

# https://github.com/billythegoat356

# Version : 1.7

# <3


from os import get_terminal_size



def center(var: str, space: int = None, icon: str = " ", sep: bool = False):

    if space is None:
        space = (get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    if sep:
        return "\n".join((icon * int(space)) + var for var in var.splitlines())
    else:
        return "\n".join((icon * int(space)) + var + icon * int(space) for var in var.splitlines())
