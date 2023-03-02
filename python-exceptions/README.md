<h1 align="center">Python 🐍 -  Exceptions</h1>

### Recommended Links 🔗
- [Exceptions in Python](https://www.youtube.com/watch?v=nlCKrKGHSSk)

- [Python Exception Handling (Use Try..Except to Catch Errors!)](https://www.youtube.com/watch?v=brICUKrzVR0)

- [Excepciones I](https://www.youtube.com/watch?v=2MaAs7XU2T0)

- [Excepciones II](https://www.youtube.com/watch?v=HH3c6ZBvSx8)

### Learning Objectives 🎯
- Why Python programming is awesome
- What’s the difference between errors and exceptions
- What are exceptions and how to use them
- When do we need to use exceptions
- How to correctly handle an exception
- What’s the purpose of catching exceptions
- How to raise a builtin exception
- When do we need to implement a clean-up action after an exception

### Tasks 📚

__1. Safe printing of an integers list__

- Write a function that prints an integer with ``"{:d}".format()``
	- Prototype: def ``safe_print_integer(value):``
	- ``value`` can be any type (integer, string, etc.)
	- The integer should be printed followed by a new line
	- Returns ``True`` if ``value`` has been correctly printed (it means the ``value`` is an integer)
	- Otherwise, returns ``False``
	- You have to use ``try: / except:``
	- You have to use ``"{:d}".format()`` to print as integer
	- You are not allowed to import any module
	- You are not allowed to use ``type()``

__2. Print and count integers__	
- Write a function that prints the first x elements of a list and only integers.
	- Prototype: ``def safe_print_list_integers(my_list=[], x=0):``
	- ``my_list`` can contain any type (integer, string, etc.)
	- All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
	- ``x`` represents the number of elements to access in ``my_list``
	- ``x`` can be bigger than the length of ``my_list`` - if it’s the case, an exception is expected to occur
	- Returns the real number of integers printed
	- You have to use ``try: / except:``
	- You have to use ``"{:d}".format()`` to print an integer
	- You are not allowed to import any module
	- You are not allowed to use ``len()``
