Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
type(a)
<class 'int'>
b=10.3
type(b)
<class 'float'>
c=3+4j
type(c)
<class 'complex'>
s="codegnan"
type(s)
<class 'str'>
l=[1,2,3,4]
type(l)
<class 'list'>
r=[1,2.3,'sri']
type(r)
<class 'list'>
k=[1,1,1,1]
type(k)
<class 'list'>
s="code"
id(s)
2593148780912
>>> s+='gnan'
>>> s
'codegnan'
>>> id(s)
2593189938416
>>> l
[1, 2, 3, 4]
>>> r
[1, 2.3, 'sri']
>>> r.append(5)
>>> r
[1, 2.3, 'sri', 5]
>>> id(r)
2593148967808
>>> r.pop()
5
>>> id(r)
2593148967808
>>> t=(1,2,3)
>>> type(t)
<class 'tuple'>
>>> s={34,12345,54678,1354,34,34,34}
>>> s
{12345, 34, 1354, 54678}
type(s)
<class 'set'>
pro={"product" :"laptop",  "price" : 350000}
type(pro)
<class 'dict'>
pro
{'product': 'laptop', 'price': 350000}
status=True
type(status)
<class 'bool'>
s=None
type(s)
<class 'NoneType'>
