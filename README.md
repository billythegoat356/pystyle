<h1 align="center">PyStyle</h1>
<br>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-2.1-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/billythegoat356/pystyle/blob/main/README.md" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://github.com/billythegoat356/pystyle" target="_blank">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" />
  </a>
  <a href="https://github.com/billythegoat356/pystyle/blob/main/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/github/license/billythegoat356/pystyle" />
  </a>
</p>

> **PyStyle** is a python library to make very beautiful TUI design.


<img src="https://media.discordapp.net/attachments/888138903138213911/888139229681561681/pystylebanner.png"/> 

## Install

```sh
pip3 install pystyle
```

# FEATURES


  - Fade Effet                        D
  - Animated Fade
  - Animated Prints and Inputs
  - Color Text
  - Center Text
  - Adding banners                    D
  - Make boxes                        D
  - System Functions    

</br>

## Fade Effet
<img src="https://media.discordapp.net/attachments/888138903138213911/888143816836653116/pystleHor.png"/>

```python
from pystyle import Colors, Colorate
print(Colorate.Horizontal(Colors.yellow_to_red, "Hello, Welcome to Pystyle.", 1))
```
`Colors.yellow_to_red` Refers to the fade color, the list of colors can be found [HERE](https://pastebin.com/raw/GpN4ZD0M)<br>
`1` Refers to the intensity of the fade effect. (Default=1)<br>
`Colorate.Vertical` Refers to how the fade effet will look<br><br>
Available effetc are:
  - Vertical
  - Horizontal
  - Diagonal
  - DiagonalBackwards
 </br>
 
## Center Text
<img src="https://media.discordapp.net/attachments/888138903138213911/888174929386799104/pycenter.png"/>
<br>
This Function lets you center a banner/text in your terminal<br>
```python
from pystyle import Center
print(Center.XCenter("Hello, Welcome to Pystyle."))
```
```
Ouput:
                                Hello, Welcome to Pystyle.                                

```
Options are:
- Center: Center the banner/text on both axis
- XCenter: Center the banner/text on the X axis
- Ycenter:Center the banner/text on The Y axis
</br></br>
 

## Adding banners
<img src="https://media.discordapp.net/attachments/888138903138213911/888139239357816842/addbanner.png" width="479" height="222"/>

```python
from pystyle import Add
banner1 = '''
    .--.
  .'_\/_'.
  '. /\ .'
    "||"
     || /\
  /\ ||//\)
 (/\\||/
____\||/____'''

print(Add.Add(banner1, "This is a beautiful banner\nmade with pystyle", 4))
```
```
Output:
    .--.
  .'_\/_'.
  '. /\ .'
    "||"    This is a beautiful banner
     || /\  made with pystyle
  /\ ||//\)
 (/\||/
____\||/____
```
The first argument is the first banner and the second is the second banner.<br>
`4` Refers to the blanc lines before the smalest banner. (Default=0)
<br>
<br>

## Making Boxes
```python
from pystyle import Box
print(Box.Lines("Hello, Welcome to Pystyle."))
print(Box.SimpleCube("Hello, Welcome to Pystyle."))
```
```
Output:
─══════════════════════════☆☆══════════════════════════─
               Hello, Welcome to Pystyle.
─══════════════════════════☆☆══════════════════════════─
╔════════════════════════════╗
║ Hello, Welcome to Pystyle. ║
╚════════════════════════════╝
```
<br>
<br>

## Author

👤 GitHub: [@**loTus01**](https://github.com/loTus04)<br>
👤 GitHub: [@**billythegoat356**](https://github.com/billythegoat356)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/billythegoat356/pystyle/issues).

## Show your support

Give a ⭐️ if this project helped you!


***
