<ol>
  <li>
Add a new function to your stats.py file that takes the text from the book as a string, and returns the number of times each character, (including symbols and spaces), appears in the string.
    
  </li>
  <li>
    
Convert any character to lowercase using the .lower() method, we don't want duplicates.
  </li>
  <li>
    
Use a dictionary of String -> Integer. The returned dictionary should look something like this:
  </li>
  <li>
Import and call the function in main.py, and capture the result in a new variable.
    
```
{'p': 6121, 'r': 20818, 'o': 25225, ...
```
  </li>
</ol>

After printing the word count, print the dictionary of characters and their counts.
