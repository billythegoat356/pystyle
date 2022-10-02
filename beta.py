r"""
Hi, Welcome to PyStyle V2
PyStyle V2 is a Syntax remodeling and advenced version of PyStyle.

The doc is not avaiable now, but later...
by Billythegoat356, LoTus01 and BlueRed
"""

import re
from typing import Union as _Union, Any as _Any, Iterator as _Iterator, Callable as _Callable, Optional as _Optional
from os import system as _system, get_terminal_size as _get_terminal_size, name as _name
import ctypes as _ctypes
from sys import stdout as _stdout
from time import sleep as _wait
from threading import Thread as _Thread


# GutHub https://github.com/billythegoat356/PyStyle
# Stats https://pepy.tech/project/PyStyle
# Package https://pypi.org/project/PyStyle

# + Added: ...
# @ Updated & Fixed: ...
# - Removed: ...



__title__: str = 'PyStyle V2'
__description__: str = 'The 2nd version of PyStyle'
__version__: str = '2.0'
__authors__: tuple[str, str, str] = ('Billythegoat356', 'LoTus01', 'BlueRed')
__doc__: str = '...'


_system('')
_terminal_size = _get_terminal_size()
_terminal_size = _terminal_size.lines, _terminal_size.columns
Stylizable: type


def _inDev(func: _Callable) -> _Callable:
    def wrapper(*args, **kw) -> None:
        raise NotImplementedError(
            f'{func.__module__}.{func.__qualname__} is not implemented in PyStyle and in developpement or has a bug '
            f'you can help us to resolve this problem: open a pull request or an issue on ' + (Col.Fade.ocean + 'github.com/billythegoat356/PyStyle')
        )
    return wrapper



class _ColorBase:

    def __radd__(self, other: str) -> str:
        return other + str(self)



class Color(_ColorBase):

    r"""
    Represent a color
    """

    __slots__ = ('rgb', 'hex', 'hsv', 'back')

    def __init__(self, rgb: tuple[int, int, int]) -> None:
        super().__init__(self)

        self.rgb: tuple[int, int, int] = tuple(rgb)
        self.hex: int = '#%02x%02x%02x' % self.rgb
        self.hsv: tuple[float, float, float] = ()

        maxColor = max(*rgb)
        minColor = min(*rgb)

        if minColor == maxColor:
            self.hsv = (0.0, 0.0, maxColor)

        else:
            s = (maxColor - minColor) /  maxColor
            rc = (maxColor - rgb[0]) / (maxColor - minColor)
            gc = (maxColor - rgb[1]) / (maxColor - minColor)
            bc = (maxColor - rgb[2]) / (maxColor - minColor)

            states = {
                rgb[0]: bc - gc,
                rgb[1]: float(2 + rc - bc)
            }

            h = states.get(maxColor, float(4 + gc - rc))
            h = float(float(h / 6) % 1)
            self.hsv = (h, s, maxColor)


    def __str__(self) -> str:
        return '\033[38;2;{};{};{}m'.format(*self.rgb)


    def __repr__(self) -> str:
        return f'Color{self.rgb}'


    def __mod__(self, other: 'Color') -> 'ColorList':
        return ColorList(self, other)


    @classmethod
    def FromHex(cls, hex: _Union[str, int]) -> 'Color':
        if isinstance(hex, str):
            hex = hex.lstrip('#')

        elif isinstance(hex, int):
            hex = f'{hex:02x}'

        rgb = tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))
        return cls(rgb)


    @classmethod
    def FromHSV(cls, hsv: tuple[float, float, float]) -> 'Color':
        r"""
        Create a color by it HSV code
        """

        rgb = ()
        if hsv[1] == 0.0:
            rgb = (hsv[2], hsv[2], hsv[2])

        i = int(hsv[0] * 6.0)
        f = (hsv[0] * 6.0) - i
        p = hsv[2] * (1.0 - hsv[1])
        q = hsv[2] * (1.0 - hsv[1] * f)
        t = hsv[2] * (1.0 - hsv[1] * float(1 - f))
        i %= 6

        states = {
            0: (hsv[2], t, p),
            1: (q, hsv[2], p),
            2: (p, hsv[2], t),
            3: (p, q, hsv[2]),
            4: (t, p, hsv[2]),
            5: (hsv[2], p, q)
        }

        rgb = states[i]
        rgb = tuple(int(color) for color in rgb)
        return cls(rgb)


    def __add__(self, other: _Union[str, 'Color', 'BackColor']) -> str:
        if not isinstance(other, (str, Color, BackColor)):
            raise TypeError(other)

        if isinstance(other, BackColor):
            return str(other) + str(self)

        elif isinstance(other, Color):
            return Colors.StaticMIX([self, other])

        elif isinstance(other, str):
            return str(self) + other + Col.reset


    def __eq__(self, other: 'Color') -> bool:
        if not isinstance(other, Color):
            return False

        return self.rgb == other.rgb


    def __ne__(self, other: 'Color') -> bool:
        return not self.__eq__(other)


    @staticmethod
    def rmAnsi(text: str) -> str:
        ansiRegex = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
        return ansiRegex.sub('', text)






class ColorList:
    
    def __init__(self, *colors: Color) -> None:
        self.colors: tuple[Color] = colors
        self.speed: int = 1


    def __str__(self) -> str:
        return str(self.fade)
        

    def __mod__(self, color: Color) -> 'ColorList':
        return ColorList(*self.colors + (color,))


    @property
    def fade(self) -> 'Fade':
        return Fade.FromColors(self.colors, self.speed)


    @property
    def mix(self) -> Color:
        return Col.StaticMIX(self.colors)



class AnsiCode:

    class CTRLCodes:
        CSI: str = '\033['
        OSC: str = '\033]'
        BEL: str = '\a'


    def __init__(self, ctrl_code: str, code: int, end: str = '') -> None:
        self.code: int = code
        self.ctrl_code: str = ctrl_code
        self.end: str = end


    def __str__(self) -> str:
        return f'{self.ctrl_code}{self.code}{self.end}'


    def __add__(self, other: str) -> str:
        return str(self) + other + Col.reset



class BackColor(AnsiCode):

    __slots__ = ('code',)
    
    def __init__(self, code: int) -> None:
        self.code: int = code
        super().__init__(AnsiCode.CTRLCodes.CSI, code)


    def __add__(self, other: _Union[str, Color, 'Fade']) -> str:
        if not isinstance(other, (str, Color, Fade)):
            raise TypeError(other)

        elif isinstance(other, str):
            return str(self) + other + Col.Back.reset

        if isinstance(other, Color):
            return str(self) + str(other)

        elif isinstance(other, Fade):
            return other + self



class Fade(_ColorBase):

    r"""
    Represent a fade of colors
    """

    __slots__ = ('colors', 'mode', 'absolute', 'back')

    horizontal: str = 'HORIZONTAL'
    vertical: str = 'VERTICAL'
    addType: str = _Union[str, BackColor, Color, 'Fade']


    def __init__(self, colors: list[Color], /, mode: str = horizontal) -> None:
        super().__init__(self)

        self.colors: list[Color] = colors
        self.mode: str = mode
        self.absolute: bool = False

        if len(self.colors) < 2:
            raise ValueError('Fade must have 2 or more colors')


    def __str__(self) -> str:
        return ''.join(str(col) for col in self.colors)


    def __add__(self, other: addType) -> addType:
        if isinstance(other, BackColor):
            return Fade(self.colors, self.mode, other)

        elif isinstance(other, Fade):
            return Col.DynamicMIX([self, other])

        elif isinstance(other, Color):
            return self + Fade.FromColors([self.colors[-1], other])

        elif not isinstance(other, Fade.addType.__args__):
            raise TypeError(other)

        colors = self.colors
        while len(other) >= len(self):
            colors += list(reversed(self.colors))

        if self.mode == Fade.horizontal:
            text = '\n'.join([
                ''.join(str(color) + char for color, char in zip(colors, line)) for line in other.splitlines()
            ]) + Colors.reset

        elif self.mode == Fade.vertical:
            if not self.absolute:
                text = '\n'.join(str(color) + other for color, other in zip(colors, other.split('\n'))) + Colors.reset
            else:
                text = '\n'.join(str(color) + str(color).join(other) for color, other in zip(colors, other.split('\n'))) + Colors.reset

        else:
            raise ValueError('Fade mode is not valid')

        return text


    def __len__(self) -> int:
        return len(self.colors)


    def __eq__(self, other: 'Fade') -> bool:
        if not isinstance(other, Fade):
            return False

        return all([
            self.colors == other.colors,
            self.mode == other.mode
        ])


    def __ne__(self, other: 'Fade') -> bool:
        return not self.__eq__(other)


    @property
    def mix(self) -> Color:
        return Col.StaticMIX(self.colors)


    @classmethod
    def FromColors(cls, colors: list[Color], speed: int = 1, **params) -> 'Fade':
        r"""
        Create a fade from some colors
        """

        all_fades = []
        only_2_colors = len(colors) == 2
        packed_colors = [colors[item:item + 2] for item in range(0, len(colors), 2)]

        for color_pack in packed_colors:
            if len(color_pack) == 1:
                color1, color2 = packed_colors[-2][1], color_pack[0]
            else:
                color1, color2 = color_pack

            colors = [Colors.Scale(color1, color2, index) for index in range(0, 100, 10)]
            all_fades.append(colors)

        all_colors = []

        if not only_2_colors:
            for fade in all_fades:
                try:
                    next_fade = all_fades[all_fades.index(fade) + 1]
                except:
                    next_fade = [all_fades[-1][-1]]
                start = fade[-1]
                end = next_fade[0]
                new_fade = cls.FromColors([start, end])
                final_fade = fade + new_fade.colors
                all_colors.extend(final_fade)
        else:
            all_colors = all_fades[0]

        final_colors = []
        for color in all_colors:
            final_colors.extend([color] * speed)

        return cls(final_colors, **params)



class Pattern:
    # NOTE: Pattern bug with fade and fade all the pattern,
    # If a fade is set, the default chars will be faded too

    r"""
    A pattern that color only specified characters in specified colors
    """

    def __init__(self, pattern: dict) -> None:
        self.pattern: dict[str, Stylizable] = pattern | {chr(99999): Col.white}
        self.fade: _Optional[Fade] = None
        self.chars: list[str] = list(pattern.keys())

        for color in pattern.values():
            if isinstance(color, Fade):
                if self.fade:
                    raise ValueError('Only one fade is allowed on a pattern')
                self.fade = color

        if self.fade:
            if self.fade.mode == Fade.vertical:
                self.fade.absolute = True


    def keys(self) -> _Iterator[str]:
        yield from self.chars


    def __getitem__(self, key: str) -> Stylizable:
        return self.pattern[key]


    def __iter__(self) -> _Iterator[tuple[str, Stylizable]]:
        yield from self.pattern.items()


    def Patternize(self, text: str) -> str:
        r"""
        Render the pattern with a text or a banner
        """

        if not isinstance(text, str):
            raise TypeError(text)

        if self.fade:
            text = self.fade + text

        for chars, color in self.pattern.items():
            if color == self.fade:
                continue

            for char in chars:
                text = text.replace(char, str(color) + char + Colors.reset)

        return text

Pattern.__slots__ = ('pattern', 'fade')



class _System:

    r"""
    1 functions:
        _System.GetTerminalSize: get the terminal size
    """

    def __init__(self) -> None:
        self._title: str = ''
        self._size: tuple[int, int] = _terminal_size
        self._cursor: bool = True


    @staticmethod
    def Clear() -> None:
        _stdout.write('\033[2J\033[1;1H')
        _stdout.flush()


    @property
    def cursor(self) -> bool:
        return self._cursor


    @cursor.setter
    def cursor(self, value: bool) -> None:
        if value:
            print('\u001b[?25h', end = '')
        else:
            print('\u001b[?25l', end = '')


    @property
    def size(self) -> tuple[int, int]:
        return self._size


    @size.setter
    def size(self, dimension: tuple[int, int]) -> None:
        if any(not isinstance(dim, int) for dim in dimension):
            raise TypeError('Size must be integers')

        x, y = dimension
        result = _system(f'mode {x}, {y}')

        if result != 0:
            raise SystemError('Could not set terminal size')

        global _terminal_size
        _terminal_size = (y, x)
        self._size = (y, x)


    @property
    def title(self) -> str:
        return self._title


    @title.setter
    def title(self, title: str) -> None:
        result = _ctypes.windll.kernel32.SetConsoleTitleA(title)
        if result != 0:
            result = _system(f'title {title}')

        if result != 0:
            raise SystemError('Could not set terminal title')

        self._title = title

System = _System()



class Styles:
    bold: AnsiCode = AnsiCode(AnsiCode.CTRLCodes.CSI, 1, 'm')
    underlined: AnsiCode = AnsiCode(AnsiCode.CTRLCodes.CSI, 4, 'm')
    reset: str = '\033[0m'



class Center:

    r"""
    3 functions:
        Center.XCenter: center the text on the x axis
        Center.YCenter: center the text on the y axis
        Center.Center: center the text on the x and y axis
    """

    def XCenter(text: str, all_lines: bool = False, **params) -> str:
        if all_lines:
            return '\n'.join(Center.XCenter(line, **params) for line in text.splitlines())

        max_line_width = max((len(line) for line in Color.rmAnsi(text).splitlines() if line.strip()), default = 0)
        spaces = round((_terminal_size[1] - max_line_width) / 2)

        return '\n'.join((params.get('icon', '\x20') * spaces) + line for line in text.splitlines())


    def YCenter(text: str) -> str:
        height = len(text.splitlines())
        spaces = round((_terminal_size[0] - height) / 2)

        text = ('\n' * spaces) + text
        return text


    def Center(text: str, all_lines: bool = False) -> str:
        return Center.XCenter(Center.YCenter(text), all_lines = all_lines)


    def Join(text1: str, text2: str, center: bool = True) -> str:
        spaces = 0

        if center:
            split1 = len(text1.splitlines())
            split2 = len(text2.splitlines())

            if split1 > split2:
                spaces = (split1 - split2) // 2
            elif split2 > split1:
                spaces = (split2 - split1) // 2
            else:
                spaces = 0

        if spaces > max(len(text1.splitlines()), len(text2.splitlines())):
            spaces = max(len(text1.splitlines()), len(text2.splitlines()))

        ban1 = text1.splitlines()
        ban2 = text2.splitlines()
        ban1count = len(ban1)
        ban2count = len(ban2)
        size = max((len(line) for line in ban1), default = 0)
        ban1 = [line + (size - len(line)) * ' ' for line in ban1]

        ban1line = 0
        ban2line = 0
        text = ''

        for _ in range(spaces):
            if ban1count >= ban2count:
                ban1data = ban1[ban1line]
                ban2data = ''
                ban1line += 1

            else:
                ban1data = ' ' * size
                ban2data = ban2[ban2line]
                ban2line += 1

            text += ban1data + ban2data + '\n'

        while ban1line < ban1count or ban2line < ban2count:
            ban1data = ban1[ban1line] if ban1line < ban1count else ' ' * size
            ban2data = ban2[ban2line] if ban2line < ban2count else ''
            text += ban1data + ban2data + '\n'

            ban1line += 1
            ban2line += 1

        return text


    def XDouble(text: str, sep: str = Styles.reset) -> str:
        # NOTE: this function remove the ANSI escape sequences in the colned part
        maxLine = max(len(line) for line in Color.rmAnsi(text).splitlines())
        text = '\n'.join(line + (' ' * (maxLine - len(Color.rmAnsi(line)))) if len(Color.rmAnsi(line)) < maxLine else line for line in text.splitlines())
        return '\n'.join(line + sep + Color.rmAnsi(line)[::-1] for line in text.splitlines())


    def YDouble(text: str, sep: str = '\n') -> str:
        return text + sep + '\n'.join(list(reversed(text.splitlines())))



class _Colors:

    r"""
    The colors and fade storage
    """

    red: Color = Color((255, 0, 0))
    green: Color = Color((0, 255, 0))
    blue: Color = Color((0, 0, 255))
    yellow: Color = Color((255, 255, 0))
    cyan: Color = Color((0, 255, 255))
    purple: Color = Color((150, 30, 225))
    pink: Color = Color((255, 110, 190))
    white: Color = Color((255, 255, 255))
    black: Color = Color((0, 0, 0))
    grey: Color = Color((128, 128, 128))
    gray: Color = grey
    dark_gray: Color = Color((64, 64, 64))
    light_gray: Color = Color((192, 192, 192))
    indigo: Color = Color((121, 28, 248))
    lime: Color = Color((134, 227, 7))
    orange: Color = Color((255, 165, 0))
    dark_blue: Color = Color((0, 0, 139))
    dark_green: Color = Color((0, 100, 0))
    dark_red: Color = Color((139, 0, 0))



    class Back:

        black: BackColor = BackColor(40)
        red: BackColor = BackColor(41)
        green: BackColor = BackColor(42)
        yellow: BackColor = BackColor(43)
        blue: BackColor = BackColor(44)
        magenta: BackColor = BackColor(45)
        cyan: BackColor = BackColor(46)
        white: BackColor = BackColor(47)
        reset: BackColor = BackColor(49)

        light_black: BackColor = BackColor(100)
        light_red: BackColor = BackColor(101)
        light_green: BackColor = BackColor(102)
        light_yellow: BackColor = BackColor(103)
        light_blue: BackColor = BackColor(104)
        light_magenta: BackColor = BackColor(105)
        light_cyan: BackColor = BackColor(106)
        light_white: BackColor = BackColor(107)

    
    class Fade:
        rainbow: Fade
        gold: Fade
        fire: Fade
        ocean: Fade
        hard: Fade

    static_colors = [
        red, green, blue,
        yellow, cyan, purple,
        pink, white, black,
        gray, dark_gray, light_gray,
        indigo, lime, orange,
        dark_blue, dark_green, dark_red
    ]

    reset: str = Styles.reset
    all: list[str]

    def __init__(self) -> None:
        for obj in dir(_Colors):
            if not obj.startswith('_'):
                setattr(self, obj, getattr(_Colors, obj))


    def __getattr__(self, name: str) -> _Any:
        all = [col_ for col_, ansi in vars(_Colors).items() if ansi in _Colors.static_colors]
        if name in vars(self).values():
            return vars(self)[name]

        elif name in vars(self):
            return vars(self)[name]

        if not '_to_' in name and not '_and_' in name:
            return vars(_Colors)[name]

        elif '_and_' in name:
            colors = name.split('_and_')
            for color in colors:
                if color not in all:
                    raise AttributeError(f'{color!r} is not a valid color')

            colors = [vars(self)[color] for color in colors]
            return Colors.StaticMIX(colors)

        colors = name.split('_to_')
        for color in colors:
            if color not in all:
                raise AttributeError(f'{color!r} is not a valid color')

        colors = [vars(self)[color] for color in colors]
        return Fade.FromColors(colors)


    @staticmethod
    def StaticMIX(colors: list[Color]) -> Color:
        return Color([
            sum(color.rgb[0] for color in colors) // len(colors),
            sum(color.rgb[1] for color in colors) // len(colors),
            sum(color.rgb[2] for color in colors) // len(colors)
        ])


    @staticmethod
    def DynamicMIX(fades: list[Fade]) -> Color:
        all_fades = []

        for fade in fades:
            last = False
            try:
                next_fade = fades[fades.index(fade) + 1]
            except IndexError:
                last = True
                next_fade = fades[-1]

            start_color = fade.colors[-1]
            end_color = next_fade.colors[0]

            all_fades.append(fade)
            new_fade = Fade.FromColors([start_color, end_color])
            if not last:
                all_fades.append(new_fade)

        colors = []
        for fade in all_fades:
            colors.extend(fade.colors)

        return Fade(colors)


    @staticmethod
    def Scale(color1: Color, color2: Color, scale: int) -> Color:
        red_colors = list(range(color1.rgb[0], color2.rgb[0])) or list(reversed(list(range(color2.rgb[0], color1.rgb[0])))) or [color1.rgb[0]]
        green_colors = list(range(color1.rgb[1], color2.rgb[1])) or list(reversed(list(range(color2.rgb[1], color1.rgb[1])))) or [color1.rgb[1]]
        blue_colors = list(range(color1.rgb[2], color2.rgb[2])) or list(reversed(list(range(color2.rgb[2], color1.rgb[2])))) or [color1.rgb[2]]

        red_scale = int((scale / 100) * len(red_colors)) if scale != 100 else len(red_colors) - 1
        green_scale = int((scale / 100) * len(green_colors)) if scale != 100 else len(green_colors) - 1
        blue_scale = int((scale / 100) * len(blue_colors)) if scale != 100 else len(blue_colors) - 1

        red_color = red_colors[int(red_scale)]
        green_color = green_colors[int(green_scale)]
        blue_color = blue_colors[int(blue_scale)]

        color = Color((red_color, green_color, blue_color))

        return color

Colors: _Colors = _Colors()
Colors.Fade.gold = Colors.orange_to_yellow
Colors.Fade.fire = Colors.orange_to_yellow_to_red
Colors.Fade.hard = Colors.red_to_black
Colors.Fade.ocean = Fade.FromColors([
    Colors.Scale(Colors.blue, Colors.dark_blue, 30),
    Colors.Scale(Colors.cyan, Colors.blue, 60),
    Colors.Scale(Colors.white, Colors.blue, 60),
])

Colors.Fade.rainbow = Fade.FromColors([
    Colors.red, Colors.orange, Colors.yellow, Colors.green, Colors.cyan, Colors.blue, Colors.dark_blue, Colors.purple
])

Colors.all = [col_ for col_, ansi in vars(_Colors).items() if ansi in _Colors.static_colors]

Col: _Colors = Colors




class Write:

    def Print(text: str, color: _Union[Fade, Color] = Colors.reset, interval: int = 0.01) -> None:
        cursor = System.cursor
        System.cursor = False

        all_colors = []
        pair = True

        if isinstance(color, Color):
            all_colors = [[color]] * len(text)

        elif isinstance(color, Fade):
            all_colors = [color.colors]
            while len(text) > len(all_colors):
                if pair:
                    all_colors.append(list(reversed(color.colors)))
                else:
                    all_colors.append(color.colors)
                pair = not pair

        elif color == Col.reset:
            color = ''
            all_colors = [color] * len(text)

        else:
            raise TypeError(color)

        colors = []
        for fade_part in all_colors:
            if isinstance(color, Fade):
                colors.extend(fade_part)
            else:
                colors.append(color)

        for letter, col in zip(text, colors):
            _stdout.write(col + letter)
            _stdout.flush()
            _wait(interval)
        
        if cursor == True:
            System.cursor = True


    def Input(prompt: str, color: _Union[Fade, Color] = Colors.reset, interval: int = 0.01, input_color: Color = Colors.white, use_icon: bool = False) -> str:
        cursor = System.cursor
        System.cursor = False

        all_colors = []
        pair = True

        if isinstance(color, Color):
            all_colors = [color] * len(prompt)

        elif isinstance(color, Fade):
            all_colors = [color.colors]
            while len(prompt) > len(all_colors):
                if pair:
                    all_colors.append(list(reversed(color.colors)))
                else:
                    all_colors.append(color.colors)
                pair = not pair

        elif color == Col.reset:
            color = ''
            all_colors = [color] * len(prompt)

        else:
            raise TypeError(color)

        if use_icon:
            icon = Logo.INPUT
            icon.icon_color = input_color
            icon.borders_color = color
            _stdout.write(icon + '')

        colors = []
        for fade_part in all_colors:
            if isinstance(color, Fade):
                colors.extend(fade_part)
            else:
                colors.append(color)

        for letter, col in zip(prompt, colors):
            _stdout.write(col + letter)
            _stdout.flush()
            _wait(interval)

        if cursor == True:
            System.cursor = True

        result = input(input_color)
        _stdout.write(Col.reset)
        return result



class Anime:

    def _anime(text: str, color: list, interval: int) -> None:
        _stdout.write(color + text)
        _stdout.flush()
        _wait(interval)


    def _makeFull(text: str) -> str:
        size = _get_terminal_size()
        lines = size.lines
        column = size.columns
        textLength = len(text)
        text += (' ' * ((lines * column) - ((textLength * 2) + 1000)))
        return text


    def Fade(text: str, fade: Fade, time: _Union[bool, int] = True, enter: bool = True, interval: int = 0.05) -> None:
        if not isinstance(fade, Fade):
            raise TypeError(fade)

        if time is int:
            time *= 15

        def _input():
            global passed
            passed = False
            input()
            passed = True

        if enter:
            _Thread(target = _input).start()

        color = fade
        text = Anime._makeFull(text)

        if time is True:
            while not passed:
                Anime._anime(text, color, interval)
                ncolor = color.colors[1:]
                ncolor.append(color.colors[0])
                color = ncolor
                color = Fade(color, fade.mode)

        else:
            for _ in range(time):
                if passed:
                    break

                Anime._anime(text, color, interval)
                ncolor = color.colors[1:]
                ncolor.append(color.colors[0])
                color = ncolor
                color = Fade(color, fade.mode)

        System.Clear()



class Logo:
    INTEROGATION: 'Logo'
    INPUT: 'Logo'
    EXCLAMATION: 'Logo'
    INFO: 'Logo'
    STAGE: 'Logo'
    ERROR: 'Logo'

    def __init__(self, icon: str, borders: list[str], borders_color: Stylizable, icon_color: Stylizable = Col.white) -> None:
        self.icon: str = icon
        self.borders: tuple[str] = tuple(borders)
        self.icon_color: Stylizable = icon_color
        self.borders_color: Stylizable = borders_color


    def __str__(self) -> str:
        return (self.borders_color + self.borders[0]) + (self.icon_color + self.icon) + (self.borders_color + self.borders[1])


    def __add__(self, other: str) -> str:
        return str(self) + ' ' + other



Logo.INTEROGATION: Logo = Logo('?', r'[]', Col.purple)
Logo.INPUT: Logo = Logo('>', r'[]', Col.green)
Logo.EXCLAMATION: Logo = Logo('!', r'[]', Col.red)
Logo.INFO: Logo = Logo('i', r'[]', Col.Scale(Col.blue, Col.white, 25))
Logo.STAGE: Logo = Logo('...', r'[]', Col.orange)
Logo.ERROR: Logo = Logo('X', r'[]', Col.red)

Stylizable: type = _Union[Color, BackColor, Fade, AnsiCode]


__all__: list[str] = [obj for obj in globals() if not obj.startswith('_')]