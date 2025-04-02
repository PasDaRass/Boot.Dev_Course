Files with a .sh extension are shell scripts. They're just text files that contain shell commands. You can run a file in your shell by typing its filepath:
```
mydir/program.sh
```
Interestingly, if the program is in the current directory (in this example, the mydir directory), you need to prefix it with ./ to run it:
```
./program.sh
```
As far as file paths go, ./program.sh and program.sh are the same. The dot (.) is an alias for the current directory. We need the prefix when running executables so that the shell knows we're trying to run a file from a file path, not an installed command like ls, mkdir, chmod, etc.

<h3>Assignment</h3>

Run the following commands in worldbanc/private/bin:
```
chmod -x genids.sh
```
Let's test those permission changes. Try to run the script:
```
./genids.sh
```
You should get an error like this:
```
permission denied
```
That error occurs because the executable permission has been removed. Let's re-add the executable permission for the owner:
```
chmod u+x <filename>
```
Once you've done that, try running the ./genids.sh script again.
