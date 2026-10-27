Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=input()
srii
a
'srii'
a=input("enter a string: ")
enter a string: ssriii
a
'ssriii'
type(a)
<class 'str'>
a=int(input())
5
a
5
type(a)
<class 'int'>
a=int(input("enter a integer: "))
enter a integer: 2
a
2
a=float(input("enter a float: "))
enter a float: 50.1
a
50.1
a=float(input("enter a float: "))
enter a float: 12
a
12.0
a=input().split()
2 3r 1 5 
a
['2', '3r', '1', '5']
a=list(map(int,input().split()))
2 5 94 0 23 45
a
[2, 5, 94, 0, 23, 45]
a=list(map(float,input().split()))

a=list(map(float,input().split()))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a=list(map(float,input().split()))
ValueError: could not convert string to float: 'a=list(map(float,input().split()))'
a=list(map(float,input().split()))
12.4 482 843 98
a
[12.4, 482.0, 843.0, 98.0]
a=input().split()
32 54 6
a
['32', '54', '6']
a=tuple(map(int,input().split()))
21 46 829
a
(21, 46, 829)
a=tuple(input().split())
12 4 86 2
a
('12', '4', '86', '2')
a=tuple(map(float,input().split()))
2 664 98 2 
a
(2.0, 664.0, 98.0, 2.0)
a=set(input().split())
3 45 2 6
a
{'3', '2', '45', '6'}
a=set(map(int,input().split()))
37 87 239 
a
{239, 37, 87}
a=set(map(float,input().split()))
2736 98.4 9832.4
a
{2736.0, 98.4, 9832.4}
# totake multiple variables at atime
a,b,c=list(map(int,input().split()))
1 2 4
a
1
b
2
c
4
email,password=input().split()
sri@gmail.com 1234
email
'sri@gmail.com'
password
'1234'
a,b,c=list(map(float,input().split()))
12l.4 23.4  23
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a,b,c=list(map(float,input().split()))
ValueError: could not convert string to float: '12l.4'
a,b,c=list(map(float,input().split()))
12
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a,b,c=list(map(float,input().split()))
ValueError: not enough values to unpack (expected 3, got 1)
>>> a,b,c=list(map(float,input().split()))
12 34 12
>>> a
12.0
>>> b
34.0
>>> c
12.0
>>> a,b,c=list(map(float,input().split()))
12.2 32.2 4.4
>>> a
12.2
>>> b
32.2
>>> c
4.4
>>> a=eval(input())
"sri"
>>> a
'sri'
a=eval(input())
23
a
23
a=eval(input())
[1,23,4]
a
[1, 23, 4]
a=eval(input())
(23,45)
a
(23, 45)
a=eval(input())
True
a
True
a=eval(input())
45.4
a
45.4
a=eval(input())
{12,4456,34}
a
{4456, 34, 12}
a=eval(input())
{1:4,2:5,3:5}
a
{1: 4, 2: 5, 3: 5}
a=eval(input())
2+5j
a
(2+5j)
'''output format'''
'output format'
c="codegana'
SyntaxError: incomplete input
a="codegana"
a
'codegana'
a=10
b=10.2
c='codegnan'
a
10
b
10.2
c
'codegnan'
print(a,b,c)
10 10.2 codegnan
print("a=",a,"b=",b,"c=",c)
a= 10 b= 10.2 c= codegnan
print("a=",a,"b=",b,"c=",c,sep=' ')
a= 10 b= 10.2 c= codegnan
print("a=",a,"b=",b,"c=",c,sep='')
a=10b=10.2c=codegnan
print("a=",a,"b=",b,"c=",c,sep='-')
a=-10-b=-10.2-c=-codegnan
print("a=",a,"b=",b,"c=",c,end="\n\n")
a= 10 b= 10.2 c= codegnan

print("a=",a,"b=",b,"c=",c,end="@")

a= 10 b= 10.2 c= codegnan@
print(f'a={a} b={b} c={c}' )
a=10 b=10.2 c=codegnan
print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=10.200000 c=codegnan
print('a=%d b=%.2f c=%s'%(a,b,c))
a=10 b=10.20 c=codegnan
print('a={} b={} c={}'.format(a,b,c))
a=10 b=10.2 c=codegnan
print('a={} b={} c={}'.format(b,c,a))
a=10.2 b=codegnan c=10
