Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s='python java flask mysql fastapi'
>>> s
'python java flask mysql fastapi'
>>> len(s)
31
>>> ord('s')
115
>>> ord('A')
65
>>> ord('u')
117
>>> chr(67)
'C'
>>> chr(100)
'd'
>>> chr(4)
'\x04'
>>> chr(1)
'\x01'
>>> sorted(s)
[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'f', 'f', 'h', 'i', 'j', 'k', 'l', 'l', 'm', 'n', 'o', 'p', 'p', 'q', 's', 's', 's', 't', 't', 'v', 'y', 'y']
max(s)
'y'
min(s)
' '
s
'python java flask mysql fastapi'
s.upper()
'PYTHON JAVA FLASK MYSQL FASTAPI'
s.lower()
'python java flask mysql fastapi'
s.swapcase()]
SyntaxError: unmatched ']'
s.swapcase()
'PYTHON JAVA FLASK MYSQL FASTAPI'
s.title()
'Python Java Flask Mysql Fastapi'
s.capitaze()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s.capitaze()
AttributeError: 'str' object has no attribute 'capitaze'. Did you mean: 'capitalize'?
s.capitalize()
'Python java flask mysql fastapi'
""""FORMATING METHODS"""
'"FORMATING METHODS'
s.center(40,'-')
'----python java flask mysql fastapi-----'
s='python'
s.center(40,' ')
'                 python                 '
s.center(40,'*')
'*****************python*****************'
s.ljust(40,'*')
'python**********************************'
s.rjust(40,'*')
'**********************************python'
'1'.zfill(5)
'00001'
'123'.zfill(9)
'000000123'
'123456789'.zfill(5)
'123456789'
s.find('a')
-1
s
'python'
s='python java flask mysql fastapi'
s.find('a')
8
s.find('f')
12
s.find('y')
1
s.rfind('a')
28
s.index('a')
8
s.rindex('f')
24
s.count('a')
5
s.count('f')
2
s.count('o')
1
s.count('z')
0
s.strip()
'python java flask mysql fastapi'
s='          code    gnan        '
s.strip()
'code    gnan'
s.rstrip()
'          code    gnan'
s.lstrip()
'code    gnan        '
s.replace('a','*')
'          code    gn*n        '
s='python java flask mysql fastapi'
s.replace('a','*')

'python j*v* fl*sk mysql f*st*pi'
s.maketrans('apqks','12345')
{97: 49, 112: 50, 113: 51, 107: 52, 115: 53}
s.translate(s.maketrans('apqks','12345'))
'2ython j1v1 fl154 my53l f15t12i'
s.translate(s.maketrans('aeiou','*****'))
'pyth*n j*v* fl*sk mysql f*st*p*'
