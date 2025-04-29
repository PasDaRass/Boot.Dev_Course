A problem arises when we want to put files in our project's directory, but we don't want to track them with Git. A .gitignore file solves this. For example, if you work with Python, you probably want to ignore automatically generated files like .pyc and __pycache__. 
If you are building a server, you probably want to ignore .env files that might hold private keys. 
If you (I'm sorry) work with JavaScript, you might want to ignore the node_modules directory.

Here's an example .gitignore file, which exists at the root of a repo:
```
node_modules
```
This will ignore every path containing node_modules as a "section" (directory name or file name). It ignores:
<ul>
  <li>
    
node_modules/code.js
  </li>
  <li>
    
src/node_modules/code.js
  </li>
  <li>
src/node_modules
    
  </li>
</ul>
It does not ignore:

```
src/node_modules_2/code.js
env/node_modules_3
```
