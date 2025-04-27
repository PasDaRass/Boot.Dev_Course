While it's true that Git stores entire snapshots on per-commit level, 
it does have some performance optimizations so that your .git directory doesn't get too unbearably large.
<ul>
  <li>
    
Git compresses and packs files to store them more efficiently.
  </li>
  <li>
    
Git deduplicates files that are the same across different commits. 
  </li>
</ul>

If a file doesn't change between commits, Git will only store it once.
