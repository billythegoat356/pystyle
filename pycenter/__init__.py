# billythegoat356

# https://github.com/billythegoat356

# Version : 1.5

# <3


from os import get_terminal_size



def center(var:str, space:int=None):

    if space is None:
        space = (get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())
