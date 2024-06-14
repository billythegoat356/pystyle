<h1 align="center">PyStyle</h1>
<br>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-2.9-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/billythegoat356/pystyle/blob/main/README.md" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://github.com/billythegoat356/pystyle" target="_blank">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" />
  </a>
  <a href="https://github.com/billythegoat356/pystyle/blob/main/LICENSE" target="_blank">
    <img alt="License: EPL-2.0" src="https://img.shields.io/github/license/billythegoat356/pystyle" />
  </a>
  <a href="https://pepy.tech/project/pystyle" target="_blank">
    <img alt="Downloads" src="https://static.pepy.tech/personalized-badge/pystyle?period=total&units=international_system&left_color=grey&right_color=orange&left_text=Downloads" />
  </a>
</p>

> **PyStyle** یک کتابخانه پایتون برای ساخت زیباترین ظاهر TUI.
> <br>
> با الهام از **pyfade** و **pycenter**.
> <br>
> ساخته شده توسط [Billy](https://github.com/billythegoat356), [loTus01](https://github.com/loTus04), و [BlueRed](https://github.com/CSM-BlueRed) و [Thecode764](https://github.com/Thecode764)


<img src="https://media.discordapp.net/attachments/888138903138213911/888139229681561681/pystylebanner.png"/> 

## نصب کنید

```sh
pip3 install pystyle
```
Stats: https://pepy.tech/project/pystyle

# بخش هایی که در این مستند گفته شده.

  - رنگی کردن متن ها ✔️
  - رنگی کردن متن ها با افکت ✔️
  - انیمیشن ها ❌
  - افکت های متنی ✔️
  - متن در مرکز ✔️
  - ساخت بنر ✔️
  - ساخت باکس ✔️
  - نشان دادن و پنهان کردن نشان گر ماوس ✔️
  - فانکشن ها سیستمی ✔️

<br>

## رنگی کردن متن ها
<img src="https://cdn.discordapp.com/attachments/882652381731504182/890179524451512330/unknown.png">
<p><i><strong>متن ها را به سادگی رنگی کنید.</strong></i></p>
<br>

```python
from pystyle import Colors, Colorate
text = "Hello world!"
print(Colors.blue + text)
# یا از مثال زیر استفاده کنید
print(Colorate.Color(Colors.blue, text, True))
```

<br>

`Colors.blue` = رنگ<br>
`text` = متنی که باید رنگی شود<br>
`True` = رنگ آمیزی را پس از پایان پایان دهید (در غیر این صورت چاپ کاراکترها در رنگ مشخص شده ادامه می یابد)

<br>

در حال حاضر فانکشن های زیر وجود دارد:
  - Color (رنگی کردن یک متن رنگی)
  - Error (ساخت افکت خطا)


<br>

## یک متن رنگی با افکت بسازید!
<img src="https://media.discordapp.net/attachments/888138903138213911/888143816836653116/pystleHor.png">
<p><i><strong>یک متن رنی با افکت بسازید</strong></i></p>
<br>

```python
from pystyle import Colors, Colorate
print(Colorate.Horizontal(Colors.yellow_to_red, "Hello, Welcome to Pystyle.", 1))
```

<br>

`Colors.yellow_to_red` = رنگ<br>
`Colorate.Vertical` = نوع<br>
`1` = شدت (پیش‌فرض=1)

<br>

در حال حاضر افکت های زیر وجود دارد:
  - Vertical
  - Horizontal
  - Diagonal
  - DiagonalBackwards

<br>

## ساخت یک متن با افکت های تایپی

<br>

برای نوشتن یک متن با افکت های تایپی از `pystyle.Write` استفاده کنید.

```python
from pystyle import Write, Colors

name = Write.Input("Enter your name -> ", Colors.red_to_purple, interval=0.0025)
Write.Print(f"Nice to meet you, {name}!", Colors.blue_to_green, interval=0.05)
```
<br>


۲ فانکشن وجود دارد:<br>


`Write.Print`: نمایش یک متن با افکت<br>
`Write.Input`: مثل همان `Write.Input` فقط به جای نوشتن ورودی میگیرد<br>


<br>


۶ آرگومان وجود دارد:<br>


`text`: متنی که باید نوشته شود<br>
`color`: رنگی که برای متن میخواهید<br>
`interval`: فاصله نوشتن هر کلمه<br>
`hide_cursor`: پنهان کردن نشان گر ماوس<br>
`end`: رنگ انتهایی، پیش فرض سفید است<br>
`input_color` (فقط برای `Write.Input`): برای رنگ ورودی استفاده میشود<br>


<br>
<br>


## قرار دادن متن در وسط صفحه
<img src="https://media.discordapp.net/attachments/888138903138213911/888174929386799104/pycenter.png">
<br>
<p><i><strong>یک متن را در مرکز صفحه قرار دهید!</strong></i></p>

```python
from pystyle import Center
print(Center.XCenter("Hello, Welcome to Pystyle."))
```
<br>
<p>خروجی</p>
<br>

```
                                            Hello, Welcome to Pystyle.                                
```


<br>

در حال حاضر حالت های زیر وجود دارد:
  - Center (بنر/متن را در هر دو محور وسط قرار دهید)
  - XCenter (بنر/متن را روی محور X وسط قرار دهید)
  - YCenter (بنر/متن را روی محور Y وسط قرار دهید)

<br><br>

## بنر اضافه کنید.
<p><i><strong>به هر چیزی یک بنر اضافه کنید.</strong></i></p>
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

text = "This is a beautiful banner\nmade with pystyle"

print(Add.Add(banner1, text, 4))
```

خروجی:

```
    .--.
  .'_\/_'.
  '. /\ .'
    "||"    This is a beautiful banner
     || /\  made with pystyle
  /\ ||//\)
 (/\||/
____\||/____
```
<br>

`banner1` = بنر اول<br>
`text` = بنر دوم<br>
`4` = خطوط خالی قبل از افزودن کوچکترین بنر به بزرگترین بنر (پیش فرض = 0). برای وسط روی `True` تنظیم کنید<br>

## ساختن باکس!
<p><i><strong>یک باکس زیبا بسازید!</strong></i></p>
<br>

```python
from pystyle import Box
print(Box.Lines("Hello, Welcome to Pystyle."))
print(Box.DoubleCube("Hello, Welcome to Pystyle."))
```

خروجی:

```
─══════════════════════════☆☆══════════════════════════─
               Hello, Welcome to Pystyle.
─══════════════════════════☆☆══════════════════════════─
╔════════════════════════════╗
║ Hello, Welcome to Pystyle. ║
╚════════════════════════════╝
```

در حال حاضر این چند نوع وجود دارد:
  - Lines
  - SimpleCube
  - DoubleCube

## ماوس
ماوس را نشان دهید!

```python
from pystyle import Cursor

Cursor.ShowCursor()
```

ماوس را پنهان کنید!

```python
from pystyle import Cursor

Cursor.HideCursor()
```

## فانکشن های سیستمی
### با یک کد بررسی کنید ترمینال شما از رنگ پشتیبانی میکند؟
```python
from pystyle import System

System.Init()
```
### صفحه ترمینال خود را تمیز کنید
```python
from pystyle import System

System.Clear()
```
### عنوان ترمینال خود را عوض کنید
```python
from pystyle import System

System.Title("The title")
```
**نکته: این قابلیت فقط در سیستم عامل ویندوز کار میکند**
### اندازه ترمینال خود را تغییر دهید

**نکته** این قابلیت فقط در سیستم عامل ویندوز کار میکند

```python
from pystyle import System

System.Size(12,12)
```
### یک کامند ترمینال را اجرا کنید
```python
from pystyle import System

System.Command("echo hello")
```

<br>
<br>

## 👤 نویسندگان

👤 گیت هاب: [@**billythegoat356**](https://github.com/billythegoat356)<br>
👤 گیت هاب: [@**loTus01**](https://github.com/loTus04)<br>
👤 گیت هاب: [@**BlueRed**](https://github.com/CSM-BlueRed)<br>
👤 گیت هاب (ترجمه کننده): [@**Thecode764**](https://github.com/Thecode764)<br>


## 🤝 به توسعه کمک کنید

توسعه دهنده های عزیز, اگر باگی دیدید گزارش دهید اگر میخواهید قابلیتی اضافه شود گزارش دهید!<br />این صفحه را برای اطلاعات بیشتر چک کنید 

[صفحه نظر ها و انتقادات](https://github.com/billythegoat356/pystyle/issues).

## ❤ پروژه خود را نشان دهید

به این پروژه یک ستاره بدهید اگر این پروژه به شما کمک کرده است.


***