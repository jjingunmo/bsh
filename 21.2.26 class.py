Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> 
================== RESTART: C:/Users/BSH/Desktop/코딩 실습/5day.py =================
>>> f1
<function f1 at 0x000001DA37BDA310>
>>> f1()
>>> f2()
안녕. 난 f2...
>>> f3()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    f3()
TypeError: f3() missing 1 required positional argument: 'x'
>>> f3(메롱)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    f3(메롱)
NameError: name '메롱' is not defined
>>> f3('메롱')
메롱 f3...
>>> f3(10)
10 f3...
>>> f2
<function f2 at 0x000001DA37CA8310>
>>> f2()
안녕. 난 f2...
>>> f2(), f3(10)
안녕. 난 f2...
10 f3...
(None, None)
>>> f2() + f3(10)
안녕. 난 f2...
10 f3...
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    f2() + f3(10)
TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
>>> f2() = f3(10)
SyntaxError: cannot assign to function call
>>> f2() / f3(10)
안녕. 난 f2...
10 f3...
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    f2() / f3(10)
TypeError: unsupported operand type(s) for /: 'NoneType' and 'NoneType'
>>> f1(0)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    f1(0)
TypeError: f1() takes 0 positional arguments but 1 was given
>>> f2(0)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    f2(0)
TypeError: f2() takes 0 positional arguments but 1 was given
>>> f3(1, 2, 3)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    f3(1, 2, 3)
TypeError: f3() takes 1 positional argument but 3 were given
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/5day.py
>>> f3(4, 6, '짱')
4 f3...
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/5day.py
>>> f2()
안녕. 난 f2...
>>> f3('응, 만나서 반가워')
응, 만나서 반가워 f3...
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/5day.py
>>> f4(4,6)
f4 ==>  10
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/5day.py
f4 ==>  60
>>> f4(5)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    f4(5)
TypeError: f4() missing 1 required positional argument: 'bb'
>>> f4(5,6)
f4 ==>  11
>>> f4('사랑해','486')
f4 ==>  사랑해486
>>> aa
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    aa
NameError: name 'aa' is not defined
>>> f2()
안녕. 난 f2...
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/5day.py
>>> f5(1, 2, 3,)
6
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/5day.py
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/5day.py
>>> f6(30, 50, 20)
100
>>> f5(1, 2, 3)
6
>>> ret = f5(1, 2, 3)
6
>>> ret
>>> ret = f6(30, 50, 20)
>>> ret
100
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/5day.py
>>> Add(20, 30)
20  +  30  +  20 30
>>> return_value = Add(20, 40)
20  +  40  +  20 40
>>> print(return_value)
None
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/5day.py
>>> return_value = Add(20, 40)
20  +  40  +  20 40
>>> print(return_value)
(20, 40)
>>> return_value = Add(20+40)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    return_value = Add(20+40)
TypeError: Add() missing 1 required positional argument: 'number2'
>>> return_value = Add(20, 40)
20  +  40  +  20 40
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/5day.py
>>> r = f7
>>> r
<function f7 at 0x0000027D2ED88670>
>>> r = f7()
>>> r
100
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/5day.py
>>> r = f7()
>>> t
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    t
NameError: name 't' is not defined
>>> r
(0, 300, 500, 1000)
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/myCalc.py
>>> Plus(1,4)
5
>>> Minus(100, 60345435)
-60345335
>>> Minus(100, 60)
40
>>> Muti(100,10)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    Muti(100,10)
NameError: name 'Muti' is not defined
>>> Multi(100,10)
1000
>>> Divi(9,3)
3
>>> 
= RESTART: C:/Users/BSH/Desktop/코딩 실습/myCalc.py
 첫번째 수 : 3
 [+, -, *, / ] : *2
 두번째 수 : 2
 첫번째 수 : 2
 [+, -, *, / ] : +
 두번째 수 : 2
 2 + 2 = 4
 첫번째 수 : 3
 [+, -, *, / ] : -
 두번째 수 : 2
 3 - 2 = 1
 첫번째 수 : 4
 [+, -, *, / ] : *
 두번째 수 : 5
 4 * 5 = 20
 첫번째 수 : 5
 [+, -, *, / ] : /
 두번째 수 : 3
 5 / 3 = 1
 첫번째 수 : 0
 Bye-Bye!! 
>>> 