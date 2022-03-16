# Pystyle remake (greatColors)
greatColors is a remake of [pystyle by Billythegoat and LoTus01](https://github.com/billythegoat356/pystyle).
It's more easy to understand but not more good 😅

## SCREENS AND UTILISATION

IMPORTATION

````python
from greatColors import *
```

ADD COLOR TO A TEXT
```python
print(Text.colorize('Hey, welcome to gcolors !', Color.red))
```
![](https://cdn.discordapp.com/attachments/953677434245484545/953709736216371250/unknown.png)

ADD FADE COLOR TO A TEXT
```python
print(Text.fade([Color.red, Color.purple], 'Hey, welcome to gcolors !'))
```
![](https://cdn.discordapp.com/attachments/953677434245484545/953710144120827954/unknown.png)

MAKE A RELATIVE COLOR WITH 2 COLORS
```python
color1 = Color.cyan
color2 = Color.green
relative = Color.middleColor([color1, color2])

print(Text.colorize('This is a color between green & cyan.', relative))
```
![](https://cdn.discordapp.com/attachments/953677434245484545/953711786471858286/unknown.png)

MAKE CENTERED TEXT
```python
print(Text.center('---- This is a centered text ----'))
```
![](https://cdn.discordapp.com/attachments/953677434245484545/953712826814459934/unknown.png)

for more install it ;)
Remake of https://github.com/billythegoat356/pystyle
