Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='python'
s
'python'
s=''

s
''
"""STRING OPERATIONS"""
'STRING OPERATIONS'
s='python'
t='programming'
s
'python'
t
'programming'
#concatination
s+t
'pythonprogramming'
#Repeatition
s*4
'pythonpythonpythonpython'
s*@
SyntaxError: incomplete input
t*4
'programmingprogrammingprogrammingprogramming'
'*'*7
'*******'
'0'*20
'00000000000000000000'
#Indexing
s='python java flask mysql fastapi'
s[1]
'y'
s[5]
'n'
s[-1]
'i'
s[-7]
'f'
s[9]
'v'
s[-10]
'q'
s[12]
'f'
#Slicing
s='python java flask mysql fastapi'
s[0:6:1]
'python'
KeyboardInterrupt
s[7:11:1]
'java'
s[:6]
'python'
s[7:11]
'java'
s[12:17]
'flask'
s[18:23]
'mysql'
s[24:]
'fastapi'
s[::-1]
'ipatsaf lqsym ksalf avaj nohtyp'
s[-5:-1]
'stap'
s[::2]
'pto aafakmslfsai'
s[-15:-20:-1]
'ksalf'
>>> s[-5]
's'
>>> s[-5:1]
''
>>> s[::2]
'pto aafakmslfsai'
>>> s
'python java flask mysql fastapi'
>>> java in s
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    java in s
NameError: name 'java' is not defined
>>> 'java'in s
True
>>> 'python' in s
True
>>> 'c++' not in s
True
>>> 'flask' not in s
False
