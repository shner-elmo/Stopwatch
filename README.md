# Python Stopwatch

This package contains two modules with each its own Stopwatch class;

One in basic_stopwatch.py, which is great for testing the time taken for a piece of 
code to run, for ex:

```py
from src.basic_stopwatch import Stopwatch
```

For the purpose of the tutorial were going to use this function which takes about 1.5 seconds to run
```python
def func():
    x = ''
    for i in range(1_000_000):
        x += str(i)
```
```py
sw = Stopwatch()
func()
print(sw)
```
```
'Time elapsed: 1.575'
```

Or with the Context Manager: (it will automatically print the time elapsed at the end)
```py
with Stopwatch():
    func()
```
```
'Time elapsed: 1.589'
```

And the second is in stopwatch.py,  
which has more features, including: start, stop, laps, resets, etc...

```python
from src.stopwatch import Stopwatch
```
```python
sw = Stopwatch()

sw.start()
func()
sw.stop()

func()

sw.start()
func()
sw.stop()

print(sw.time_elapsed)
```
```
'2.7854167000041343'
```

Or you can use a context manager which will start and stop the Stopwatch automatically:
```python
sw = Stopwatch()

with sw:
    func()

func()

with sw:
    func()
    
print(sw.time_elapsed)
```
```
'2.9421735999640077'
```

#### You can also use the decorator to time a function every time you run it

First import the decorator:
```python
from src.stopwatch import time_it
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

You can also add the time take to an existing instance of Stopwatch like so:
```python
sw = Stopwatch()

@time_it(stopwatch=sw)
def func():
    x = ''
    for i in range(1_000_000):
        x += str(i)
```
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