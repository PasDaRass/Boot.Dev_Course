<h4>Negation</h4>
You can add comments to your .gitignore file by starting a line with a #. For example:

```
# Ignore all .txt files
*.txt
```

<h4>Order Matters</h4>
The order of patterns in a .gitignore file determines their effect, and patterns can override each other. For example:

```
temp/*
!temp/instructions.md
```

Everything in the temp/ directory would be ignored except for instructions.md. If the order were reversed, instructions.md would be ignored.
