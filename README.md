# hackxor

`hackxor` (pronounced "haxor" [1]) is an ~~evil~~ cool library that turns the `^` operator into exponentiation on `int`s and `float`s. You know, akin to other great programming languages like... VBA?

```python
>>> x = 2
>>> print(x ^ 2)
0
>>> import hackxor
>>> print(x ^ 2)
4
```

Once you import `hackxor`, things will randomly break. Pretty sick.

```python
>>> import hackxor
>>> import hmac
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.12/hmac.py", line 19, in <module>
    trans_5C = bytes((x ^ 0x5C) for x in range(256))
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: bytes must be in range(0, 256)
```

Note: Python's ast optimizier performs simple [constant folding](https://github.com/python/cpython/blob/c618f7d80e78f83cc24b6bdead33ca38cbd4d27f/Python/ast_opt.c#L450). Because of this, you might see some ~~confusing~~ cool behavior.

```python
>>> from pathlib import Path
>>> print(Path("surprise.py").read_text())
print(2 ^ 2)
x = 2
print(x ^ 2)
>>> import hackxor
>>> import surprise
0
4
```

> [1] Haxor, and derivations thereof, is leet for "hacker".
