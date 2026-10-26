Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
"ARITHMETICAL OPERATORS"
'ARITHMETICAL OPERATORS'
A=20
a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
a//b
2
a%b
0
a**b
10240000000000
a**b #it is exponent or power value
10240000000000
# + - * / // % **
''' COMPARISION OPERATOR'''
' COMPARISION OPERATOR'
a=20
b=10
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True
# <,>,<=,>=,==,!=
''' ASSIGNMENT OPERATOR'''
' ASSIGNMENT OPERATOR'
c=20
c+=10
c
30
c-=20
c
10
c*=10
c
100
c//=10
c
10
''' LOGICAL OPERATOR'''
' LOGICAL OPERATOR'
# and,or,not
a
20
b
10
a%2==0 and a>10 # and means all statements should be true or statisfied
True
b%2==0 and b>10
False
b%2==0 or b>10 # or means any of the stmt is true the output will be true
True
b%2==0
True
not b%2==0 # not means it  convert true to false and vise versa
False
''' MEMBERSHIP OPERATOR'''
' MEMBERSHIP OPERATOR'
# used for string,list,tuple,set,dict operations
s='python'
'p' in s
True
'y' in s
True
's' in s
False
'p' not in s
False
's' not in s
True
l=[1,2,3,4]
2 in l
True
5 in l
False
5 not in l
True
t=(12,3,5,8)
1 in t
False
12 in t
True
1 not in t
True
s={3,7,9,2}
5 in s
False
7 in s
True
12 not in s
True
7 not in s
False
d={1:2,2:5,4:8,5:0}
2 in s
True
5 is in s
SyntaxError: invalid syntax
5 in s
False
5 not in s
True
''' IDENTITY OPERATOR'''
' IDENTITY OPERATOR'
#  is,is not
l=[1,2,3,4,5]
m=[1,2,3,4,,5]
SyntaxError: invalid syntax
l=[1,2,3,4,5]
m=[1,2,3,4,5]
SyntaxError: multiple statements found while compiling a single statement
l=[1,2,3,4,5]
m=[1,2,3,4,5]
>>> id(l)
2370315539840
>>> id(m)
2370315541376
>>> l==m #it checks assigned   values
True
>>> l  is m #it check the memory references
False
>>> n==m
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    n==m
NameError: name 'n' is not defined
>>> n=m
>>> id(n)
2370315541376
>>> n
[1, 2, 3, 4, 5]
>>> n is not m
False
>>> n is not l
True
