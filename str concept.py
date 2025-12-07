Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> str1 = "Atharva"
>>> str1[2] =
SyntaxError: invalid syntax
>>> 
>>> str1[3]
'a'
>>> str1[2]="Rahul"
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    str1[2]="Rahul"
TypeError: 'str' object does not support item assignment
>>> str = "This is 'Python' Language"
>>> str[9:14]
'Pytho'
>>> str[9:15]
'Python'
>>> str = "Python is my first programming Language"
>>> str = "'Python is my first programming Language'str[1:39]
SyntaxError: unterminated string literal (detected at line 1)
>>> 
>>> str = "'Python is my first programming Language'str[1:39]
SyntaxError: unterminated string literal (detected at line 1)
>>> 
>>> 
>>> 
>>> s ="Me Atharva hooooo"
>>> s[-14:-6]
'Atharva '
