
# billythegoat356

# https://github.com/billythegoat356

# Version : 1.2

# <3


from os import get_terminal_size



def center(var, space=None):

    size = get_terminal_size().columns

    if not space:
        space = (size - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "".join(f"{(' ' * int(space)) + var}\n" for var in var.splitlines())
