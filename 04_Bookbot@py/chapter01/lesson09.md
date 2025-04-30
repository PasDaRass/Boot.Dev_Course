# Read File
Let's start actually building "bookbot"! Here are some things you'll need to know how to do for this step:

<h5>with Block</h5>
A with block can be used to open a file:

```
with open(path_to_file) as f:
    # do something with f (the file) here
```
The with block will automatically close the file when the block is exited, cleaning up resources.

<h5>.read() Method</h5>
You can use the .read() method to read the contents of a file into a string:

```
# f is a file object
file_contents = f.read()
```
