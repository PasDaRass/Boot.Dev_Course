<strong>stderr</strong> represents an error that has occured within the print function

<h3>Redirecting Streams</h3>
You can redirect stdout and stderr to different places using the > and 2> operators. > redirects stdout, and 2> redirects stderr.
<p>
  
Redirect stdout to a File
</p>

```
echo "Hello world" > hello.txt
cat hello.txt
# Hello world
```

Redirect stderr to a File
```
cat doesnotexist.txt 2> error.txt
cat error.txt
# cat: doesnotexist.txt: No such file or directory
```
