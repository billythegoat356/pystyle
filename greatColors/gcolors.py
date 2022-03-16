import os
import pystyle
import random
import threading
import time
import sys

nbr = int or str
text = str or bytes or int or float
mode = tuple or list

end = '\033[38;2;255;255;255m'
default = ''
debugChar = '#'
defaultNoneArgument = '_NDArg'
rand = random.randint
max_caracters = 9999
stdout = sys.stdout

class Color:

    def rgb(red: nbr = 0, green: nbr = 0, blue: nbr = 0):
        final = f'\033[38;2;{red};{green};{blue}m'
        return final

    blue = rgb(0, 0, 255)
    red = rgb(255, 0, 0)
    green = rgb(0, 255, 0)
    yellow = rgb(255, 255, 0)
    purple = rgb(100, 0, 255)
    pink = rgb(255, 0, 150)
    cyan = rgb(0, 100, 255)

    # Mixed colors

        # Blue

    blue_to_blue = [blue, blue]
    red_to_blue = [red, blue]
    green_to_blue = [green, blue]
    yellow_to_blue = [yellow, blue]
    purple_to_blue = [purple, blue]
    pink_to_blue = [pink, blue]
    cyan_to_blue = [cyan, blue]

        # Red

    blue_to_red = [blue, red]
    red_to_red = [red, red]
    green_to_red = [green, red]
    yellow_to_red = [yellow, red]
    purple_to_red = [purple, red]
    pink_to_red = [pink, red]
    cyan_to_red = [cyan, red]

        # Green

    blue_to_green = [blue, green]
    red_to_green = [red, green]
    green_to_green = [green, green]
    yellow_to_green = [yellow, green]
    purple_to_green = [purple, green]
    pink_to_green = [pink, green]
    cyan_to_green = [cyan, green]

        # Yellow

    blue_to_yellow = [blue, yellow]
    red_to_yellow = [red, yellow]
    green_to_yellow = [green, yellow]
    yellow_to_yellow = [yellow, yellow]
    purple_to_yellow = [purple, yellow]
    pink_to_yellow = [pink, yellow]
    cyan_to_yellow = [cyan, yellow]

        # Purple

    blue_to_purple = [blue, purple]
    red_to_purple = [red, purple]
    green_to_purple = [green, purple]
    yellow_to_purple = [yellow, purple]
    purple_to_purple = [purple, purple]
    pink_to_purple = [pink, purple]
    cyan_to_purple = [cyan, purple]

        # Pink

    blue_to_pink = [blue, pink]
    red_to_pink = [red, pink]
    green_to_pink = [green, pink]
    yellow_to_pink = [yellow, pink]
    purple_to_pink = [purple, pink]
    pink_to_pink = [pink, pink]
    cyan_to_pink = [cyan, pink]

    default = rgb(255, 255, 255)

    def alternative(color: text, returnAll: bool = False, gap: int = 125, numbers: int = 10):
        red, green, blue = Color.decode_rgb(color = color)
        all_colors = [
            Color.rgb(
                red = red + rand(0, gap),
                green = green + rand(0, gap),
                blue = blue + rand(0, gap),
            )
            for i in range(numbers)
        ]
        if not returnAll:
            final = random.choice(all_colors)
            return final
        final = all_colors
        return final

    def randomColor():
        final = f'\033[38;2;{rand(0, 255)};{rand(0, 255)};{rand(0, 255)}m'
        return final

    def decode_rgb(color: text):
        params = color.split(';')
        red = int(float(params[2]))
        green = int(float(params[3]))
        blue = int(float(params[4][:-1]))
        return red, green, blue

    def middleColor(colors: list, returnTuple: bool = False):
        r1, g1, b1 = Color.decode_rgb(colors[0])
        r2, g2, b2 = Color.decode_rgb(colors[1])
        relative_r = int((r1 + r2) / 2)
        relative_g = int((g1 + g2) / 2)
        relative_b = int((b1 + b2) / 2)
        if not returnTuple:
            final = f'\033[38;2;{relative_r};{relative_g};{relative_b}m'
            return final
        return relative_r, relative_g, relative_b


class Screen():

    def setTitle(title) -> None:
        os.system(f'title {title}' if os.name == 'nt' else '')

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def setSize(size: mode):
        size = list(size)
        os.system(f'mode {size[0]}, {size[1]}')

    def exit():
        os.system('exit')


    def crazy():
        while True:
            Screen.setSize((rand(0, 200), rand(0, 50)))
            Screen.setTitle(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') * 50)

class Text:

    def colorize(content: text, color) -> text:
        return Text.fade(colors = [color, color], content = content)
        #final = color + content + end
        #return final

    def getSpaceCenter(content: text) -> text:
        # Thanks to pystyle for this function : https://github.com/billythegoat356/pystyle
        col = os.get_terminal_size().columns
        var = content.splitlines()
        nvarl = max(len(v) for v in var if v.strip())
        return int((col - nvarl) / 2)

    def getYCenter(content: text) -> text:
        # Thanks to pystyle for this function : https://github.com/billythegoat356/pystyle
        line = os.get_terminal_size().lines
        var = content.splitlines()
        nvarl = len(var)
        return int((line - nvarl) / 2)

    def center(content: text):
        # Thanks to pystyle for this function : https://github.com/billythegoat356/pystyle
        return '\n'.join((' ' * Text.getSpaceCenter(content = content)) + var for var in content.splitlines())

    def yCenter(content: text):
        return '\n' * Text.getYCenter(content = content) + '\n'.join(content.splitlines()) + '\n' * Text.getYCenter(content = content)

    def multiCoulour(content: text, mode = 'block'):
        final = ''
        if mode == 'block':
            final = ''.join(f'\033[38;2;{rand(0, 255)};{rand(0, 255)};{rand(0, 255)}m' + letter for letter in content) + end
        if mode == 'lines':
            final = '\n'.join(f'\033[38;2;{rand(0, 255)};{rand(0, 255)};{rand(0, 255)}m' + line for line in content.splitlines()) + end
        return final

    def console(content: text, speed: nbr = 1):
        content = list(content)
        for letter in content:
            print(letter, end = '')
            stdout.write
            time.sleep(speed / len(content))

    def banner(banner: text, color: text):
        bannerRunning = True
        def _input():
            nonlocal bannerRunning
            while bannerRunning:
                a = input()
                os.system('cls' if os.name == 'nt' else 'clear')
                bannerRunning = False
        def _show():
            nonlocal bannerRunning
            while bannerRunning:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Text.yCenter(Text.fade([Color.alternative(color), Color.alternative(color)], content = center_banner) + '\n'))
                time.sleep(0.2)
        center_banner = Text.center(banner[1:])
        threading.Thread(target = _input).start()
        threading.Thread(target = _show).start()
        while bannerRunning:
            continue

    def fade(colors: list, content: text):
        fade1 = Color.middleColor(colors = colors)             # "-"--------------------------------------"-"
        fade2 = Color.middleColor(colors = [fade1, colors[1]]) # -------------------"-"-------------------"-"
        fade3 = Color.middleColor(colors = [fade1, colors[0]]) # "-"----------------"-"----------------------
        fade4 = Color.middleColor(colors = [fade2, colors[1]]) # -----------------------------"-"---------"-"
        fade5 = Color.middleColor(colors = [fade1, fade3])     # ---------"-"-------"-"----------------------
        fade6 = Color.middleColor(colors = [fade3, colors[0]]) # "-"------"-"--------------------------------
        fade7 = Color.middleColor(colors = [fade1, fade2])     # -------------------"-"-------"-"------------

        phs1 = colors[0]
        phs2 = fade6
        phs3 = fade3
        phs4 = fade5
        phs5 = fade1
        phs6 = fade7
        phs7 = fade2
        phs8 = fade4
        phs9 = colors[1]
        phs = [phs1, phs2, phs3, phs4, phs5, phs6, phs7, phs8, phs9]
        # return phs1 + debugChar*5 + phs2 + debugChar*5 + phs3 + debugChar*5 + phs4 + debugChar*5 + phs5 + debugChar*5 + phs6 + debugChar*5 + phs7 + debugChar*5 + phs8 + debugChar*5 + phs9 + debugChar*5
        final = ''
        phs_number = 0
        phs_mode = True
        for line in content.splitlines():
            for letter in list(line):
                final += f'{phs[phs_number]}{letter}'
                if phs_number == 0:
                    phs_mode = True
                elif phs_number == 8:
                    phs_mode = False
                if not phs_mode:
                    phs_number -= 1
                else:
                    phs_number += 1
            final += '\n'
            phs_mode = True
            phs_number = 0

        final = final[:-1]
        return final + end

    def table(color: text = Color.default, informations: mode = defaultNoneArgument):
        list_informations = list(informations)
        _table = """
"""
        for info in list_informations:
            line = color + f'[ ' + Color.default + str(list_informations.index(str(info))) + color + ' ]' + Color.default + f' {str(info)}' + end + '\n'
            _table += line
        return _table