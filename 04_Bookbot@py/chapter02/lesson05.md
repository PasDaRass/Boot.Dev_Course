Refactoring is a fancy word for "rewriting your god-awful code so it's not so terrible." Refactoring doesn't change the behavior of your code, just the way it's written.
<br />
Let's refactor our project to use multiple Python files. Not only will it be useful for you to learn how to split code across files, but in this case, it will help us organize our code. We'll use this structure:

```
main.py - The entry point to our program and any code that doesn't fit elsewhere
stats.py - A file that contains functions for analyzing the text
```
