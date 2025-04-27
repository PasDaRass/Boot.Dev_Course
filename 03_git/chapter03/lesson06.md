Here are some terms to know:
<ul>
  <li>
    
tree: git's way of storing a directory
  </li>
  <li>
    
blob: git's way of storing a file
  </li>
</ul>
Here's an example commit:

> git cat-file -p 5ba786fcc93e8092831c01e71444b9baa2228a4f
```
tree 4e507fdc6d9044ccd8a4a3061324c9f711c4667d
author ThePrimeagen <the.primeagen@aol.com> 1705891256 -0700
committer ThePrimeagen <the.primeagen@aol.com> 1705891256 -0700

A: add contents.md
```
Notice that we can see:
<ul>
  <li>
    
The tree object
  </li>
  <li>
    
The author
  </li>
  <li>
    
The committer
  </li>
  <li>
The commit message
    
  </li>
</ul>

However, we cannot see the contents of the contents.md file itself! That's because the blob object stores it.
