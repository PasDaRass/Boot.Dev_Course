# Patterns
It would be rough if .gitignore files only accepted exact filepath section names. Luckily, they don't!

Let's go over some of the most common patterns.
<br />
<h4>Wildcards</h4>
The * character matches any number of characters except for a slash (/). For example, to ignore all .txt files, you could use the following pattern:

```
*.txt
```

<h4>Rooted Patterns</h4>
Patterns starting with a / are anchored to the directory containing the .gitignore file. For example, this would ignore a main.py in the root directory, but not in any subdirectories:

```
/main.py
```

<h4>Negation</h4>
You can negate a pattern by prefixing it with an exclamation mark (!). For example, to ignore all .txt files except for important.txt, you could use the following pattern:

```
*.txt
!important.txt
```
