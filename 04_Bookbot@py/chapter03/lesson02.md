# System Arguments
The built in sys module provides access to command line arguments. In particular sys.argv is a list of strings representing the arguments passed to the script. The first argument is the script name, the rest are the arguments.
<br />
For example, python3 main.py will result in a sys.argv list that looks like this:
```
['main.py']
```
And python3 main.py books/frankenstein.txt will result in a sys.argv list that looks like this:
```
['main.py', 'books/frankenstein.txt']
```
