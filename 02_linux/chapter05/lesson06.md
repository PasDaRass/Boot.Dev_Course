<h3>Exit Codes</h3>

0 is the exit code for success. Any other exit code is an error. 9 times out of 10, if a non-zero exit code is returned (meaning an error) it will be 1, which is the "catch-all" error code.
<br />
Programs that call other programs use error codes to figure out if execution was successful.
<br />
In a shell, you can access the exit code of the last program you ran with the question mark variable ($?). For example, if you run a program that exits with a non-zero exit code, you can see what it was with the echo command:

```
ls ~
echo $?
# 0
```
```
ls /does/not/exist
echo $?
# 1
```
