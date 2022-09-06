# Python Stopwatch

#### This module contains a Stopwatch class with a context manager and a decorator function to time your code easily  

Below are some examples:

---

First import the Stopwatch class
```py
from stopwatch import Stopwatch
```

For the tutorial we're going to use this function which takes a bit more than a second to run
```python
def func():
    x = ''
    for i in range(1_000_000):
        x += str(i)
```

Instantiate the Stopwatch class:
```python
sw = Stopwatch()

sw.start()
func()
sw.stop()

print('Time elapsed:', sw.time_elapsed)
```
```
Time elapsed: 1.2138440999988234
```

Or we can simply print the instance which will return a nicely formatted string:
```python
print(sw)
```
```
Time elapsed: 1.214
```
---

Using the 'with' statement:
```py
with Stopwatch() as sw:
    func()
    print(sw)
```
```
Time elapsed: 1.138
```

You can also pass an instance of a class to automatically add the time taken to the total elapsed time of the instance: 
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
Time elapsed: 2.328
```

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
Time elapsed: 2.324
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

Now the function will return a tuple with the time taken and the output of the function (which in our case is None)
```python
print(func())
```
```
(1.1769665000028908, None)
```

You can also add the time taken to an existing Stopwatch instance like so:
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
print(sw)
print('Out:', func())
print(sw)
```
```
Out: (1.2755557999989833, None)
Time elapsed: 1.276
Out: (1.3011283000014373, None)
Time elapsed: 2.577
```
