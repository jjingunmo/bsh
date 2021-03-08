Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [1, 2, 4, 6, 9, 3, 5]
>>> b = (2, 4, 6, 7, 5, 6, 6)
>>> c = {2, 3, 4, 2, 3, 3}
>>> d = {'1':'one', '2':'two'}
>>> 
>>> type(a)
<class 'list'>
>>> type(b)
<class 'tuple'>
>>> type(c)
<class 'set'>
>>> type(d)
<class 'dict'>
>>> a
[1, 2, 4, 6, 9, 3, 5]
>>> b
(2, 4, 6, 7, 5, 6, 6)
>>> c
{2, 3, 4}
>>> d
{'1': 'one', '2': 'two'}
>>> a == b
False
>>> a == a
True
>>> d.keys()
dict_keys(['1', '2'])
>>> d.values()
dict_values(['one', 'two'])
>>> d.keys
<built-in method keys of dict object at 0x000001F18A37C500>
>>> a
[1, 2, 4, 6, 9, 3, 5]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> min(a)
1
>>> max(a)
9
>>> sum(a)
30
>>> min([4, 8, 9, 3])
3
>>> 
>>> max([4, 8, 9, 3])
9
>>> sum([4, 8, 9, 3])
24
>>> sum(2, 3, 4)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    sum(2, 3, 4)
TypeError: sum() takes at most 2 arguments (3 given)
>>> 2 * 3
6
>>> 2 ** 3
8
>>> pow(2, 3)
8
>>> 20 / 3
6.666666666666667
>>> 20 // 3
6
>>> 20 % 3
2
>>> import math
>>> math.pi
3.141592653589793
>>> math.cos(10)
-0.8390715290764524
>>> math.cos(2, 10)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    math.cos(2, 10)
TypeError: math.cos() takes exactly one argument (2 given)
>>> math.cos(2)
-0.4161468365471424
>>> math.tan(10)
0.6483608274590866
>>> math.sin(10)
-0.5440211108893698
>>> math.log(8)
2.0794415416798357
>>> math.log(8, 2)
3.0
>>> math.factorial(2)
2
>>> math.factorial(3)
6
>>> math.factorial(4)
24
>>> math.factorial(50)
30414093201713378043612608166064768844377641568960512000000000000
>>> math.factorial(10)
3628800
>>> math.factorial(80)
71569457046263802294811533723186532165584657342365752577109445058227039255480148842668944867280814080000000000000000000
>>> math.factorial(100)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
>>> math.factorial(80)
71569457046263802294811533723186532165584657342365752577109445058227039255480148842668944867280814080000000000000000000
>>> range(5)
range(0, 5)
>>> range(10)
range(0, 10)
>>> for i in range(0, 5):
	print(i, end = ' ')

	
0 1 2 3 4 
>>> for i in range(1, 11, 2):
	print(i, end = ' ')

	
1 3 5 7 9 
>>> for i in range(0, 11):
	print(i, end = ' ')

	
0 1 2 3 4 5 6 7 8 9 10 
>>> for i in range(1, 10):
	print(i, end = ' ')

	
1 2 3 4 5 6 7 8 9 
>>> for i in range(2, 11, 2):
	print(i, end = ' ')

	
2 4 6 8 10 
>>> for i in range(0, 11, 3):
	print(i, end = ' ')

	
0 3 6 9 
>>> for i in range(0, 11, 3):
	print(i)

	
0
3
6
9
>>> for i in range(0, 11, 5):
	print(i, end = ' ')

	
0 5 10 
>>> for i in range(0, 11, 5):
	print(i, end = '.')

	
0.5.10.
>>> for i in range(0, 11, 5):
	print(i, end = '/')

	
0/5/10/
>>> for i in range(0, 11, 5):
	print(i, end = 'asd')

	
0asd5asd10asd
>>> for i in range(0, 11, 5):
	print(i, end = '/t')

	
0/t5/t10/t
>>> for i in range(0, 11, 5):
	print(i, end = ' /t ')

	
0 /t 5 /t 10 /t 
>>> for i in range(0, 11, 5):
	print(i, end = ' \t ')

	
0 	 5 	 10 	 
>>> for i in range(0, 12):
	print(i, end = ' \t ')

	
0 	 1 	 2 	 3 	 4 	 5 	 6 	 7 	 8 	 9 	 10 	 11 	 
>>> for i in range(0, 12):
	print(i, end = '\')
	      
SyntaxError: EOL while scanning string literal
>>> for i in range(0, 12):
	print(i, end = ' \ ')
	
SyntaxError: invalid escape sequence \ 
>>> bin(15)
'0b1111'
>>> 5.15
5.15
>>> 5.15 - 5.05
0.10000000000000053
>>> Sum = 0
>>> for i in range(0, 100):
	print(i, end = '  ')

	
0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99  
>>> for i in range(0, 101):
	print(i, end = '  ')

	
0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90  91  92  93  94  95  96  97  98  99  100  
>>> for i in range(0, 101):
	Sum = Sum + i

	
>>> 
>>> Sum
5050
>>> Sum = 0.0
>>> for i in range(0, 101):
	Sum = Sum + i

	
>>> Sum
5050.0
>>> for i in range(0, 101):
	Sum = Sum + 0.7

	
>>> Sum
5120.699999999982
>>> Sum = 0.0
>>> for i in range(0, 101):
	Sum = Sum + 0.7

	
>>> Sum
70.70000000000013
>>> print(' %f \n' %(Sum))
 70.700000 

>>> print(' %.20f \n' %(Sum))
 70.70000000000013073986 

>>> print(' %.2f \n' %(Sum))
 70.70 

>>> for i in range(1, 101):
	Sum = Sum + 0.7

	
>>> 
>>> Sum
140.70000000000016
>>> Sum = 0.0
>>> for i in range(1, 101):
	Sum = Sum + 0.7

	
>>> Sum
70.00000000000013
>>> print(' %.2f \n' %(Sum))
 70.00 

>>> 4 + 5j
(4+5j)
>>> aa = 4 + 5j
>>> bb = 9 + 2j
>>> type(aa)
<class 'complex'>
>>> aa.real
4.0
>>> aa.imag
5.0
>>> aa + bb
(13+7j)
>>> aa -bb
(-5+3j)
>>> aa * bb
(26+53j)
>>> aa // bb
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    aa // bb
TypeError: can't take floor of complex number.
>>> aa / bb
(0.5411764705882353+0.4352941176470588j)
>>> p = 'programming'
>>> p
'programming'
>>> type(p)
<class 'str'>
>>> 
>>> p[0]
'p'
>>> p[1]
'r'
>>> p[3]
'g'
>>> p[11]
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    p[11]
IndexError: string index out of range
>>> p[-11:]
'programming'
>>> p[5:-4]
'am'
>>> p[0:-11]
''
>>> p[0:-1]
'programmin'
>>> p[0:]
'programming'
>>> p[-11:]
'programming'
>>> p[0:100000000000000000000000000]
'programming'
>>> p[0:2]
'pr'
>>> p[0:3]
'pro'
>>> p[0:3] == p[-8:-11]
False
>>> p[0:2] == p[-11:-9]
True
>>> p[0:2] + p[-11:-9]
'prpr'
>>> p[0:2] * p[-11:-9]
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    p[0:2] * p[-11:-9]
TypeError: can't multiply sequence by non-int of type 'str'
>>> p[0:2] * p[-11:-0]
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    p[0:2] * p[-11:-0]
TypeError: can't multiply sequence by non-int of type 'str'
>>> p[0:2] * p[-11:-8]
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    p[0:2] * p[-11:-8]
TypeError: can't multiply sequence by non-int of type 'str'
>>> p[0:2] + p[-11:-8]
'prpro'
>>> p
'programming'
>>> print(p)
programming
>>> p + '좋아요'
'programming좋아요'
>>> P * 3
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    P * 3
NameError: name 'P' is not defined
>>> p * 3
'programmingprogrammingprogramming'
>>> p / 3
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    p / 3
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> p.find('f')
-1
>>> p.find('p')
0
>>> p.find('o')
2
>>> p.rfind('o')
2
>>> p.lfind('o')
Traceback (most recent call last):
  File "<pyshell#173>", line 1, in <module>
    p.lfind('o')
AttributeError: 'str' object has no attribute 'lfind'
>>> p.count('o')
1
>>> p.count('t')
0
>>> p.count('m')
2
>>> p.count('g')
2
>>> p.count('p')
1
>>> p.startswith('r')
False
>>> p.startswith('p')
True
>>> p.with('p')
SyntaxError: invalid syntax
>>> p.startswith('k')
False
>>> p.startswith('d')
False
>>> p.title()
'Programming'
>>> dir(p)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> p.islower()
True
>>> p.islupper()
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    p.islupper()
AttributeError: 'str' object has no attribute 'islupper'
>>> p.isupper()
False
>>> p.startswith('d')
False
>>> p.startswith('g')
False
>>> p.endwith('g')
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    p.endwith('g')
AttributeError: 'str' object has no attribute 'endwith'
>>> p.endwith('g')
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    p.endwith('g')
AttributeError: 'str' object has no attribute 'endwith'
>>> help(str.count)
Help on method_descriptor:

count(...)
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.

>>> p.endswith('g')
True
>>> bc = 'kbs mbc sbs ytn'
>>> bc
'kbs mbc sbs ytn'
>>> len(bc)
15
>>> len('korea')
5
>>> len('대한민국')
4
>>> bc.split()
['kbs', 'mbc', 'sbs', 'ytn']
>>> bc.split(  )
['kbs', 'mbc', 'sbs', 'ytn']
>>> bc.split()
['kbs', 'mbc', 'sbs', 'ytn']
>>> bc.split(      )
['kbs', 'mbc', 'sbs', 'ytn']
>>> bc.split(' ')
['kbs', 'mbc', 'sbs', 'ytn']
>>> bc.split('/')
['kbs mbc sbs ytn']
>>> bc.split( ' / ' )
['kbs mbc sbs ytn']
>>> bc.split('  /  ')
['kbs mbc sbs ytn']
>>> bc.split('  ,  ')
['kbs mbc sbs ytn']
>>> bc.split(' / ')
['kbs mbc sbs ytn']
>>> k = "추신수:뉴욕:34'A'
SyntaxError: EOL while scanning string literal
>>> k = "추신수:뉴욕:34'A'"
>>> ㅏ
Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    ㅏ
NameError: name 'ᅡ' is not defined
>>> j
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    j
NameError: name 'j' is not defined
>>> k
"추신수:뉴욕:34'A'"
>>> k.split()
["추신수:뉴욕:34'A'"]
>>> k.split(:)
SyntaxError: invalid syntax
>>> k.split(':')
['추신수', '뉴욕', "34'A'"]
>>> k2 = k.split(':')
>>> k2
['추신수', '뉴욕', "34'A'"]
>>> type(k)
<class 'str'>
>>> type(k2)
<class 'list'>
>>> d1 = 90
>>> d3 = 9.9
>>> dir()
['Sum', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'aa', 'b', 'bb', 'bc', 'c', 'd', 'd1', 'd3', 'i', 'k', 'k2', 'math', 'p']
>>> del i, k, k2
>>> dir()
['Sum', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'aa', 'b', 'bb', 'bc', 'c', 'd', 'd1', 'd3', 'math', 'p']
>>> del a, aa, b, bb
>>> dir()
['Sum', '__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'bc', 'c', 'd', 'd1', 'd3', 'math', 'p']
>>> help(del)
SyntaxError: invalid syntax
>>> help(ist)
Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    help(ist)
NameError: name 'ist' is not defined
>>> help(dir)
Help on built-in function dir in module builtins:

dir(...)
    dir([object]) -> list of strings
    
    If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it.
    If the object supplies a method named __dir__, it will be used; otherwise
    the default dir() logic is used and returns:
      for a module object: the module's attributes.
      for a class object:  its attributes, and recursively the attributes
        of its bases.
      for any other object: its attributes, its class's attributes, and
        recursively the attributes of its class's base classes.

>>> help()

Welcome to Python 3.9's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.9/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> int

help> del
The "del" statement
*******************

   del_stmt ::= "del" target_list

Deletion is recursively defined very similar to the way assignment is
defined. Rather than spelling it out in full details, here are some
hints.

Deletion of a target list recursively deletes each target, from left
to right.

Deletion of a name removes the binding of that name from the local or
global namespace, depending on whether the name occurs in a "global"
statement in the same code block.  If the name is unbound, a
"NameError" exception will be raised.

Deletion of attribute references, subscriptions and slicings is passed
to the primary object involved; deletion of a slicing is in general
equivalent to assignment of an empty slice of the right type (but even
this is determined by the sliced object).

Changed in version 3.2: Previously it was illegal to delete a name
from the local namespace if it occurs as a free variable in a nested
block.

Related help topics: BASICMETHODS

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> print('aaa')
aaa
>>> print('aaa', end = /')
      
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> print('aaa', end = \')
SyntaxError: unexpected character after line continuation character
>>> print('aaa', end = '\n')
aaa
>>> chr(65)
'A'
>>> chr(66)
'B'
>>> chr(95)
'_'
>>> ord('a')
97
>>> ord('A')
65
>>> ord('B')
66
>>> ord('_')
95
>>> for i in range(65, 91):
	print(i, end = ' ')

	
65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 
>>> for i in range(65, 91):
	print(chr(i), end = ' ')

	
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
>>> '\uac00'
'가'
>>> '\uac01'
'각'
>>> '\uac02'
'갂'
>>> '\ud7a3'
'힣'
>>> hex(ord('가'))
'0xac00'
>>> hex(ord('큐'))
'0xd050'
>>> '\ud050'
'큐'
>>> chr(55203)
'힣'
>>> chr(44032)
'가'
>>> chr('愛')
Traceback (most recent call last):
  File "<pyshell#260>", line 1, in <module>
    chr('愛')
TypeError: an integer is required (got type str)
>>> ord('愛')
24859
>>> chr('愛')
Traceback (most recent call last):
  File "<pyshell#262>", line 1, in <module>
    chr('愛')
TypeError: an integer is required (got type str)
>>> chr(12414)
'ま'
>>> chr(12415)
'み'
>>> chr(12412)
'ぼ'
>>> a = 1234
>>> b = 'boss'
>>> c = '대구시'
>>> b.encode()
b'boss'
>>> c.encode()
b'\xeb\x8c\x80\xea\xb5\xac\xec\x8b\x9c'
>>> a.encode()
Traceback (most recent call last):
  File "<pyshell#271>", line 1, in <module>
    a.encode()
AttributeError: 'int' object has no attribute 'encode'
>>> '서울시'.encode()
b'\xec\x84\x9c\xec\x9a\xb8\xec\x8b\x9c'
>>> s2 = '서울시'.encode()
>>> s2.decode()
'서울시'
>>> help()

Welcome to Python 3.9's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.9/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> ketwords
No Python documentation found for 'ketwords'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               break               for                 not
None                class               from                or
True                continue            global              pass
__peg_parser__      def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield

help> symbol

help> symbols

Here is a list of the punctuation symbols which Python assigns special meaning
to. Enter any symbol to get more help.

!=                  +                   <=                  __
"                   +=                  <>                  `
"""                 ,                   ==                  b"
%                   -                   >                   b'
%=                  -=                  >=                  f"
&                   .                   >>                  f'
&=                  ...                 >>=                 j
'                   /                   @                   r"
'''                 //                  J                   r'
(                   //=                 [                   u"
)                   /=                  \                   u'
*                   :                   ]                   |
**                  <                   ^                   |=
**=                 <<                  ^=                  ~
*=                  <<=                 _                   

help> modules

Please wait a moment while I gather a list of all available modules...


Warning (from warnings module):
  File "C:\Users\BSH\AppData\Local\Programs\Python\Python39\lib\site-packages\setuptools\distutils_patch.py", line 25
    warnings.warn(
UserWarning: Distutils was imported before Setuptools. This usage is discouraged and may exhibit undesirable behaviors or errors. Please use Setuptools' objects directly or at least import Setuptools first.
__future__          argparse            heapq               runscript
__main__            array               help                sched
_abc                ast                 help_about          scrolledlist
_aix_support        asynchat            history             search
_ast                asyncio             hmac                searchbase
_asyncio            asyncore            html                searchengine
_bisect             atexit              http                secrets
_blake2             audioop             hyperparser         select
_bootlocale         autocomplete        idle                selectors
_bootsubprocess     autocomplete_w      idle_test           setuptools
_bz2                autoexpand          idlelib             shelve
_codecs             base64              imaplib             shlex
_codecs_cn          bdb                 imghdr              shutil
_codecs_hk          binascii            imp                 sidebar
_codecs_iso2022     binhex              importlib           signal
_codecs_jp          bisect              inspect             site
_codecs_kr          browser             io                  smtpd
_codecs_tw          builtins            iomenu              smtplib
_collections        bz2                 ipaddress           sndhdr
_collections_abc    cProfile            itertools           socket
_compat_pickle      calendar            json                socketserver
_compression        calltip             keyword             sqlite3
_contextvars        calltip_w           lib2to3             squeezer
_csv                cgi                 linecache           sre_compile
_ctypes             cgitb               locale              sre_constants
_ctypes_test        chunk               logging             sre_parse
_datetime           cmath               lzma                ssl
_decimal            cmd                 macosx              stackviewer
_elementtree        code                mailbox             stat
_functools          codecontext         mailcap             statistics
_hashlib            codecs              mainmenu            statusbar
_heapq              codeop              marshal             string
_imp                collections         math                stringprep
_io                 colorizer           mimetypes           struct
_json               colorsys            mmap                subprocess
_locale             compileall          modulefinder        sunau
_lsprof             concurrent          msilib              symbol
_lzma               config              msvcrt              symtable
_markupbase         config_key          multicall           sys
_md5                configdialog        multiprocessing     sysconfig
_msi                configparser        netrc               tabnanny
_multibytecodec     contextlib          nntplib             tarfile
_multiprocessing    contextvars         nt                  telnetlib
_opcode             copy                ntpath              tempfile
_operator           copyreg             nturl2path          test
_osx_support        crypt               numbers             textview
_overlapped         csv                 opcode              textwrap
_peg_parser         ctypes              operator            this
_pickle             curses              optparse            threading
_py_abc             dataclasses         os                  time
_pydecimal          datetime            outwin              timeit
_pyio               dbm                 parenmatch          tkinter
_queue              debugger            parser              token
_random             debugger_r          pathbrowser         tokenize
_sha1               debugobj            pathlib             tooltip
_sha256             debugobj_r          pdb                 trace
_sha3               decimal             percolator          traceback
_sha512             delegator           pickle              tracemalloc
_signal             difflib             pickletools         tree
_sitebuiltins       dis                 pip                 tty
_socket             distutils           pipes               turtle
_sqlite3            doctest             pkg_resources       turtledemo
_sre                dynoption           pkgutil             types
_ssl                easy_install        platform            typing
_stat               editor              plistlib            undo
_statistics         email               poplib              unicodedata
_string             encodings           posixpath           unittest
_strptime           ensurepip           pprint              urllib
_struct             enum                profile             uu
_symtable           errno               pstats              uuid
_testbuffer         faulthandler        pty                 venv
_testcapi           filecmp             py_compile          warnings
_testconsole        fileinput           pyclbr              wave
_testimportmultiple filelist            pydoc               weakref
_testinternalcapi   fnmatch             pydoc_data          webbrowser
_testmultiphase     format              pyexpat             window
_thread             formatter           pyparse             winreg
_threading_local    fractions           pyshell             winsound
_tkinter            ftplib              query               wsgiref
_tracemalloc        functools           queue               xdrlib
_uuid               gc                  quopri              xml
_warnings           genericpath         random              xmlrpc
_weakref            getopt              re                  xxsubtype
_weakrefset         getpass             redirector          zipapp
_winapi             gettext             replace             zipfile
_xxsubinterpreters  glob                reprlib             zipimport
_zoneinfo           graphlib            rlcompleter         zlib
abc                 grep                rpc                 zoneinfo
aifc                gzip                run                 zoomheight
antigravity         hashlib             runpy               zzdummy

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> topics

Here is a list of available topics.  Enter any topic name to get more help.

ASSERTION           DELETION            LOOPING             SHIFTING
ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
BINARY              EXECUTION           NONE                STRINGS
BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
CLASSES             FRAMES              PACKAGES            TUPLES
CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING             
CONVERSIONS         LISTS               SEQUENCEMETHODS     
DEBUGGING           LITERALS            SEQUENCES           

help> lists
No Python documentation found for 'lists'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help> list

help> 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 