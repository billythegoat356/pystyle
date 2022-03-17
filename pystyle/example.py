from __init__ import *

color1 = Colors.StaticRGB(0, 0, 255)
color2 = Colors.StaticRGB(255, 0, 0)
color3 = Colors.StaticRGB(255, 255, 0)
color4 = Colors.StaticRGB(0, 255, 255)

fade1 = Colors.MakeFade([color1, color2])
fade2 = Colors.MakeFade([color3, color4])
fade3 = Colors.DynamixMIX([fade1, fade2])

print(Colorate.FadeByColors('Salut cv bien ? tranquille ? Moi oui je vais bien merci !!!', [color1, color2, color3, color4]))

input()