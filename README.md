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
