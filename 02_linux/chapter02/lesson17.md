<h4>Find</h4>
<p>
  
The find command is a powerful tool for finding files and directories by name, not by their contents.
</p>

<h4>Find a File by Name</h4>
<p>
  
Let's say you're looking for a file named hello.txt somewhere in your home directory. You can use the find command to search for exactly that title:
</p>

```
find some_directory -name hello.txt
```
<h4>Pattern Search</h4>
<p>
  
The find command can also search for files that match a pattern. For example, if you wanted to find all files that end in .txt, you could run:
</p>

```
find some_directory -name "*.txt"
```
<p>
  
The * character is a wildcard that matches anything. If you're trying to find filenames that contain a specific word, you can use the * character to match the rest of the filename:
</p>

```
# Find all filenames that contain the word "chad"
find some_directory -name "*chad*"
```
