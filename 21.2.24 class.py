Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a = [1, 3, 5, 7, 9]
>>> a
[1, 3, 5, 7, 9]
>>> a[0]
1
>>> a[1]
3
>>> a[4]
9
>>> a[5]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a[5]
IndexError: list index out of range
>>> sum(a)
25
>>> min(a)
1
>>> max(a)
9
>>> len(a)
5
>>> type(a)
<class 'list'>
>>> a[2] = 50
>>> a
[1, 3, 50, 7, 9]
>>> a[1] = 50
>>> a
[1, 50, 50, 7, 9]
>>> a[2] = 66
>>> a
[1, 50, 66, 7, 9]
>>> a[-1]
9
>>> a[-2]
7
>>> a[-5]
1
>>> a[-100]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a[-100]
IndexError: list index out of range
>>> a[-;3]
SyntaxError: invalid syntax
>>> a[-:3]
SyntaxError: invalid syntax
>>> a[:3]
[1, 50, 66]
>>> a[2:5]
[66, 7, 9]
>>> a[3:]
[7, 9]
>>> a
[1, 50, 66, 7, 9]
>>> len(a)
5
>>> a[0]
1
>>> a[0] = 5.678
>>> a
[5.678, 50, 66, 7, 9]
>>> a[1] = 'korea'
>>> a
[5.678, 'korea', 66, 7, 9]
>>> a[5] = 70
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a[5] = 70
IndexError: list assignment index out of range
>>> a.append(70)
>>> a.append(80)
>>> a
[5.678, 'korea', 66, 7, 9, 70, 80]
>>> a.append('서울')
>>> ㅁ
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    ㅁ
NameError: name 'ᄆ' is not defined
>>> a.append('america')
>>> a
[5.678, 'korea', 66, 7, 9, 70, 80, '서울', 'america']
>>> len(a)
9
>>> a.reverse()
>>> a
['america', '서울', 80, 70, 9, 7, 66, 'korea', 5.678]
>>> a.reverse()
>>> a
[5.678, 'korea', 66, 7, 9, 70, 80, '서울', 'america']
>>> a.append('부산', '목포', '대구')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a.append('부산', '목포', '대구')
TypeError: list.append() takes exactly one argument (3 given)
>>> ㅁ
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    ㅁ
NameError: name 'ᄆ' is not defined
>>> a
[5.678, 'korea', 66, 7, 9, 70, 80, '서울', 'america']
>>> id(a)
2795248231680
>>> id(a[0])
2795249831536
>>> a == b
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a == b
NameError: name 'b' is not defined
>>> b
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> a
[5.678, 'korea', 66, 7, 9, 70, 80, '서울', 'america']
>>> a - 0
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a - 0
TypeError: unsupported operand type(s) for -: 'list' and 'int'
>>> a == 0
False
>>> a == a
True
>>> a == (a+a) - a
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a == (a+a) - a
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> a == {(a+a) - a}
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a == {(a+a) - a}
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> a == ((a+a) - a)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a == ((a+a) - a)
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> a == a+a
False
>>> a == a+0
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a == a+0
TypeError: can only concatenate list (not "int") to list
>>> a2 = [5, 7, 9, 3]
>>> a2
[5, 7, 9, 3]
>>> a2.sort()
>>> a2
[3, 5, 7, 9]
>>> a2.reverse()
>>> a
[5.678, 'korea', 66, 7, 9, 70, 80, '서울', 'america']
>>> a2
[9, 7, 5, 3]
>>> a
[5.678, 'korea', 66, 7, 9, 70, 80, '서울', 'america']
>>> a.reverse()
>>> a
['america', '서울', 80, 70, 9, 7, 66, 'korea', 5.678]
>>> del(a[3])
>>> a
['america', '서울', 80, 9, 7, 66, 'korea', 5.678]
>>> aa = a.copy()
>>> aa
['america', '서울', 80, 9, 7, 66, 'korea', 5.678]
>>> a
['america', '서울', 80, 9, 7, 66, 'korea', 5.678]
>>> a.append(200)
>>> a
['america', '서울', 80, 9, 7, 66, 'korea', 5.678, 200]
>>> a.append(200)
>>> a
['america', '서울', 80, 9, 7, 66, 'korea', 5.678, 200, 200]
>>> aa
['america', '서울', 80, 9, 7, 66, 'korea', 5.678]
>>> a.count(10)
0
>>> a.count(100)
0
>>> a.count(200)
2
>>> a.index(200)
8
>>> a.index(100)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a.index(100)
ValueError: 100 is not in list
>>> a.index('서울')
1
>>> aa
['america', '서울', 80, 9, 7, 66, 'korea', 5.678]
>>> a.extend(aa)
>>> a
['america', '서울', 80, 9, 7, 66, 'korea', 5.678, 200, 200, 'america', '서울', 80, 9, 7, 66, 'korea', 5.678]
>>> a.remove(200)
>>> a
['america', '서울', 80, 9, 7, 66, 'korea', 5.678, 200, 'america', '서울', 80, 9, 7, 66, 'korea', 5.678]
>>> a.remove(100)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    a.remove(100)
ValueError: list.remove(x): x not in list
>>> a.remove(8)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    a.remove(8)
ValueError: list.remove(x): x not in list
>>> a.remove(80)
>>> a
['america', '서울', 9, 7, 66, 'korea', 5.678, 200, 'america', '서울', 80, 9, 7, 66, 'korea', 5.678]
>>> len(a)
16
>>> a.insert(500)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    a.insert(500)
TypeError: insert expected 2 arguments, got 1
>>> a.insert(0,500)
>>> a
[500, 'america', '서울', 9, 7, 66, 'korea', 5.678, 200, 'america', '서울', 80, 9, 7, 66, 'korea', 5.678]
>>> len(a)
17
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a = efe
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    a = efe
NameError: name 'efe' is not defined
>>> a = ''efe''
SyntaxError: invalid syntax
>>> a = ('e')
>>> a
'e'
>>> a.clear()
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    a.clear()
AttributeError: 'str' object has no attribute 'clear'
>>> a.clear(a)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    a.clear(a)
AttributeError: 'str' object has no attribute 'clear'
>>> a
'e'
>>> a = e
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    a = e
NameError: name 'e' is not defined
>>> a == e
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    a == e
NameError: name 'e' is not defined
>>> a
'e'
>>> a == 'e'
True
>>> a
'e'
>>> del(a)
>>> a
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> aa
['america', '서울', 80, 9, 7, 66, 'korea', 5.678]
>>> aa == ['america', '서울', 80, 9, 7, 66, 'korea', 5.678]
True
>>> aa
['america', '서울', 80, 9, 7, 66, 'korea', 5.678]
>>> aw
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    aw
NameError: name 'aw' is not defined
>>> a2
[9, 7, 5, 3]
>>> a2.index()
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    a2.index()
TypeError: index expected at least 1 argument, got 0
>>> a2.reverse()
>>> a2
[3, 5, 7, 9]
>>> bb = (1, 4, 5)
>>> bb
(1, 4, 5)
>>> type(bb)
<class 'tuple'>
>>> bb[0]
1
>>> bb[4]
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    bb[4]
IndexError: tuple index out of range
>>> bb.append(30)
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    bb.append(30)
AttributeError: 'tuple' object has no attribute 'append'
>>> bb[2] = 7
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    bb[2] = 7
TypeError: 'tuple' object does not support item assignment
>>> bb.count(1)
1
>>> bb
(1, 4, 5)
>>> bb.count(5)
1
>>> bb.index5)
SyntaxError: unmatched ')'
>>> bb.index(5)
2
>>> b2 = (2, 4, 4, 6, 2, 2)
>>> b2
(2, 4, 4, 6, 2, 2)
>>> b2.index(2)
0
>>> b2.count(2)
3
>>> b3 = ('aaa', 4, 5, 6.7)
>>> b3
('aaa', 4, 5, 6.7)
>>> type(b3)
<class 'tuple'>
>>> type(aa)
<class 'list'>
>>> aa
['america', '서울', 80, 9, 7, 66, 'korea', 5.678]
>>> b3
('aaa', 4, 5, 6.7)
>>> type(bb)
<class 'tuple'>
>>> b3
('aaa', 4, 5, 6.7)
>>> b5 = {1, 'a', 2, 3}
>>> type(b5)
<class 'set'>
>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(tuple)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> a.append
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    a.append
NameError: name 'a' is not defined
>>> s1 - {1, 2, 3, 4, 5}
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    s1 - {1, 2, 3, 4, 5}
NameError: name 's1' is not defined
>>> s1 = {1, 2, 3, 4, 5}
>>> s2 = {2, 4, 6, 3, 3, 3}
>>> s1
{1, 2, 3, 4, 5}
>>> s2
{2, 3, 4, 6}
>>> type(s1), type(s2)
(<class 'set'>, <class 'set'>)
>>> s1 : s2
>>> s1 & s2
{2, 3, 4}
>>> s1 - s2
{1, 5}
>>> s1 ^ s2
{1, 5, 6}
>>> s2 - s1
{6}
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6}
>>> s1.intersection(s2)
{2, 3, 4}
>>> s1.difference(s2)
{1, 5}
>>> dir(s1)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> s1 | s2
{1, 2, 3, 4, 5, 6}
>>> s2
{2, 3, 4, 6}
>>> s2.pop()
2
>>> s2
{3, 4, 6}
>>> s2.remove(4)
>>> s2
{3, 6}
>>> d = {'1' : 'one', '2' : 'two', '3' : 'four'}
>>> d
{'1': 'one', '2': 'two', '3': 'four'}
>>> type(d)
<class 'dict'>
>>> d.key()
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    d.key()
AttributeError: 'dict' object has no attribute 'key'
>>> d.keys()
dict_keys(['1', '2', '3'])
>>> d.values()
dict_values(['one', 'two', 'four'])
>>> d.items()
dict_items([('1', 'one'), ('2', 'two'), ('3', 'four')])
>>> d
{'1': 'one', '2': 'two', '3': 'four'}
>>> len(d)
3
>>> d['1']
'one'
>>> d['2']
'two'
>>> dd = {'이름' : '추신수', '직업' : '야구선수', '나이' : 39}
>>> dd
{'이름': '추신수', '직업': '야구선수', '나이': 39}
>>> d.pop(1)
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    d.pop(1)
KeyError: 1
>>> dd('이름']
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> dd('이름')
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    dd('이름')
TypeError: 'dict' object is not callable
>>> dd['이름']
'추신수'
>>> dd['직업']
'야구선수'
>>> dd[0]
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    dd[0]
KeyError: 0
>>> for i, j in d.items():
	print(i, '==>', j)

	
1 ==> one
2 ==> two
3 ==> four
>>> for f, r in d.items():
	print(f, '==>', r)

	
1 ==> one
2 ==> two
3 ==> four
>>> for keys, values in dd.items():
	print(keys, '==>', values)

	
이름 ==> 추신수
직업 ==> 야구선수
나이 ==> 39
>>> dd
{'이름': '추신수', '직업': '야구선수', '나이': 39}
>>> dd.update({'지역' : '대구'})
>>> dd
{'이름': '추신수', '직업': '야구선수', '나이': 39, '지역': '대구'}
>>> d.update({'4' : 'four'})
>>> d
{'1': 'one', '2': 'two', '3': 'four', '4': 'four'}
>>> d.get('1')
'one'
>>> d.get('3')
'four'
>>> d.get('2')
'two'
>>> d.get('4')
'four'
>>> d.pop('2')
'two'
>>> d
{'1': 'one', '3': 'four', '4': 'four'}
>>> d.popitems('4')
Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    d.popitems('4')
AttributeError: 'dict' object has no attribute 'popitems'
>>> d.popitems()
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    d.popitems()
AttributeError: 'dict' object has no attribute 'popitems'
>>> d
{'1': 'one', '3': 'four', '4': 'four'}
>>> d.popitem()
('4', 'four')
>>> d
{'1': 'one', '3': 'four'}
>>> d.clear()
>>> d
{}
>>> dir(d)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> d
{}
>>> a
Traceback (most recent call last):
  File "<pyshell#224>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a = [2, 3]
>>> a
[2, 3]
>>> dd.copy(ff)
Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    dd.copy(ff)
NameError: name 'ff' is not defined
>>> dd.copy()
{'이름': '추신수', '직업': '야구선수', '나이': 39, '지역': '대구'}
>>> dd
{'이름': '추신수', '직업': '야구선수', '나이': 39, '지역': '대구'}
>>> a = [1, 2, 3, 4, 5]
>>> b = [1, 2, 3, 4, 5]
>>> a
[1, 2, 3, 4, 5]
>>> b
[1, 2, 3, 4, 5]
>>> 4 in a
True
>>> 9 in a
False
>>> 0 in a
False
>>> a
[1, 2, 3, 4, 5]
>>> b
[1, 2, 3, 4, 5]
>>> a  == b
True
>>> a is a
True
>>> a is b
False
>>> id(a)
2795251265216
>>> id(b)
2795251548032
>>> la = a
>>> la  = a
>>> la == a
True
>>> a[0]
1
>>> b[0]
1
>>> b is a
False
>>> a[0] is b[0]
True
>>> 
>>> id(a[0])
2795214891312
>>> id(b[0])
2795214891312
>>> a
[1, 2, 3, 4, 5]
>>> b
[1, 2, 3, 4, 5]
>>> id(a), id(b)
(2795251265216, 2795251548032)
>>> a2 = a
>>> id(a), id(a2)
(2795251265216, 2795251265216)
>>> a[2] = 333
>>> a
[1, 2, 333, 4, 5]
>>> a2
[1, 2, 333, 4, 5]
>>> a5
Traceback (most recent call last):
  File "<pyshell#262>", line 1, in <module>
    a5
NameError: name 'a5' is not defined
>>> a5 = a.copy()
>>> a
[1, 2, 333, 4, 5]
>>> a2
[1, 2, 333, 4, 5]
>>> a5
[1, 2, 333, 4, 5]
>>> id(a), id(a2), id(a5)
(2795251265216, 2795251265216, 2795249729408)
>>> a5
[1, 2, 333, 4, 5]
>>> a
[1, 2, 333, 4, 5]
>>> a2
[1, 2, 333, 4, 5]
>>> id(a), id(a2), id(a5)
(2795251265216, 2795251265216, 2795249729408)
>>> 
================== RESTART: C:/Users/BSH/Desktop/코딩 실습/3day.py =================
1  ==> 1
2  ==> 3
3  ==> 6
4  ==> 10
5  ==> 15
6  ==> 21
7  ==> 28
8  ==> 36
9  ==> 45
10  ==> 55
 1 ~ 10까지의 합 :  55
>>> 
================== RESTART: C:/Users/BSH/Desktop/코딩 실습/3day.py =================
1  ==> 1
2  ==> 3
3  ==> 6
4  ==> 10
5  ==> 15
6  ==> 21
7  ==> 28
8  ==> 36
9  ==> 45
10  ==> 55
11  ==> 66
12  ==> 78
13  ==> 91
14  ==> 105
15  ==> 120
16  ==> 136
17  ==> 153
18  ==> 171
19  ==> 190
20  ==> 210
21  ==> 231
22  ==> 253
23  ==> 276
24  ==> 300
25  ==> 325
26  ==> 351
27  ==> 378
28  ==> 406
29  ==> 435
30  ==> 465
31  ==> 496
32  ==> 528
33  ==> 561
34  ==> 595
35  ==> 630
36  ==> 666
37  ==> 703
38  ==> 741
39  ==> 780
40  ==> 820
41  ==> 861
42  ==> 903
43  ==> 946
44  ==> 990
45  ==> 1035
46  ==> 1081
47  ==> 1128
48  ==> 1176
49  ==> 1225
50  ==> 1275
51  ==> 1326
52  ==> 1378
53  ==> 1431
54  ==> 1485
55  ==> 1540
56  ==> 1596
57  ==> 1653
58  ==> 1711
59  ==> 1770
60  ==> 1830
61  ==> 1891
62  ==> 1953
63  ==> 2016
64  ==> 2080
65  ==> 2145
66  ==> 2211
67  ==> 2278
68  ==> 2346
69  ==> 2415
70  ==> 2485
71  ==> 2556
72  ==> 2628
73  ==> 2701
74  ==> 2775
75  ==> 2850
76  ==> 2926
77  ==> 3003
78  ==> 3081
79  ==> 3160
80  ==> 3240
81  ==> 3321
82  ==> 3403
83  ==> 3486
84  ==> 3570
85  ==> 3655
86  ==> 3741
87  ==> 3828
88  ==> 3916
89  ==> 4005
90  ==> 4095
91  ==> 4186
92  ==> 4278
93  ==> 4371
94  ==> 4465
95  ==> 4560
96  ==> 4656
97  ==> 4753
98  ==> 4851
99  ==> 4950
100  ==> 5050
 1 ~ 10까지의 합 :  5050
>>> 
================== RESTART: C:/Users/BSH/Desktop/코딩 실습/3day.py =================
 1 ~ 10까지의 합 :  5050
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/3day.py
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/3day.py
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/3day.py
서울
대구
부산
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/3day.py
 ***  2 단 ***
2  *  1  =  2
2  *  2  =  4
2  *  3  =  6
2  *  4  =  8
2  *  5  =  10
2  *  6  =  12
2  *  7  =  14
2  *  8  =  16
2  *  9  =  18
 ****************** 
 ***  3 단 ***
3  *  1  =  3
3  *  2  =  6
3  *  3  =  9
3  *  4  =  12
3  *  5  =  15
3  *  6  =  18
3  *  7  =  21
3  *  8  =  24
3  *  9  =  27
 ****************** 
 ***  4 단 ***
4  *  1  =  4
4  *  2  =  8
4  *  3  =  12
4  *  4  =  16
4  *  5  =  20
4  *  6  =  24
4  *  7  =  28
4  *  8  =  32
4  *  9  =  36
 ****************** 
 ***  5 단 ***
5  *  1  =  5
5  *  2  =  10
5  *  3  =  15
5  *  4  =  20
5  *  5  =  25
5  *  6  =  30
5  *  7  =  35
5  *  8  =  40
5  *  9  =  45
 ****************** 
 ***  6 단 ***
6  *  1  =  6
6  *  2  =  12
6  *  3  =  18
6  *  4  =  24
6  *  5  =  30
6  *  6  =  36
6  *  7  =  42
6  *  8  =  48
6  *  9  =  54
 ****************** 
 ***  7 단 ***
7  *  1  =  7
7  *  2  =  14
7  *  3  =  21
7  *  4  =  28
7  *  5  =  35
7  *  6  =  42
7  *  7  =  49
7  *  8  =  56
7  *  9  =  63
 ****************** 
 ***  8 단 ***
8  *  1  =  8
8  *  2  =  16
8  *  3  =  24
8  *  4  =  32
8  *  5  =  40
8  *  6  =  48
8  *  7  =  56
8  *  8  =  64
8  *  9  =  72
 ****************** 
 ***  9 단 ***
9  *  1  =  9
9  *  2  =  18
9  *  3  =  27
9  *  4  =  36
9  *  5  =  45
9  *  6  =  54
9  *  7  =  63
9  *  8  =  72
9  *  9  =  81
 ****************** 
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/3day.py
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/3day.py
 출력할 단 : 1
Traceback (most recent call last):
  File "C:/Users/BSH/Desktop/코딩 실습/3day.py", line 21, in <module>
    for i in range(a, 10):
NameError: name 'a' is not defined
>>> 2
2
>>> 3
3
>>> 4
4
5
>>> 
>>> 56
56
6
>>> 
>>> 67
67
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/3day.py
 출력할 단 : 2
Traceback (most recent call last):
  File "C:/Users/BSH/Desktop/코딩 실습/3day.py", line 21, in <module>
    for i in range(a, 10):
NameError: name 'a' is not defined
>>> 5
5
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/3day.py
0
1
2
3
4
5
6
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/3day.py
0
1
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/3day.py
0
1
3
4
5
6
Traceback (most recent call last):
  File "C:/Users/BSH/Desktop/코딩 실습/3day.py", line 31, in <module>
    print(end)
NameError: name 'end' is not defined
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/3day.py
0
1
3
4
5
6
end
>>> 