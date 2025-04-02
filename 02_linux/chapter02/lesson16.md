You can also search multiple files at once. For example, if we wanted to search for the word "hello" in hello.txt and hello2.txt, we could run:
```
grep "hello" hello.txt hello2.txt
```

You can also search an entire directory, including all subdirectories. For example, to search for the word "hello" in the current directory and all subdirectories:
```
grep -r "hello" .
```
<em>The . is a special alias for the current directory.</em>
