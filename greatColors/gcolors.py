# made by billythegoat356 and loTus01

# https://github.com/billythegoat356 https://github.com/loTus04

# Version : 1.2 (added Colors.StaticMIX)

# based on pyfade anc pycenter, R.I.P

# <3


from argparse import ArgumentError
import random
import colorsys
from os import name as _name, system as _system, get_terminal_size as _terminal_size
from sys import stdout as _stdout
from time import sleep as _sleep
from random import randint as rand
from threading import Thread as _thread

if _name == 'nt':
    from ctypes import c_int, c_byte, Structure, byref, windll

    class _CursorInfo(Structure):
        _fields_ = [("size", c_int),
                    ("visible", c_byte)]


class System:

    """
    5 functions:

        Init()       |      initialize the terminal to allow the use of colors
        Clear()      |      clear the terminal
        Title()      |      set the title of terminal, only for Windows
        Size()       |      set the size of terminal, only for Windows
        Command()    |      enter a shell command
    """

    def Init():
        _system('')

    def Clear():
        return _system("cls" if _name == 'nt' else "clear")

    def Title(title: str):
        if _name == 'nt':
            return _system(f"title {title}")

    def Size(x: int, y: int):
        if _name == 'nt':
            return _system(f"mode {x}, {y}")

    def Command(command: str):
        return _system(command)

class Cursor:

    """
    2 functions:

        HideCursor()      |      hides the white blinking in the terminal
        ShowCursor()      |      shows the white blinking in the terminal

    """

    def HideCursor():
        if _name == 'nt':
            Cursor._cursor(False)
        elif _name == 'posix':
            _stdout.write("\033[?25l")
            _stdout.flush()

    def ShowCursor():
        if _name == 'nt':
            Cursor._cursor(True)
        elif _name == 'posix':
            _stdout.write("\033[?25h")
            _stdout.flush()

    """ ! developper area ! """

    def _cursor(visible: bool):
        ci = _CursorInfo()
        handle = windll.kernel32.GetStdHandle(-11)
        windll.kernel32.GetConsoleCursorInfo(handle, byref(ci))
        ci.visible = visible
        windll.kernel32.SetConsoleCursorInfo(handle, byref(ci))


class _MakeColors:

    """ ! developper area ! """

    def _makeansi(col: str, text: str) -> str:
        return f"\033[38;2;{col}m{text}\033[38;2;255;255;255m"

    def _makergbcol(var1: list, var2: list) -> list:
        col = [_col for _col in var1[:12]]
        for _col in var2[:12]:
            col.append(_col)
        for _col in reversed(col):
            col.append(_col)
        return col

    def _start(color: str) -> str:
        return f"\033[38;2;{color}m"

    def _end() -> str:
        return "\033[38;2;255;255;255m"

    def _maketext(color: str, text: str, end: bool = False) -> str:
        end = _MakeColors._end() if end else ""
        return color+text+end

    def _getspaces(text: str) -> int:
        return len(text) - len(text.lstrip())

    def _makerainbow(*colors) -> list:
        colors = [color[:24] for color in colors]
        rainbow = []
        for color in colors:
            for col in color:
                rainbow.append(col)
        return rainbow


class Colors:

    """
    54 variables (colors)
    
    3 lists:
        static_colors      |      colors that are static, ex: 'red' (can't be faded)
        dynamic_colors     |      colors that are dynamic, ex: 'blue_to_purple' (can be faded)
        all_colors         |      every color of static_colors and dynamic_colors
        
    3 functions:
        StaticRGB()        |      create your own fix/static color
        DynamicRGB()       |      create your own faded/dynamic color (soon...)
        MiddleColor()      |      mix two static colors
        DynamixMIX()       |      mix two dynamix colors (soon...)
        Symbol()           |      create a colored symbol, ex: '[!]'
        Alternative()      |      return random alternative of a static color
        DecodeRGB()        |      return the RGB of a static color ex: 100, 0, 255


    """

    def StaticRGB(r: int, g: int, b: int) -> str:
        return _MakeColors._start(f"{r};{g};{b}")

    def DynamicRGB(r1: int, g1: int, b1: int, r2: int,
                   g2: int, b2: int) -> list: ...

    def DecodeRGB(color: str):
        params = color.split(';')
        red = int(float(params[2]))
        green = int(float(params[3]))
        blue = int(float(params[4][:-1]))
        return red, green, blue

    """ remake colors """

    def Alternative(color: str, returnAll: bool = False, gap: int = 125, numbers: int = 10):
        red, green, blue = Colors.DecodeRGB(color = color)
        all_colors = [
            Colors.StaticRGB(
                r = red + rand(0, gap),
                g = green + rand(0, gap),
                b = blue + rand(0, gap),
            )
            for i in range(numbers)
        ]
        if not returnAll:
            final = random.choice(all_colors)
            return final
        final = all_colors
        return final

    def MakeFade(colors: list) -> list:
        fade1 = Colors.MiddleColor(colors = colors)             # "-"--------------------------------------"-"
        fade2 = Colors.MiddleColor(colors = [fade1, colors[1]]) # -------------------"-"-------------------"-"
        fade3 = Colors.MiddleColor(colors = [fade1, colors[0]]) # "-"----------------"-"----------------------
        fade4 = Colors.MiddleColor(colors = [fade2, colors[1]]) # -----------------------------"-"---------"-"
        fade5 = Colors.MiddleColor(colors = [fade1, fade3])     # ---------"-"-------"-"----------------------
        fade6 = Colors.MiddleColor(colors = [fade3, colors[0]]) # "-"------"-"--------------------------------
        fade7 = Colors.MiddleColor(colors = [fade1, fade2])     # -------------------"-"-------"-"------------

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
        return phs

    def MiddleColor(colors: list, returnTuple: bool = False):
        r1, g1, b1 = Colors.DecodeRGB(colors[0])
        r2, g2, b2 = Colors.DecodeRGB(colors[1])
        relative_r = int((r1 + r2) / 2)
        relative_g = int((g1 + g2) / 2)
        relative_b = int((b1 + b2) / 2)
        if not returnTuple:
            final = f'\033[38;2;{relative_r};{relative_g};{relative_b}m'
            return final
        return relative_r, relative_g, relative_b

    def DynamixMIX(colors: list) -> list:
        fadeColor1 = colors[0]
        fadeColor2 = colors[1]
        mixed = [fadeColor1[-1], fadeColor2[0]]
        between = Colors.MakeFade(mixed)
        print(between)
        return fadeColor1 + between + fadeColor2

    """ symbols """

    def Symbol(symbol: str, col: str, col_left_right: str, left: str = '[', right: str = ']') -> str:
        return f"{col_left_right}{left}{col}{symbol}{col_left_right}{right}{Col.reset}"


    """ dynamic colors """

    black_to_white = ["m;m;m"]
    black_to_red = ["m;0;0"]
    black_to_green = ["0;m;0"]
    black_to_blue = ["0;0;m"]

    white_to_black = ["n;n;n"]
    white_to_red = ["255;n;n"]
    white_to_green = ["n;255;n"]
    white_to_blue = ["n;n;255"]

    red_to_black = ["n;0;0"]
    red_to_white = ["255;m;m"]
    red_to_yellow = ["255;m;0"]
    red_to_purple = ["255;0;m"]

    green_to_black = ["0;n;0"]
    green_to_white = ["m;255;m"]
    green_to_yellow = ["m;255;0"]
    green_to_cyan = ["0;255;m"]

    blue_to_black = ["0;0;n"]
    blue_to_white = ["m;m;255"]
    blue_to_cyan = ["0;m;255"]
    blue_to_purple = ["m;0;255"]

    yellow_to_red = ["255;n;0"]
    yellow_to_green = ["n;255;0"]

    purple_to_red = ["255;0;n"]
    purple_to_blue = ["n;0;255"]

    cyan_to_green = ["0;255;n"]
    cyan_to_blue = ["0;n;255"]

    red_to_blue = ...
    red_to_green = ...

    green_to_blue = ...
    green_to_red = ...

    blue_to_red = ...
    blue_to_green = ...

    rainbow = ...

    """ static colors """

    red = _MakeColors._start('255;0;0')
    green = _MakeColors._start('0;255;0')
    blue = _MakeColors._start('0;0;255')

    white = _MakeColors._start('255;255;255')
    black = _MakeColors._start('0;0;0')
    gray = _MakeColors._start('150;150;150')

    yellow = _MakeColors._start('255;255;0')
    purple = _MakeColors._start('255;0;255')
    cyan = _MakeColors._start('0;255;255')

    orange = _MakeColors._start('255;150;0')
    pink = _MakeColors._start('255;0;150')
    turquoise = _MakeColors._start('0;150;255')

    light_gray = _MakeColors._start('200;200;200')
    dark_gray = _MakeColors._start('100;100;100')

    light_red = _MakeColors._start('255;100;100')
    light_green = _MakeColors._start('100;255;100')
    light_blue = _MakeColors._start('100;100;255')

    dark_red = _MakeColors._start('100;0;0')
    dark_green = _MakeColors._start('0;100;0')
    dark_blue = _MakeColors._start('0;0;100')

    reset = white

    """ ! developper area ! """

    dynamic_colors = [
        black_to_white, black_to_red, black_to_green, black_to_blue,
        white_to_black, white_to_red, white_to_green, white_to_blue,

        red_to_black, red_to_white, red_to_yellow, red_to_purple,
        green_to_black, green_to_white, green_to_yellow, green_to_cyan,
        blue_to_black, blue_to_white, blue_to_cyan, blue_to_purple,

        yellow_to_red, yellow_to_green,
        purple_to_red, purple_to_blue,
        cyan_to_green, cyan_to_blue
    ]

    for color in dynamic_colors:
        col = 20
        reversed_col = 220

        dbl_col = 20
        dbl_reversed_col = 220

        content = color[0]
        color.pop(0)

        for _ in range(12):

            if 'm' in content:
                result = content.replace('m', str(col))
                color.append(result)

            elif 'n' in content:
                result = content.replace('n', str(reversed_col))
                color.append(result)

            col += 20
            reversed_col -= 20

        for _ in range(12):

            if 'm' in content:
                result = content.replace('m', str(dbl_reversed_col))
                color.append(result)

            elif 'n' in content:
                result = content.replace('n', str(dbl_col))
                color.append(result)

            dbl_col += 20
            dbl_reversed_col -= 20

    red_to_blue = _MakeColors._makergbcol(red_to_purple, purple_to_blue)
    red_to_green = _MakeColors._makergbcol(red_to_yellow, yellow_to_green)

    green_to_blue = _MakeColors._makergbcol(green_to_cyan, cyan_to_blue)
    green_to_red = _MakeColors._makergbcol(green_to_yellow, yellow_to_red)

    blue_to_red = _MakeColors._makergbcol(blue_to_purple, purple_to_red)
    blue_to_green = _MakeColors._makergbcol(blue_to_cyan, cyan_to_green)

    rainbow = _MakeColors._makerainbow(
        red_to_green, green_to_blue, blue_to_red)

    for col in [
            red_to_blue, red_to_green,
            green_to_blue, green_to_red,
            blue_to_red, blue_to_green
    ]:
        dynamic_colors.append(col)

    dynamic_colors.append(rainbow)

    static_colors = [
        red, green, blue,
        white, black, gray,
        yellow, purple, cyan,
        orange, pink, turquoise,
        light_gray, dark_gray,
        light_red, light_green, light_blue,
        dark_red, dark_green, dark_blue,
        reset
    ]

    all_colors = [color for color in dynamic_colors]
    for color in static_colors:
        all_colors.append(color)


Col = Colors


class Colorate:

    """
    7 functions:
        Static colors:

            Color()                 |            color a text with a static color
            Error()                 |            make an error with red text and advanced arguments

        Dynamic colors:

            Vertical()              |           fade a text vertically
            Horizontal()            |           fade a text horizontally
            Diagonal()              |           fade a text diagonally
            DiagonalBackwards()     |           fade a text diagonally but backwards
            RandColor()             |           randomize a text with a lot of colors

    """

    """ fix/static colors"""

    def Color(color: str, text: str, end: bool = True) -> str:
        return _MakeColors._maketext(color=color, text=text, end=end)

    def Error(text: str, color: str = Colors.red, end: bool = False, spaces: bool = 1, enter: bool = True, wait: int = False) -> str:
        content = _MakeColors._maketext(
            color=color, text="\n" * spaces + text, end=end)
        if enter:
            var = input(content)
        else:
            print(content)
            var = None

        if wait is True:
            exit()
        elif wait is not False:
            _sleep(wait)

        return var

    """ faded/dynamic colors"""

    def Vertical(color: list, text: str, speed: int = 1, start: int = 0, stop: int = 0) -> str:

        lines = text.splitlines()
        result = ""

        nstart = 0
        color_n = 0
        for lin in lines:
            colorR = color[color_n]
            result += " " * \
                _MakeColors._getspaces(
                    lin) + _MakeColors._makeansi(colorR, lin.strip()) + "\n"

            if nstart != start:
                nstart += 1
                continue

            if lin.rstrip():
                if (
                    stop == 0
                    and color_n + speed < len(color)
                    or stop != 0
                    and color_n + speed < stop
                ):
                    color_n += speed
                elif stop == 0:
                    color_n = 0
                else:
                    color_n = stop

        return result.rstrip()

    def Horizontal(color: list, text: str, speed: int = 1) -> str:
        lines = text.splitlines()
        result = ""

        for lin in lines:
            carac = list(lin)
            color_n = 0
            for car in carac:
                colorR = color[color_n]
                result += " " * \
                    _MakeColors._getspaces(
                        car) + _MakeColors._makeansi(colorR, car.strip())
                if color_n + speed < len(color):
                    color_n += speed
                else:
                    color_n = 0
            result += "\n"
        return result.rstrip()

    def Diagonal(color: list, text: str, speed: int = 1) -> str:
        lines = text.splitlines()
        result = ""
        color_n = 0
        for lin in lines:
            carac = list(lin)
            for car in carac:
                colorR = color[color_n]
                result += " " * \
                    _MakeColors._getspaces(
                        car) + _MakeColors._makeansi(colorR, car.strip())
                if color_n + speed < len(color):
                    color_n += speed
                else:
                    color_n = 1
            result += "\n"

        return result.rstrip()

    def DiagonalBackwards(color: list, text: str, speed: int = 1) -> str:

        lines = text.splitlines()
        result = ""
        resultL = ''
        color_n = 0
        for lin in lines:
            carac = list(lin)
            carac.reverse()
            resultL = ''
            for car in carac:
                colorR = color[color_n]
                resultL = " " * \
                    _MakeColors._getspaces(
                        car) + _MakeColors._makeansi(colorR, car.strip()) + resultL
                if color_n + speed < len(color):
                    color_n += speed
                else:
                    color_n = 0
            result = result + '\n' + resultL
        return result.strip()

    def RandColor(content: str, mode = 'block'):
        final = ''
        if mode == 'block':
            final = ''.join(f'\033[38;2;{rand(0, 255)};{rand(0, 255)};{rand(0, 255)}m' + letter for letter in content) + end
        if mode == 'lines':
            final = '\n'.join(f'\033[38;2;{rand(0, 255)};{rand(0, 255)};{rand(0, 255)}m' + line for line in content.splitlines()) + end
        return final


class Anime:

    """
    2 functions:
        Fade()                  |            make a small animation with a changing color text, using a dynamic color
        Move()                  |            make a small animation moving the text, available soon
        Bar()                   |            a fully customizable charging bar
        Anime()                 |            a mix between Fade() and Move(), available soon

    """

    def Fade(text: str, color: list, mode, time=True, interval=0.05, hide_cursor: bool = True, enter: bool = False):
        if hide_cursor:
            Cursor.HideCursor()

        if type(time) == int:
            time *= 15

        global passed
        passed = False

        if enter:
            th = _thread(target=Anime._input)
            th.start()

        if time is True:
            while True:
                if passed is not False:
                    break
                Anime._anime(text, color, mode, interval)
                ncolor = color[1:]
                ncolor.append(color[0])
                color = ncolor

        else:
            for _ in range(time):
                if passed is not False:
                    break
                Anime._anime(text, color, mode, interval)
                ncolor = color[1:]
                ncolor.append(color[0])
                color = ncolor

        if hide_cursor:
            Cursor.ShowCursor()

    def Move() -> None: ...

    def Bar(length, carac_0: str = '[ ]', carac_1: str = '[0]', color: list = Colors.white, mode=Colorate.Horizontal, interval: int = 0.5, hide_cursor: bool = True, enter: bool = False, center: bool = False):

        if hide_cursor:
            Cursor.HideCursor()

        if type(color) == list:
            while True:
                if length <= len(color):
                    break
                ncolor = [col for col in color]
                for col in ncolor:
                    color.append(col)

        global passed
        passed = False

        if enter:
            th = _thread(target=Anime._input)
            th.start()

        for i in range(length + 1):
            bar = carac_1 * i + carac_0 * (length - i)
            if passed is not False:
                break
            if type(color) == list:
                if center:
                    print(Center.XCenter(mode(color, bar)))
                else:
                    print(mode(color, bar))
                _sleep(interval)
                System.Clear()
            else:
                if center:
                    print(Center.XCenter(color + bar))
                else:
                    print(color + bar)
                _sleep(interval)
                System.Clear()

        if hide_cursor:
            Cursor.ShowCursor()

    def Anime() -> None: ...
    """ ! developper area ! """

    def _anime(text: str, color: list, mode, interval: int):
        _stdout.write(mode(color, text))
        _stdout.flush()
        _sleep(interval)
        System.Clear()

    def _input() -> str:
        global passed
        passed = input()
        return passed


class Write:
    """
    2 functions:
        Print()         |          print a text to the terminal while coloring it and with a fade and write effect
        Input()         |          same than Print() but adds an input to the end and returns its valor

    """

    def Print(text: str, color: list, interval=0.05, hide_cursor: bool = True, end: str = Colors.reset) -> None:

        if hide_cursor:
            Cursor.HideCursor()

        Write._write(text=text, color=color, interval=interval)

        _stdout.write(end)
        _stdout.flush()

        if hide_cursor:
            Cursor.ShowCursor()

    def Input(text: str, color: list, interval=0.05, hide_cursor: bool = True, input_color: str = Colors.reset, end: str = Colors.reset) -> str:

        if hide_cursor:
            Cursor.HideCursor()

        Write._write(text=text, color=color, interval=interval)

        valor = input(input_color)

        _stdout.write(end)
        _stdout.flush()

        if hide_cursor:
            Cursor.ShowCursor()

        return valor

    " ! developper area ! "

    def _write(text: str, color, interval: int):
        lines = list(text)
        if type(color) == list:
            while True:
                if len(lines) <= len(color):
                    break
                ncolor = [col for col in color]
                for col in ncolor:
                    color.append(col)

        n = 0
        for line in lines:
            if type(color) == list:
                _stdout.write(_MakeColors._makeansi(color[n], line))
            else:
                _stdout.write(color + line)
            _stdout.flush()
            _sleep(interval)
            if line.strip():
                n += 1


class Center:

    """
    2 functions:
        XCenter()                  |             center the given text in X cords
        YCenter()                  |             center the given text in Y cords
        Center()                   |             center the given text in X and Y cords

    """

    def XCenter(var: str, spaces: int = None, icon: str = " ", middle: bool = False):
        if spaces is None:
            spaces = Center._xspaces(var=var)

        if not middle:
            return "\n".join((icon * spaces) + var for var in var.splitlines())
        else:
            return "\n".join((icon * spaces) + var + (icon * int(spaces)) for var in var.splitlines())

    def YCenter(var: str, spaces: int = None, icon: str = "\n", middle: bool = False):
        if spaces is None:
            spaces = Center._yspaces(var=var)

        if not middle:
            return icon * spaces + "\n".join(var.splitlines())
        else:
            return icon * spaces + "\n".join(var.splitlines()) + icon * spaces

    def Center(var: str, xspaces: int = None, yspaces: int = None, xicon: str = " ", yicon: str = "\n", middle: bool = False) -> str:
        if xspaces is None:
            xspaces = Center._xspaces(var=var)

        if yspaces is None:
            yspaces = Center._yspaces(var=var)

        if not middle:
            var = yicon * yspaces + "\n".join(var.splitlines())
        else:
            var = yicon * yspaces + \
                "\n".join(var.splitlines()) + yicon * yspaces

        if not middle:
            return "\n".join((xicon * xspaces) + var for var in var.splitlines())
        else:
            return "\n".join((xicon * xspaces) + var + (xicon * int(xspaces)) for var in var.splitlines())

    """ ! developper area ! """

    def _xspaces(var: str):
        try:
            col = _terminal_size().columns
        except OSError:
            return 0
        varl = var.splitlines()
        nvarl = max(len(v) for v in varl if v.strip())
        return int((col - nvarl) / 2)

    def _yspaces(var: str):
        try:
            lin = _terminal_size().lines
        except OSError:
            return 0
        varl = var.splitlines()
        nvarl = len(varl)
        return int((lin - nvarl) / 2)


class Add:
    """
    1 function:
        Add()           |           allow you to add a text to another, and even center it

    """
    def Add(banner1, banner2, spaces=0, center=False):
        if center:
            split1 = len(banner1.splitlines())
            split2 = len(banner2.splitlines())
            if split1 > split2:
                spaces = (split1 - split2) // 2
            elif split2 > split1:
                spaces = (split2 - split1) // 2
            else:
                spaces = 0

        if spaces > max(len(banner1.splitlines()), len(banner2.splitlines())):
            # raise Banner.MaximumSpaces(f"Too much spaces [{spaces}].")
            spaces = max(len(banner1.splitlines()), len(banner2.splitlines()))

        ban1 = banner1.splitlines()
        ban2 = banner2.splitlines()

        ban1count = len(ban1)
        ban2count = len(ban2)

        size = Add._length(ban1)

        ban1 = Add._edit(ban1, size)

        ban1line = 0
        ban2line = 0
        text = ''

        for _ in range(spaces):

            if ban1count >= ban2count:
                ban1data = ban1[ban1line]
                ban2data = ''

                ban1line += 1

            else:
                ban1data = " " * size
                ban2data = ban2[ban2line]

                ban2line += 1

            text = text + ban1data + ban2data + '\n'
        while ban1line < ban1count or ban2line < ban2count:

            ban1data = ban1[ban1line] if ban1line < ban1count else " " * size
            ban2data = ban2[ban2line] if ban2line < ban2count else ""
            text = text + ban1data + ban2data + '\n'

            ban1line += 1
            ban2line += 1
        return text

    """ ! developper area ! """

    class MaximumSpaces(Exception):
        ...

    def _length(ban1):
        bigestline = 0

        for line in ban1:
            if len(line) > bigestline:
                bigestline = len(line)
        return bigestline

    def _edit(ban1, size):
        return [line + (size - len(line)) * " " for line in ban1]


class Box:
    """
    2 functions:
        SimpleCube()                  |             create a simple cube with the given text
        Lines()                       |             create a text framed by two lines

    """

    def Box(content: str, up_left: str, up_right: str, down_left: str, down_right: str, left_line: str, up_line: str, right_line: str, down_line: str) -> str:
        l = 0
        lines = content.splitlines()
        for a in lines:
            if len(a) > l:
                l = len(a)
        if l % 2 == 1:
            l += 1
        box = up_left + (up_line * l) + up_right + "\n"
        #box += "║ " + (" " * int(l / 2)) + (" " * int(l / 2)) + " ║\n"
        for line in lines:
            box += left_line + " " + line + (" " * int((l - len(line)))) + " " + right_line + "\n"
        box += down_left + (down_line * l) + down_right + "\n"
        return box


    def SimpleCube(content: str) -> str:
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

    def DoubleCube(content: str) -> str:
        return Box.Box(content, "╔═", "═╗", "╚═", "═╝", "║", "═", "║", "═")

    def Lines(content: str) -> str:
        # voir pour ajouter un argument pour personnaliser la ligne
        l = 1
        for c in content.splitlines():
            if len(c) > l:
                l = len(c)
        box = f"─{'═'*l}☆☆{'═'*l}─"
        addspace = round((len(box) - len(content)) / 2)
        if addspace % 2 == 0:
            addspace += 1

        return box + "\n" + addspace * " " + content + addspace * " " + "\n" + box

    def table(color: str = Colors.reset, informations: tuple or list = ()):
        list_informations = list(informations)
        _table = """
"""
        for info in list_informations:
            line = color + f'[ ' + Colors.reset + str(list_informations.index(str(info))) + color + ' ]' + Colors.reset + f' {str(info)}' + Colors.reset + '\n'
            _table += line
        return _table


System.Init()
