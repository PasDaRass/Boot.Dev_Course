<h3>Pipe</h3>
<p>
  
The pipe operator is |. It's the character that looks like a vertical line. It's usually on the same key as the backslash (\) above the enter key. The pipe operator takes the stdout of the program on the left and "pipes" it into the stdin of the program on the right.
</p>

```
echo "Have you heard the tragedy of Darth Plagueis the Wise?" | wc -w
  
# 10
```
<p>
  
In the example above, the echo command sends "Have you heard the tragedy of Darth Plagueis the Wise?" to stdout.
</p>
<p>
  
However, instead of that text being sent to your terminal, the pipe operator pipes it into the wc (word count) command. The wc command counts the number of words in the input it receives. The -w flag tells wc to only count words.
</p>
<p>
  
This only works because the wc command, like most shell commands, can optionally read from stdin instead of a filepath
</p>
