Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

======= RESTART: C:/users/sreej/OneDrive/Desktop/python/Day 2/keyword.py =======
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
35
a=10
b=20
a
10
b
20
a=b=c=10
b
10
>>> c
10
>>> a
10
>>> a,b,c,=10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> a,b=b,a
>>> a
20
>>> b
10
>>> del b
>>> b
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    b
NameError: name 'b' is not defined
