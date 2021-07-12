
# billythegoat356

# https://github.com/billythegoat356

# Version : 1.2

# <3


from os import get_terminal_size



def center(var, space=None):

    if not space:
        space = (get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "".join(f"{(' ' * int(space)) + var}\n" for var in var.splitlines())
