
# billythegoat356

# https://github.com/billythegoat356

# Version : 1.4

# <3


from os import get_terminal_size



def center(var:str, space:int=None):

    if not space:
        space = (get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())
