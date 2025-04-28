Let's say we start with this:
```
A - B - C    main
   \
    D - E    vimchadsonly
```
And we merge vimchadsonly into main by running this while on main:
```
git merge vimchadsonly
```
The merge will:
<ul>
  <li>
    
Find the "merge base" commit, or "best common ancestor" of the two branches. In this case, A.
  </li>
  <li>
Replays the changes from main, starting from the best common ancestor, into a new commit.
    
  </li>
  <li>
    
Replays the changes from vimchadsonly onto main, starting from the best common ancestor.
  </li>
  <li>
Records the result as a new commit, in our case, F.
    
  </li>
  <li>
    
F is special because it has two parents, C and E.
  </li>
</ul>
After:

```
A - B - C - F    main
   \     /
    D - E        vimchadsonly
```
