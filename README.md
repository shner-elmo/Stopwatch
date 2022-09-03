# Python Stopwatch

#### This module contains a class and function to time your code easily  
Below are some examples:
---

First import the Stopwatch class
```py
from stopwatch import Stopwatch
```

For the purpose of the tutorial were going to use this function which takes about 1.5 seconds to run
```python
def func():
    x = ''
    for i in range(1_000_000):
        x += str(i)
```

Using the with statement:
```py
with Stopwatch() as sw:
    func()
    print(sw.time_elapsed)
```
```
1.4438485999708064
```

Or you can print the instance itself, which will return a nicely formatted string:
```python
print(sw)
```
```
Time elapsed: 1.444
```
---

You can also a pass an instance of a class to automatically add the time taken to the total elapsed time of the insatnce: 
```python
sw = Stopwatch()

with sw:
    func()

func()

with sw:
    func()
    
print(sw)
```
```
'2.7854167000041343'
```
---

The above example is the equivalent of:
```python
sw = Stopwatch()

sw.start()
func()
sw.stop()

func()

sw.start()
func()
sw.stop()

print(sw)
```
```
'2.9421735999640077'
```
---

#### You can also use the decorator to time a function every time you run it

First import the decorator:
```python
from stopwatch import time_it
```

Add it to your function:
```python
@time_it()
def func():
    x = ''
    for i in range(1_000_000):
        x += str(i)
```

Now it will return a tuple with the time taken and the output of the function (which in our case is None)
```python
print(func())
```
```
(1.1367347000050358, None)
```

You can also add the time taken to an existing instance of Stopwatch like so:
```python
sw = Stopwatch()

@time_it(stopwatch=sw)
def func():
    x = ''
    for i in range(1_000_000):
        x += str(i)
```

Call the function twice:
```python
print('Out:', func())
print('Total time elapsed:', sw.time_elapsed)
print('Out:', func())
print('Total time elapsed:', sw.time_elapsed)
```
```
Out: (1.3642582000466064, None)
Total time elapsed: 1.3642542000161484
Out: (1.3336866000317968, None)
Total time elapsed: 2.6979382000281475
```