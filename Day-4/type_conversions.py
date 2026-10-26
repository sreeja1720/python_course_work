Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
b=1.0
int(b)
1
complex(b)
(1+0j)
str(b)
'1.0'
list(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
c=1+2j
int(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(1+2j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
d='codegnan'
int(d)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int(d)
ValueError: invalid literal for int() with base 10: 'codegnan'
float(d)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    float(d)
ValueError: could not convert string to float: 'codegnan'
complex(d)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    complex(d)
ValueError: complex() arg is a malformed string
list(d)
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
tuple(d)
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
set(d)
{'o', 'e', 'a', 'c', 'n', 'd', 'g'}
dict(d)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    dict(d)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(d)
True
l=[1,2,3,4,5]
int(l)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
str(l)
'[1, 2, 3, 4, 5]'
complex(l)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
list(l)
[1, 2, 3, 4, 5]
tuple(l)
(1, 2, 3, 4, 5)
set(l)
{1, 2, 3, 4, 5}
dict(l)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(l)
True
t=(1,2,3,4,5,6)
int(t)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
dtr(t)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    dtr(t)
NameError: name 'dtr' is not defined. Did you mean: 'dir'?
str(t)
'(1, 2, 3, 4, 5, 6)'
list(t)
[1, 2, 3, 4, 5, 6]
set(t)
{1, 2, 3, 4, 5, 6}
dict(t)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(t)
True
s={1,3,4,5,7,9}
int(s)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
complex(s)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'set'
str(s)
'{1, 3, 4, 5, 7, 9}'
list(s)
[1, 3, 4, 5, 7, 9]
tuple(s)
(1, 3, 4, 5, 7, 9)
bool(s)
True
dict{1:2,2:3,4:5,6:7}
SyntaxError: invalid syntax
d={1:2,2:3,4:5,6:7}
d
{1: 2, 2: 3, 4: 5, 6: 7}
int(d)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(d)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    complex(d)
TypeError: complex() first argument must be a string or a number, not 'dict'
str(d)
'{1: 2, 2: 3, 4: 5, 6: 7}'
list(d)
[1, 2, 4, 6]
tuple(d) #only keys will convert into tuple,list,set
(1, 2, 4, 6)
set(d)
{1, 2, 4, 6}
dict(d)
{1: 2, 2: 3, 4: 5, 6: 7}
bool(d)
True
#for a string ,if string has a number or numerical they can convert into integer,float
v="1234"
int(v)
1234
flaot(v)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    flaot(v)
NameError: name 'flaot' is not defined. Did you mean: 'float'?
float(v)
1234.0
complex(v)
(1234+0j)
str(v)
'1234'
list(v)
['1', '2', '3', '4']
tuple(v)
('1', '2', '3', '4')
set(v)
{'2', '3', '1', '4'}
>>> dict(v)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    dict(v)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> bool(v)
True
>>> b=True
>>> int(b)
1
>>> flaot(b)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    flaot(b)
NameError: name 'flaot' is not defined. Did you mean: 'float'?
>>> float(b)
1.0
>>> complex(b)
(1+0j)
>>> str(b)
'True'
